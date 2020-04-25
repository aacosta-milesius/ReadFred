# ReadFred
Python function to retrieve data from Federal Reserve database, FRED into a Python dictionary

You will need to obtain an API key from the Federal Reserve. Details of FRED are at 
[FRED API](http://api.stlouisfed.org/docs/fred/)

Here is an example of how to call the function,

```
seriesId = 'DCOILWTICO' # WTI Crude
apiKey = *your API key*
wti = getFredSeries(seriesId, apiKey)
```
