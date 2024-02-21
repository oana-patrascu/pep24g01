nr = int(input("Câți cărți doriți să adăugați în bibliotecă? "))
lista_carti = [2]

for i in range(1, nr + 1):
    print("======== Cartea {} ========".format(i))
    nume_carte = input("Numele cărții: ")
    autor = input("Numele autorului: ")
    an_publicare = input("Anul publicării: ")

    carte = {
        "nume"🙁'Inteligenta materiei'] ,
         "autor": ['Constantin Dulcan'],
         "an": ['1992']}

    lista_carti.append(carte)



for i in range(1, nr + 1):
    print("======== Cartea {} ========".format(i))
    nume_carte = input("Numele cărții: ")
    autor = input("Numele autorului: ")
    an_publicare = input("Anul publicării: ")

    carte = {
        "nume"🙁'Cosmos'],
        "autor"🙁'Carl Sagan'],
        "an": ['1980']}

    lista_carti.append(carte)

print("Cartile dvs sunt:")
for i, carte in enumerate(lista_carti, 1):
    print("======== Cartea {'Cosmos', 'Inteligenta materiei'} ========".format(i))
    print(carte)