import urllib
import StringIO
import numpy as np
TIMESTAMP=0
BTCE_PROFIT=1
BTCE_OB_PRICE=2
BTCE_OB_PRICE_VOL=3
BTCE_TRADE_PRICE=4
BTCE_TRADE_PRICE_VOL=5
BTCE_VOLUME=6

BS_PROFIT=7
BS_OB_PRICE=8
BS_OB_PRICE_VOL=9
BS_TRADE_PRICE=10
BS_TRADE_PRICE_VOL=11
BS_VOLUME=12

BFX_PROFIT=13
BFX_OB_PRICE=14
BFX_OB_PRICE_VOL=15
BFX_TRADE_PRICE=16
BFX_TRADE_PRICE_VOL=17
BFX_VOLUME=18




def timeSeries(timeStep=None,startDate=None, endDate=None):
    extra = []
    if timeStep:
        extra.append("timeStep=%d" % timeStep)
    if startDate:
        extra.append("startDate=%s" % startDate)
    if endDate:
        extra.append("endDate=%s" % endDate)
    fp = urllib.urlopen("http://www.agileminers.fi/analyze/backend/timeseries?%s" % "&".join(extra))
    return np.genfromtxt(fp, delimiter=",")


        
