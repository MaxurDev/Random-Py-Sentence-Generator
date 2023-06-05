import random

print('RANDOM PY SENTENCE GENERATOR - V1.0')
print('A Random Python Sentence Generator')
print()

# Defines the list of words in order
      
# These are Template Words - Delete the words in the list if you want to add your own, or you can use a seperate file for storing them.
first = ['You','He','They','She','They',"My Mom", "My Dad"]
second = ['Could','Heard/Hears','Was/Were','Is/Are','Has/Have','Hate(s)']
third = ['A','No/Not','Both/All of the','The']
forth = ['Big','Little','One','Two','Three']
fifth = ['Liar(s)','Friend(s)','Person(s)','Hater(s)','Enemys']

def choose(word_list):
    return random.choices(word_list, k=1)[0]

#These variables randomly choose an option from the list of words
firRW = choose(first) #first random word - copy and paste this to make another word in the sentence
secRW = choose(second)
thiRW = choose(third)
forRW = choose(forth)
fifRW = choose(fifth)
print(firRW, secRW, thiRW, forRW, fifRW + '.')
