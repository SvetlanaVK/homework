text = input('enter text: ')

words = text.split()

print('number of words: ' + str(len(words)))

ALPHABET = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

count = 0
for c in text:
	if c in ALPHABET : 
		count += 1

print('number of english letters: ' + str(count))