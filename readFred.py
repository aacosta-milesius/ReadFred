# Parse a FRED query, which comes back from the web as an XML file
# http://api.stlouisfed.org/docs/fred/

# apiKey = YOUR API KEY

def getFredSeries(seriesId, apiKey):
	import urllib
	from xml.dom import minidom
	
	fredUrl = 'https://api.stlouisfed.org/fred/series/observations?series_id=%s&api_key=%s' \
		% (seriesId, apiKey)

	# Next, parse the XML retrieved in the variable, data.
	# Parse XML file to DOM tree
	xmlDoc = minidom.parse(urllib.urlopen(fredUrl))

	# Get nodes at root of tree
	cNodes = xmlDoc.childNodes

	# Direct Node Access
	nObserve = cNodes[0].getElementsByTagName('observation')

	# Make a dictionary of all XML observations
	fredDict={}
	for acct in nObserve:
		try:
			fredDict[acct.getAttribute('date')] = float(acct.getAttribute('value'))
		except ValueError:
			pass
			
	return fredDict
	


