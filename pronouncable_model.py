import tensorflow as tf

f = open('./usa.txt', 'r') # want to build a training set on valid english words

english_words = tf.placeholder(tf.string, shape=[100, 2], name="words") #tensor will hold the file's contents + gibberish words

count = 0
for word in f:
	if count > 20:
		break
	print(word[:-1]) #excludes the newlines
	count += 1
