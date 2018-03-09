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

def is_pronouncable(word): #function needs to be created
	return True

#all_words = open("./usa.txt", "r") #dictionary file of english words
available_domains = open("./available_domains.txt", "w") 

for i in range(0, 10): #generate 10 words
	word_length = int(random.uniform(4, 9)) #random word length from 4 - 8
	word = ""
	for j in range(0, word_length):
		word += chr(int(random.uniform(97, 122))) #get a char from random ascii value
		"""characters are picked with a uniform dist from a to z with equal probability
			 it might be better to make an array of chars and have the vowels more
			 likely to be chosen"""
	if(is_pronouncable(word)): #if it's pronouncable check if it's availabe
		domain = word + ".com"
		if is_available(domain):
			print '{} is available'.format(domain)
			available_domains.write(domain + "\n")

#loop to go through the dictionary file of words
"""for word in all_words:
	domain = word[:-1] + ".com" # removing last letter takes away the newline char in file
	if is_available(domain):
		print '{} is available!'.format(domain)
		available_domains.write(domain + " is available!\n")"""

#close files
#all_words.close()
available_domains.close()
