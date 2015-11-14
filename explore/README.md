# Time series api

Install Python library:

````
cd am; python setup.py install
````

# Usage

````
>>> import am
>>> mtx = am.timeSeries(timeStep=600,startDate='2015-03-01',endDate='2015-03-02')
>>> len(mtx[:,timeseries.BTCE_OB_PRICE])
143
````

# Model Development

...
