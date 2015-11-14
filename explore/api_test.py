import time

from pylab import *

import am

# get data from BTCE
tic = time.time()
mtx = am.timeSeries(timeStep=600,startDate='2015-02-01',endDate='2015-03-01')
toc = time.time()
print "Fetch data took: %f.1 sec" % (toc-tic)

x = mtx[:,am.BTCE_OB_PRICE]

# write API call result to file
open("BTCE-feb.txt","w").write("\n".join(map(str, x)))
