Text = " " " the Quick broWn Fox jumps over the lazy dog. the quick bron fox jumped over the lazy dawg " " "

#cleaning text and lower casing all words

for char in '-_,/.!?'
    Text=Text.replace(char,' ')
Text = Text.lower()

print(Text)

#split returns a list of words delimited by sequenses of 'white spaces' (including tabs, new lines, etc. like re's /s)

word_list = Text.split()
print(word_list)

#initializing a dictionary

d={}

#counting number of times eacj word comes up in list of words (in dictionary)

for word in word_list:
    d[word] = d.get(word,0) +1

    #next piece of code reverses key and values so they can be stored (dictionaries can't be sorted on their own)
    #using tuples

    word_freq = []
    for key, value in d.items():
        word_freq.append ((value, key))
    word_freq

    word_freq.sort (reverse=True)
    print (word_freq)
