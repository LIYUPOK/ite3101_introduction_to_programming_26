pyg = 'ay'

new_word = input('Enter a word:')
if len(new_word) > 0 and new_word.isalpha():
    word = new_word.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
else:
    print('empty')
