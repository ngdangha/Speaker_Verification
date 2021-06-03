import tensorflow as tf
import numpy as np
import os
import time

from tensorflow.python.ops.array_ops import _constant_if_small
from utils import cossim, generate_enroll_batch, generate_verif_batch, random_batch, normalize, similarity, loss_cal, optim
from configuration import get_config
from tensorflow.contrib import rnn

config = get_config()

#n == speaker_number
#m == utterance_number

model_path = "./new_model"

if __name__ == "__main__":
    saver = tf.train.Saver(var_list=tf.global_variables())
    with tf.Session() as sess:
        tf.global_variables_initializer().run()

        # load model
        print("model path :", config.model_path)
        ckpt = tf.train.get_checkpoint_state(checkpoint_dir=os.path.join(config.model_path, "Check_Point"))
        ckpt_list = ckpt.all_model_checkpoint_paths
        loaded = 0
        for model in ckpt_list:
            if config.model_num == int(model.split('-')[-1]):    # find ckpt file which matches configuration model number
                print("ckpt file is loaded !", model)
                loaded = 1
                saver.restore(sess, model)  # restore variables from selected ckpt file
                model.save('model.h5')
                break

        if loaded == 0:
            raise AssertionError("ckpt file does not exist! Check config.model_num or config.model_path.")