from zadanie1_newreq import get_facebook_likeit_description
import pytest


@pytest.mark.parametrize("n, result", [(["Piotr"], "Piotr lubi to!"), (["Piotr", "Magda"], "Piotr i Magda lubią to!"),
                                       (["Piotr", "Magda", "Janusz"], "Piotr, Magda i Janusz lubią to!"),
                                       (["Piotr", "Anna", "Janusz", "Krzysztof"], "Piotr, Anna i 2 inne osoby lubią to!"),
                                       ([], "Nikt tego nie lubi")])

def test(n, result):
    assert get_facebook_likeit_description(n) == result