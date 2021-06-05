# Speaker_Verification
Modified tensorflow implementation of generalized end-to-end loss for speaker verification.
Original by Janghuyn (https://github.com/Janghyun1230/Speaker_Verification)

### Files
- configuration.py  
Argument parsing  

- data_preprocess.py  
Perform STFT for raw audio. For each raw audio, voice activity detection is performed by using librosa library.
Use for training and test data.

- utils.py   
Contain various functions for training and test.

- model.py  
Contain train, test and verify function. 
Train fucntion draws graph, starts training and saves the model and history. 
Test function load variables and test performance with test dataset.
Verify function loads 2 audio files and compares them using the model.

- test.py
Get result of verification.

- gui.py
Graphic User Interface.

- record.py
Record audio using for verfication.
run 'python record.py --verify False' to record enrollment data.
run 'python record.py --verify True' to record verify data.

### Data
- From INT3411 20 Class: 70 people, 10 utterance each person.
- I used last 5 utterances from each speaker (32 speakers). Blank of raw audio files are trimmed and then slicing is performed.

### Results
Model hyperpameters are followed by the paper :3-lstm layers with 128 hidden nodes and 64 projection nodes (Total 210434 variables), 0.01 lr sgd with 1/2 decay, l2 norm clipping with 3. To finish training and test in time, I use smaller batch (4 speakers x 5 utterances) than the paper.

TI-SV:
Random selected utterances are used. I test the model after 60000 iteration. Result is similarity matrix.

[[[ 0.77 -0.13  0.7   0.42]
  [-0.15 -0.19 -0.11 -0.24]
  [ 0.77 -0.2   0.46  0.35]
  [ 0.34 -0.06  0.16 -0.28]
  [ 0.13 -0.23  0.03 -0.4 ]]

 [[ 0.25  0.99 -0.07  0.7 ]
  [ 0.24  0.99 -0.09  0.69]
  [ 0.22  0.99 -0.06  0.69]
  [ 0.31  1.    0.02  0.71]
  [ 0.26  1.   -0.05  0.69]]

 [[ 0.58  0.    0.95  0.38]
  [ 0.27 -0.14  0.3  -0.34]
  [ 0.31 -0.15  0.34 -0.32]
  [ 0.53 -0.04  0.99  0.26]
  [ 0.51 -0.09  0.99  0.18]]

 [[ 0.59  0.64  0.62  0.85]
  [ 0.59  0.49  0.73  0.75]
  [ 0.37  0.99  0.01  0.78]
  [ 0.39  0.95  0.06  0.85]
  [ 0.33  0.99  0.01  0.75]]]

EER : 0.25 (thres:0.53, FAR:0.25, FRR:0.25)


[[[ 0.77 -0.13]
  [-0.15 -0.19]
  [ 0.77 -0.2 ]
  [ 0.34 -0.06]
  [ 0.13 -0.23]]

 [[ 0.25  0.99]
  [ 0.24  0.99]
  [ 0.22  0.99]
  [ 0.31  1.  ]
  [ 0.26  1.  ]]]

EER : 0.15 (thres:0.50, FAR:0.00, FRR:0.30)








