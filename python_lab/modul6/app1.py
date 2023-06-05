data = """
in p$imava$a anu^ui 1894, t%ata ^%nd$a a f%!t int#$#!ata, ia$
^um#a ^a m%da a f%!t &%n!t#$nata d# u&id#$#a %n%$abi^u^ui $%na^d
adai$ in &i$&um!tant# &#^# mai n#%bi!nuit# !i in#xp^i&abi^#.
pub^i&u^ a af^at d#ja a&#^# d#ta^ii a^# &$im#i &a$# au i#!it ^a
iv#a^a in an&@#ta p%^iti#i; da$ mu^t# au f%!t !up$imat# &u a&#a
%&azi#, d#%a$#&# &azu^ a&uza$ii #$a atat d# &%p^#!it%$ d#
put#$ni&, in&at nu #$a n#&#!a$ !a !# p$#zint# t%at# fapt#^#. abia
a&um, ^a !fa$!itu^ a ap$%ap# z#&# ani, imi #!t# p#$mi! !a
ap$%vizi%n#z a&#^# v#$igi ^ip!a &a$# a^&atui#!& int$#gu^ ^ant
$#ma$&abi^. &$ima #$a int#$#!anta in !in#, da$ a&#^ int#$#! nu
#$a nimi& p#nt$u min# in &%mpa$ati# &u &%ntinua$#a d# n#&%n&#put,
&a$# mi-a %f#$it &#^ mai ma$# !%& !i !u$p$iza din %$i&# #v#nim#nt
din vitța m#a av#ntu$%a!a. &@ia$ !i a&um, dupa a&#!t int#$va^
^ung, mă t$#z#!& #m%ti%nat &and ma gand#!& ^a a!ta !i !imt din
n%u a&#^ p%t%p b$u!& d# bu&u$i#, uimi$# !i n#in&$#d#$# &a$# mi-a
&ufundat &u t%tu^ mint#a.
"""

decrypt_key = {
    '!': 's',
    '@': 'h',
    '#': 'e',
    '$': 'r',
    '^': 'l',
    '%': 'o',
    '&': 'c',
    '*': 'k'}


def decrypt(encrypted_text, decryption_key):
    result = ""
    for letter in encrypted_text:
        if letter in decryption_key:
            letter = decryption_key[letter]
            result += letter
        else:
            result += letter
    return result


result = decrypt(encrypted_text=data, decryption_key=decrypt_key)


def capitalize_sentence(text):
    my_list = []

    for sentence in text.split('.'):
        my_list.append(sentence.strip().capitalize())

    return '. '.join(my_list)


new_result = capitalize_sentence(result)
print(new_result)


def count_letters(text):
    short_w = []
    medium_w = []
    long_w = []
    for word in text.split():
        word = word.strip(',.;: ')  # type:str
        print(len(word))
        if len(word) <= 5:
            short_w.append(word)
        elif 5 < len(word) <= 8:
            medium_w.append(word)
        else:
            long_w.append(word)
    return (short_w, medium_w, long_w)


result = count_letters(new_result)
print('Short words: ', result[0])
print('Medium words: ', result[1])
print('Long words: ', result[2])
