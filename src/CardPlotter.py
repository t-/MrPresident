import numpy as np
import matplotlib.pyplot as plt
import helperfn.style as style
import helperfn.fn as fn
import sys

# define distribution properties
xmin = -7.0
xmax =  7.0
x = np.linspace(xmin,xmax,1000)
NSAMPLE = np.random.randint(200)
phi = np.random.uniform(0.,2.*np.pi)
width1 = np.random.randint(4,10)
width2 = np.random.randint(4,10)
# define distribution fn
fx1 = np.exp(-x*x/width1)
fx2 = np.exp(-x*x/width2)
# number of pairs generated
npairs = 20

#
# create cards
#

for i in xrange(npairs):
	# draw points from distribution
	xr = fn.fn2dist(x,fx1,NSAMPLE)
	yr = fn.fn2dist(x,fx2,NSAMPLE)
	# rotate distributions by phi
	x = xr*np.cos(phi)-yr*np.sin(phi)
	y = xr*np.sin(phi)-yr*np.cos(phi)

	# draw card 1
	fig, ax = plt.subplots()
	ax.scatter(x,y,color=style.colors[np.random.randint(len(style.colors))],lw=0.0001)
	plt.axis('equal')
	plt.xlim((xmin,xmax))
	plt.ylim((xmin,xmax))
	plt.axis('off')
	plt.show()
	# plt.savefig('../renderings/find_similar%d_1.png'%(i))

	# draw card 2
	fig, ax = plt.subplots()
	ax.scatter(x,y,color=style.colors[np.random.randint(len(style.colors))],lw=0.0001)
	plt.axis('equal')
	plt.xlim((xmin,xmax))
	plt.ylim((xmin,xmax))
	plt.axis('off')
	plt.show()
	# plt.savefig('../renderings/find_similar%d_2.png'%(i))
	sys.exit()
# fig, ax = plt.subplots()
# ax.text(0, 7, r'an equation: $E=mc^2$')
# ax.text(0, 5, r'an equation: $E=mc^2$')
# ax.text(0, 3, r'an equation: $E=mc^2$')
# ax.text(0, 1, r'an equation: $E=mc^2$')
# ax.axis([0, 10, 0, 10])
# # plt.axis('equal')
# plt.axis('off')
# plt.show()