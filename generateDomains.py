import pythonwhois as pwh
import datetime as dt
import random

def is_expired(experation_date):
  now = dt.datetime.now()
  return expiration_date < now

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
  vowels = ['a', 'e', 'i', 'o', 'u']
  consanants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
  word = ""
  word_length = int(random.uniform(4, 9)) #random word length from 4 - 8
  for j in range(0, word_length):
    if(j % 2 == 0):
      word += vowels[random.randint(0, len(vowels) - 1)] #get a vowel
    else:
      word += consanants[random.randint(0, len(consanants) - 1)] #get a consanant
  return word

domain_limit = 25 #how many domains do we want to find
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
