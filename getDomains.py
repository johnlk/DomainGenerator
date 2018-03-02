import pythonwhois as pwh
domains = ['google.com', 'yahoo.com', 'flicktheories.com']
for d in domains:
	details = pwh.get_whois(d)
	#print details['contacts']['registrant']
	print details['status']

