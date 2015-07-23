#!/usr/bin/python2.7
import numpy as np
import matplotlib.pyplot as plt
import helperfn.style as style
import helperfn.fn as fn
import random

# define distribution properties
xmin = -10.0
xmax = 10.0

# number of pairs generated
npairs = 16

#
# create cards
#

hashes = []
for i in xrange(npairs):
    NSAMPLE = np.random.randint(30, 300)
    phi = np.random.uniform(0., 2.*np.pi)
    sigma1 = np.random.uniform(1.2, 2.5)
    sigma2 = np.random.uniform(1.2, 2.5)

    # draw points from distribution
    x = np.random.normal(0., sigma1, NSAMPLE)
    y = np.random.normal(0., sigma2, NSAMPLE)
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
    plt.savefig('../renderings/find_similar%d_1.png' % (i))

    # draw card 2
    fig, ax = plt.subplots()
    ax.scatter(x, y, color=style.colors[np.random.randint(len(style.colors))], lw=0.0001)
    ax.text(xmin, xmin, r'%s' % a)
    plt.axis('equal')
    plt.xlim((xmin, xmax))
    plt.ylim((xmin, xmax))
    plt.axis('off')
    plt.savefig('../renderings/find_similar%d_2.png' % (i))

    hashes.append([a, sigma1, sigma2, NSAMPLE])

f = open('../renderings/hash_gauss.dat', 'w')
for i in hashes:
    print >>f, i
f.close()
