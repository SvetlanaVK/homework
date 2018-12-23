text1 = input('enter text1: ').lower()
text2 = input('enter text2: ').lower()

words1 = set(text1.split())
words2 = set(text2.split())

print(words1 & words2)

