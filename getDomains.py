import pythonwhois as pwh
import datetime

def is_expired(date): #date is a datetime object
	today = datetime.datetime.now()
	#compare year
	if date.year > today.year:
		return False
	elif date.year < today.year:
		return True
	#compare month, given year is the same
	if date.month > today.month:
		return False				
	elif date.month < today.month:
		return True	
	#compare day
	return date.day < today.day #returns false if it becomes availbe on today's date

def is_available(domain_name):
	details = pwh.get_whois(domain_name)
	if details.get('expiration_date', 0) == 0: #if never registered, it's available
		return True
	return is_expired(details['expiration_date'][0])	#if expired it's available

domains = ['qqqq.com', 'kasdqoipurqwuirwek.com']

for d in domains:
	print '{} is available: {}'.format(d, is_available(d))

