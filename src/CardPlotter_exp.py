#!/usr/bin/python2.7
import numpy as np
import matplotlib.pyplot as plt
import helperfn.style as style
import helperfn.fn as fn
import random

# define distribution properties
xmin = 0.0
xmax = 1.0

# number of pairs generated
npairs = 4

#
# create cards
#
hashes = []
for i in xrange(npairs):
    NSAMPLE = np.random.randint(300, 500)
    x = np.linspace(xmin, xmax, NSAMPLE)

    width1 = 1
    width2 = 1

    # define distribution fn
    fx1 = np.random.exponential(0.3, NSAMPLE)
    fx2 = np.random.exponential(0.3, NSAMPLE)

    # draw points from distribution
    x = fx1
    y = fx2
    # rotate distributions by phi
    # x = xr*np.cos(phi)-yr*np.sin(phi)
    # y = xr*np.sin(phi)-yr*np.cos(phi)

    hash = random.getrandbits(128)
    a = "%032x" % hash
    a = a[0:6]

    # draw card 1
    fig, ax = plt.subplots()
    ax.scatter(x, y, color=style.colors[np.random.randint(len(style.colors))], lw=0.0001)
    ax.text(xmin, xmin, r'%s' % a)
    plt.axis('equal')
    plt.xlim((xmin, xmax))
    plt.ylim((xmin, xmax))
    plt.axis('off')
    plt.savefig('../renderings/find_similar_exp%d_1.png' % (i))

    # draw card 2
    fig, ax = plt.subplots()
    ax.scatter(x, y, color=style.colors[np.random.randint(len(style.colors))], lw=0.0001)
    ax.text(xmin, xmin, r'%s' % a)
    plt.axis('equal')
    plt.xlim((xmin, xmax))
    plt.ylim((xmin, xmax))
    plt.axis('off')
    plt.savefig('../renderings/find_similar_exp%d_2.png' % (i))

    hashes.append([a,NSAMPLE])

f = open('../renderings/hash_exp.dat', 'w')
for i in hashes:
    print >>f, i
f.close()
