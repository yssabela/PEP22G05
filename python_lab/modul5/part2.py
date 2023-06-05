# binary chars

# 10 = 0000 1010  in binar
# 10 = 0    A    in hexazecimale
# 10 = 0    12   in octal
# cate valori pot fi stocate in 4 biti?? 16= adica 2 la a 4-a

# un nr obtinut de la un caracter:
# a_number = ord ('a')
# A_number = ord ('A')
# # de definit in biti
# # in primul rand trebuie sa ii dam o lungime , alegem o lung. de 8
#
# print(bin(A_number))
# print(bin(a_number))
# print(max('abcd')) # acesta este mai mare decat cel de jos
# print(max('AabvdZ'))
#
# letter1 = chr(70)
# letter2 = chr(39)
# print(letter1, letter2)
#
# print(10 ^ 10)
# # 0000 1010 ^ 0000 1010 = 0000 0000
# rezultatul este 0 cand sunt identici si 1 cand sunt diferiti
#
# print('10 xor^ 10', 10 ^ 10)
# # 0000 1000 ^ 0000 1010 = 0000 0010
#
# print('10 xor^ 25', (10 ^ 25)^25)  # tot 10


my_message = 'This is my message '
encrypted_result = ''
for letter in my_message:
    # se tranf fiecare litera intr-un nr:
    #print(ord(letter))
    # se face xor ^ 48:
    #print(ord(letter)^48)
    # se transf inapoi in litere:
    #print(chr(ord(letter) ^ 48))
    encrypted_result += chr(ord(letter) ^ 48)
print(encrypted_result)

# 48 este cheia de criptare

decrypted_result = ''
for letter in encrypted_result:
    decrypted_result += chr(ord(letter)^ 48)
print(decrypted_result)