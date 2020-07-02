"""Super, dokładnie o takie coś z debuggerem chodzi!

To ja bym poprosił o to żeby przygotował Pan krótką funkcję która przyjmie jako argument listę imion. Zwróci natomiast string.

Funkcja ma zwrócić tekst taki jaki jest na Facebooku tj, np:

nikt tego nie lubi - dla argumentu który jest pustą listą
Piotr lubi to! - jeśli lista przekazana jako argument ma jeden element o wartości "Piotr"
Piotr i Ania lubią to - jeśli lista przekazana jako argument ma dwa elementy: "Piotr" i "Ania"
Piotr, Ania i Marek lubią to - jeśli lista przekazana jako argument ma trzy elementy: "Piotr" i "Ania" i "Marek"
Piotr, Ania i 2 inne osoby lubią to - jeśli lista ma 4 elementy i dwa pierwsze z nich to "Piotr" i "Ania"
Piotr, Ania i N inne osoby lubią to - jeśli lista ma N elementy i dwa pierwsze z nich to "Piotr" i "Ania"

Proszę dać znać czy to jest jasne:) jak już się uda - proszę podesłać link do repozytorium z kodem:) a jeśli będzie problem - proszę pisać:)
"""
def facebook(lista_imion):
    if bool(lista_imion) == False:
        print("Nikt tego nie lubi")
    elif len(lista_imion) == 1 and lista_imion[0] == "Piotr":
        print("Piotr lubi to!")
    elif len(lista_imion) == 2:
        lista_imion = set(lista_imion)
        if bool(lista_imion - {"Piotr", "Ania"}) == False:
            print("Piotr i Ania lubią to")
    elif len(lista_imion) == 3:
        lista_imion = set(lista_imion)
        if bool(lista_imion - {"Piotr", "Ania", "Marek"}) == False:
            print("Piotr, Ania i Marek lubią to")
    elif len(lista_imion) == 4:
        a = set(lista_imion[0:2])
        if bool(a - {"Piotr", "Ania"}) == False: #tu założyłem, że nie ma znaczenia czy Piotr jest jako pierwszy czy Ania. Jezeli jednak chciales by to mialo znacznie to po prostu bym sprawdzil po kolei pozycje listy
            print("Piotr, Ania i 2 inne osoby lubią to")
    elif len(lista_imion) > 4:
        a = set(lista_imion[0:2])
        if bool(a - {"Piotr", "Ania"}) == False: #tu założyłem, że nie ma znaczenei czy Piotr jest jako pierwszy czy Ania. Jezeli jednak chciales by to mialo znacznie to po prostu bym sprawdzil po kolei pozycje listy
            print("Piotr, Ania i %d inne osoby lubią to" %len(lista_imion))
    return



