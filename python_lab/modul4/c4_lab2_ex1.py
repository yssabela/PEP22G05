def sondaj():
    varste_participanti = []
    nr_part = int(input('Cati participanti avem la sondaj?'))
    for nr in range(1,nr_part + 1):
        try:
            var_part = int(input(f'introduceti varsta paticipantului,{nr}'))
        except ValueError:
            print('valoare introdusa este incorecta')
            var_part = int(input(f'introduceti varsta paticipantului,{nr}'))
        varste_participanti.append(var_part)
    print('media de varsta este:', sum(varste_participanti)/len(varste_participanti))
sondaj()

