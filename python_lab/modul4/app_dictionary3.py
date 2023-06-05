dictionary = {'cat':'chat', 'dog':'chien','horse':'cheval'}
words = ['cat','lion','horse']

for word in words:
    if word in dictionary:
        print(word,'->',dictionary[word])
    else:
        print(word,'is not in dictionary')

# or

for key in sorted(dictionary.keys()):
    print(key,'->',dictionary[key])

for english, french in dictionary.items():
    print(french,'->',english)

for french in dictionary.values():
    print(french)

######
dictionary = {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval'}
dictionary['cat'] = 'minou'
dictionary['dog'] = 'minionet'
dictionary['eyes'] = 'eyex'
dictionary.pop('dog')
dictionary.update({'mouth':'gouche'})
del dictionary['eyes']
print(dictionary)
