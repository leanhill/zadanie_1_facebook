from zadanie1_newreq import get_facebook_likeit_description


def test():
    assert get_facebook_likeit_description(["Piotr"]) == "Piotr lubi to!"
    assert get_facebook_likeit_description(["Piotr", "Magda"]) == "Piotr i Magda lubią to!"
    assert get_facebook_likeit_description(["Piotr", "Magda", "Janusz"]) == "Piotr, Magda i Janusz lubią to!"
    assert get_facebook_likeit_description(["Piotr", "Magda", "Janusz", "Krzysztof"]) == "Piotr, Magda i 2 " \
                                                                                         "inne osoby lubią to!"
    assert get_facebook_likeit_description([]) == "Nikt tego nie lubi"
