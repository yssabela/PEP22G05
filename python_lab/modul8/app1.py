# create generator for letters a to z:
# generator de la a->z

# def my_generator(start_letter, end_letter):
#     for i in range(ord(start_letter), ord(end_letter)+1):
#         yield chr(i)
#
#
# for letter in my_generator("a","z"):
#    print(letter)
#
letter_generator = (chr(i) for i in range(ord('a'), ord('z')+1))

for i in letter_generator:
    print("Letter v1:", i)