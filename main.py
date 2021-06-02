import tensorflow as tf
import os
from model import train, test
from configuration import get_config

config = get_config()
tf.reset_default_graph()

if __name__ == "__main__":
    # start training
    if config.train:
        print("\nTraining Session")
        os.makedirs(config.model_path)
        train(config.model_path, config.utterance_number, config.speaker_number)
    # start test
    else:
        print("\nTest session")
        if os.path.isdir(config.model_path):
            test(config.model_path, config.utterance_number, config.speaker_number)
        else:
            raise AssertionError("model path doesn't exist!")