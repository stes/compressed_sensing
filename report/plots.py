import os

from numpy import *
from pylab import *
#import seaborn as sns

#sns.despine()
#sns.set_style("white")

if not os.path.exists("fig"):
    os.mkdir("fig")

size = 1000
xx, yy = meshgrid(linspace(-1,1,size), linspace(-1,1,size))

f_l0 = lambda x,y : float32(abs(x) > 0.04) + float32(abs(y) > 0.04)
f_l1 = lambda x,y : abs(x) + abs(y)
f_l2 = lambda x,y : x**2 + y**2

xx = xx.flatten()
yy = yy.flatten()

l0 = f_l0(xx,yy)
l1 = f_l1(xx,yy)
l2 = f_l2(xx,yy)

subplot(1,3,1)
imshow(l0.reshape(size,size), cmap="gray")
xticks([])
yticks([])
grid("off")
title("(a)")
subplot(1,3,2)
imshow(l1.reshape(size,size), cmap="gray")
xticks([])
yticks([])
grid("off")
title("(b)")
subplot(1,3,3)
imshow(l2.reshape(size,size), cmap="gray")
xticks([])
yticks([])
grid("off")
title("(c)")

savefig("fig/losses.pdf", bbox_inches="tight")

