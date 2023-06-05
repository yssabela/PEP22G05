nume = input("Introduceti numele:")
str_note = input("Introduceti notele elevului separate prin virgula:")
str_note = str_note.replace(" ", "")
assert str_note, "Nu ai dat nicio nota!"
note = str_note.split(",")
lista_note = []
for nota in note:
    try:
        lista_note.append(int(nota))
    except ValueError:
        print("introduceti note 1-10!")
print(lista_note)
media = sum(lista_note) / len(lista_note)
print("media = ", media)
if media >= 5:
    print(f"{nume} a trecut clasa!")
else:
    print(f"{nume} nu a trecut clasa!")
