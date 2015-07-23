#!/usr/bin/python2.7
import numpy as np
import matplotlib.pyplot as plt
import helperfn.style as style
import helperfn.fn as fn

# define distribution properties
xmin = -7.0
xmax = 7.0

# number of pairs generated
npairs = 4

#
# create cards
#

for i in xrange(npairs):
    NSAMPLE = np.random.randint(200)
    x = np.linspace(xmin, xmax, NSAMPLE)
    phi = np.random.uniform(0., 2.*np.pi)
    width1 = np.random.randint(4, 6)
    width2 = np.random.randint(4, 6)

    # define distribution fn
    fx1 = np.random.uniform(0, 1, NSAMPLE) * width1
    fx2 = np.random.uniform(0, 1, NSAMPLE) * width2

    # draw points from distribution
    xr = fn.fn2dist(x, fx1, NSAMPLE)
    yr = fn.fn2dist(x, fx2, NSAMPLE)
    # rotate distributions by phi
    x = xr*np.cos(phi)-yr*np.sin(phi)
    y = xr*np.sin(phi)-yr*np.cos(phi)

    # draw card 1
    fig, ax = plt.subplots()
    ax.scatter(x, y, color=style.colors[np.random.randint(len(style.colors))], lw=0.0001)
    ax.text(xmin, xmin, r'U')
    plt.axis('equal')
    plt.xlim((xmin, xmax))
    plt.ylim((xmin, xmax))
    plt.axis('off')
    plt.savefig('../renderings/find_similar_uniform%d_1.png' % (i))

    # draw card 2
    fig, ax = plt.subplots()
    ax.scatter(x, y, color=style.colors[np.random.randint(len(style.colors))], lw=0.0001)
    ax.text(xmin, xmin, r'U')
    plt.axis('equal')
    plt.xlim((xmin, xmax))
    plt.ylim((xmin, xmax))
    plt.axis('off')
    plt.savefig('../renderings/find_similar_uniform%d_2.png' % (i))
