import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

from scipy.io.wavfile import write
from configuration import get_config
from utils import keyword_spot

config = get_config()   # get arguments from parser
fs = 8000  # Sample rate
seconds = 10  # Duration of recording
audio_path = config.raw_path

def record():
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('./raw_data/speaker/raw.wav', fs, myrecording)  # Save as WAV file

def save_spectrogram(path):
    """ Full preprocess of text independent utterance. The log-mel-spectrogram is saved as numpy file.
        Each partial utterance is splitted by voice detection using DB
    """

    os.makedirs(path, exist_ok=True)   # make folder to save train file

    utter_min_len = (config.tisv_frame * config.hop + config.window) * config.sr    # lower bound of utterance length
    total_speaker_num = len(os.listdir(audio_path))
    train_speaker_num= (total_speaker_num//10)*9            # split total data 90% train and 10% test
    print("total speaker number : %d"%total_speaker_num)
    print("train : %d, test : %d"%(train_speaker_num, total_speaker_num-train_speaker_num))
    for i, folder in enumerate(os.listdir(audio_path)):
        speaker_path = os.path.join(audio_path, folder)     # path of each speaker
        utterances_spec = []
        k=0
        for utter_name in os.listdir(speaker_path):
            utter_path = os.path.join(speaker_path, utter_name)         # path of each utterance
            utter, sr = librosa.core.load(utter_path, config.sr)        # load utterance audio
            intervals = librosa.effects.split(utter, top_db=20)         # voice activity detection
            for interval in intervals:
                if (interval[1]-interval[0]) >= utter_min_len:           # If partial utterance is sufficient long,
                    utter_part = utter[interval[0]:interval[1]]         # save first and last 180 frames of spectrogram.
                    S = librosa.core.stft(y=utter_part, n_fft=config.nfft,
                                          win_length=int(config.window * sr), hop_length=int(config.hop * sr))
                    S = np.abs(S) ** 2
                    mel_basis = librosa.filters.mel(sr=config.sr, n_fft=config.nfft, n_mels=40)
                    S = np.log10(np.dot(mel_basis, S) + 1e-6)           # log mel spectrogram of utterances
                    
                    if (interval[1]-interval[0]) > utter_min_len:
                      utterances_spec.append(S[:, :config.tisv_frame])    # first 180 frames of partial utterance
                      utterances_spec.append(S[:, -config.tisv_frame:])   # last 180 frames of partial utterance
                    else:
                      utterances_spec.append(S[:, :config.tisv_frame])    # first 180 frames of partial utterance

        utterances_spec = np.array(utterances_spec)
        print(utterances_spec.shape)
        np.save(os.path.join(path, "speaker%d.npy"%i), utterances_spec)

if __name__ == "__main__":
    record()
    if config.verify:
        save_spectrogram(config.verify_path)
    else:
        save_spectrogram(config.enroll_path)