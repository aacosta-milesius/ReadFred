# Compare the WTI/Brent spread over time from FRED data
import readFred as fed

brent = fed.getFredSeries('DCOILBRENTEU')
wti   = fed.getFredSeries('DCOILWTICO')
dates = list()

for key in wti:
	dates.append(key)
	
dates.sort()

for d in dates:
	try: # Sometimes, you don't get a price from both sources
		print '%s\t%.2f\t%.2f\t%.2f' % (d, wti[d], brent[d], brent[d] - wti[d])
	except KeyError:
		pass

