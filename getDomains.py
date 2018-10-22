import pythonwhois as pwh
import datetime
import random

"""Test if a domain has expired by comparing it's exp date and today's date"""
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
	return date.day < today.day #returns false if it becomes available on or after today's date

"""Tests if a domain is availble by checking first if it is registered, and next if it's expired"""
def is_available(domain_name):
	try:
		details = pwh.get_whois(domain_name)
	except:
		return True
	if details.get('expiration_date', 0) == 0: #if never registered, it's available
		return True
	return is_expired(details['expiration_date'][0]) #if expired it's available

def generate_new_word():
  word = ""
  word_length = int(random.uniform(4, 9)) #random word length from 4 - 8
  for j in range(0, word_length):
    word += chr(int(random.uniform(97, 122))) #get a char from random ascii value
  return word

domain_limit = 5 #how many domains do we want to find
domains_found = 0

available_domains = open("./available_domains.txt", "w") 

while domains_found < domain_limit:
  word = generate_new_word()
  domain = word + ".com"
  if is_available(domain):
    domains_found += 1
    print '{} is available'.format(domain)
    available_domains.write(domain + "\n")

available_domains.close()
