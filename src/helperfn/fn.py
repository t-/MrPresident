import numpy as np
import matplotlib.pyplot as plt
def fn2dist(x,fx,Nsample):
	fx = fx / np.sum(fx)
	cumsumf = np.cumsum(fx);
	rands = np.random.uniform(0.0,1.0,Nsample)
	return np.interp(rands, cumsumf, x)