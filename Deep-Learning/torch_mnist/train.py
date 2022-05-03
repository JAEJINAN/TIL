from copy import deepcopy

import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim


class Trainer():
    def __init__(self, model, optimizer, crit):
        self.model = model
        self.optimizer = optimizer
        self.crit = crit

        super().__init__()

    def _train(self, x, y, config):
        self.model.train()

        # Shuffle before begin
        indices = torch.randperm(x.size(0), device=x.device)
        x = torch.index_select(x, dim=0, index=indices).split(
            config.batch_size, dim=0)
        y = torch.index_select(y, dim=0, )
