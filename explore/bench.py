from pylab import *

# read data: BTCE february 2015
x = map(float, open("BTCE-feb.txt"))

# plot results
plot(x, 'k-', lw=0.75)
grid()
xlabel('time')
ylabel('USD')

# show
title('BTCE')
show()
