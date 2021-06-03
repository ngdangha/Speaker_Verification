import tensorflow as tf
import os
from model import verify
from configuration import get_config

config = get_config()
tf.reset_default_graph()

model_path = "./model"

if __name__ == "__main__":
    if os.path.isdir(model_path):
        verify(model_path)
    else:
        raise AssertionError("model path doesn't exist!")