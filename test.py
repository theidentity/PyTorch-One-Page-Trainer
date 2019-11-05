import matplotlib.pyplot as plt
import math
import numpy as np

def cosine_lr(opt, base_lr, e, epochs):
    lr = 0.5 * base_lr * (math.cos(math.pi * e / epochs) + 1)
    # for param_group in opt.param_groups:
    # param_group["lr"] = lr
    return lr


lambda_1 = lambda epoch: .5*.1*(math.cos(math.pi*epoch/300)+1)
x = list(range(300))
y = [lambda_1(e) for e in x]
print(y)