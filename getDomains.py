import pythonwhois as pwh

def is_available(domain_name):
	details = pwh.get_whois(domain_name)
	return details.get('id', 'none') == 'none'

domains = ['google.com', 'flicktheories.com', 'shit.com', 'ass.com', 'pornhub.com', 'kasdqoipurqwuirwek.com']

for d in domains:
	print '{} is available: {}'.format(d, is_available(d))

