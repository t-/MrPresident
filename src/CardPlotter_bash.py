#!/usr/bin/python2.7
import numpy as np
import matplotlib.pyplot as plt
import helperfn.style as style
import helperfn.fn as fn
import random

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
    x = []
    y = []
    for f in open('../data/doom_%d.dat' % (i+1)):
        li = f.strip('\n').split(' ')
        x.append(float(li[0]))
        y.append(float(li[1]))
    NSAMPLE = np.random.randint(300, 500)
    x = np.array(x[0:NSAMPLE]) * xmax  # * 3.0
    y = np.array(y[0:NSAMPLE]) * xmax  # * 3.0

    print np.max(x), np.max(y)
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
    plt.savefig('../renderings/find_similar_bash%d_1.png' % (i))

    # draw card 2
    fig, ax = plt.subplots()
    ax.scatter(x, y, color=style.colors[np.random.randint(len(style.colors))], lw=0.0001)
    ax.text(xmin, xmin, r'%s' % a)
    plt.axis('equal')
    plt.xlim((xmin, xmax))
    plt.ylim((xmin, xmax))
    plt.axis('off')
    plt.savefig('../renderings/find_similar_bash%d_2.png' % (i))

    hashes.append(a)

f = open('../renderings/hash_bash.dat', 'w')
for i in hashes:
    print >>f, i
f.close()
