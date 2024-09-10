vowel = 0
consonant = 0
word = (input('Enter words: '))
new_word = set(word)

for alphabet in new_word:
	if (alphabet == 'a') or (alphabet == 'e') or (alphabet == 'i') or (alphabet == 'o') or (alphabet == 'u'):
		vowel = vowel + 1
		
	else:
		consonant = consonant + 1
		
print('There are',vowel, 'vowel in the word')
print('There are',consonant, 'consonant in the word')