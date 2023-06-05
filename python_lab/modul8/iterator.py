# building my own iterator

# class Sentence:
#     def __init__(self,sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.word = self.sentence.split()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.word):
#             raise StopIteration
#         index = self.index
#         self.index += 1
#         return self.word[index]
#
#
# my_sentence = Sentence('This is a test')
#
# for words in my_sentence:
#     print(words)


 #### building my own generator


class Sentence:
    def __init__(self,sentence):           # definim constructorul
        self.sentence = sentence
        self.index = 0                     # iteratorul este un obiect cu stare si ii atribuim 0
        self.word = self.sentence.split()  # vrem ca stringul sa fie splituit

    def __iter__(self):     # am definit functia pt  iterabil
        return self         # am apelat functia in felul acesta pt ca iter returneaza obiectul in sine

    def __next__(self):                   # aplicam metoda next pe iterabilul nostru
        if self.index >= len(self.word):  # definim o variabila care sa itereze prin string
            raise StopIteration           # daca se indeplineste conditia raise exceptia
        index = self.index        # daca nu indeplineste conditia => vrem sa ne dea cuvintele
        self.index += 1           # incrementam index
        return self.word[index]   # vrem sa ne returneze cuvintele de la indexul 0

def sentence(sentence):            # am creat un generator
    for word in sentence.split():  # am parcurs prin sentinta
        yield word                 # returneaza cuvintele separat

# my_sentence = Sentence('This is a test')   # apelam clasa
my_sentence = sentence('This is a test')     # apelam generatorul
#
# for words in my_sentence:   # a doua metoda de a returna cuvintele fara sa printam next
#     print(words)

print(next(my_sentence))      # prima metoda de a returna cuvintele pe rand
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))


################################################################

class IterableClass:
    def __init__(self):
        self.list = [1, 2, 3, 4, 5]
        print(self.list)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index == len(self.list) - 1:
            raise StopIteration
        self.index += 1
        return self.list[self.index]

    def __getitem__(self, key):
        return self.list[key]


c = IterableClass()

for i in c:
    print (i)

print(c[0:2])

#############################################################
# generator

def sentence(sentence):
    for word in sentence.split():
        yield word

my_sentence = sentence('This is a test')  # apelam generatorul

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))



