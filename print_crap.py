import random

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for x in xrange(0, 3000):
	word = ""
	word_length = random.randint(2, 10)
	for _ in xrange(0, word_length):
		word += alpha[random.randint(0, len(alpha) - 1)]
	print "{}".format(word)

