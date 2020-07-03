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
def get_facebook_likeit_description(names):
    if bool(names) == False:
        return ("Nikt tego nie lubi")
    elif len(names) == 1:
        return (f"{names[0]} lubi to!")
    elif len(names) == 2:
        return (f"{names[0]} i {names[1]} lubią to!")
    elif len(names) == 3:
        return (f"{names[0]}, {names[1]} i {names[2]} lubią to!")
    elif len(names) == 4:
        return (f"{names[0]}, {names[1]} i 2 inne osoby lubią to!")
    elif len(names) > 4:
        return (f"{names[0]}, {names[1]} i {len(names)-2} inne osoby lubią to!")



