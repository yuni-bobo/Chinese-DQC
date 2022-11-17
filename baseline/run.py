# coding: UTF-8
import time
import torch
import numpy as np
from train_eval import train
from bert import *
from utils import build_dataset, build_iterator, get_time_dif



if __name__ == '__main__':

    config = Config()
    np.random.seed(1)
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    torch.backends.cudnn.deterministic = True

    start_time = time.time()
    print("Loading data...")
    train_data, dev_data, test_data = build_dataset(config)
    train_iter = build_iterator(train_data, config)
    dev_iter = build_iterator(dev_data, config)
    test_iter = build_iterator(test_data, config)
    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)

    # train
    model = Model(config).to(config.device)
    train(config, model, train_iter, dev_iter, test_iter)
