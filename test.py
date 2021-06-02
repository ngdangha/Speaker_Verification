import tensorflow as tf
import os
from model import train, test, verify
from configuration import get_config

config = get_config()
tf.reset_default_graph()

model_path = "F:\IT\Python\Speaker_Verification\model"

if __name__ == "__main__":
    if os.path.isdir(model_path):
        verify(model_path, config.utterance_number, config.speaker_number)
    else:
        raise AssertionError("model path doesn't exist!")