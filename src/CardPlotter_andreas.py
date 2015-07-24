#!/usr/bin/python2.7
import numpy as np
import matplotlib.pyplot as plt
import helperfn.style as style
import helperfn.fn as fn
import random


def bla(num):
    return 4*num*(1-num)


def badrnd(N):
    rand = [bla(0.6)]
    for i in range(1, N):
        rand.append(bla(rand[-1]))
    return rand

# define distribution properties
xmin = 0.0
xmax = 15.0

# number of pairs generated
npairs = 4

#
# create cards
#
hashes = []
for i in xrange(npairs):
    NSAMPLE = np.random.randint(300, 500)
    a = badrnd(NSAMPLE*2)
    x = np.array(a[0:NSAMPLE]) * xmax
    y = np.array(a[NSAMPLE-1:-1]) * xmax

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
    plt.savefig('../renderings/find_similar_andreas%d_1.png' % (i))

    # draw card 2
    fig, ax = plt.subplots()
    ax.scatter(x, y, color=style.colors[np.random.randint(len(style.colors))], lw=0.0001)
    ax.text(xmin, xmin, r'%s' % a)
    plt.axis('equal')
    plt.xlim((xmin, xmax))
    plt.ylim((xmin, xmax))
    plt.axis('off')
    plt.savefig('../renderings/find_similar_andreas%d_2.png' % (i))

    hashes.append([a, '4*num*(1-num)'])

f = open('../renderings/hash_andreas.dat', 'w')
for i in hashes:
    print >>f, i
f.close()
