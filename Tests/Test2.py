#! -*- coding: utf-8 -*-
from app import to_text

liczby = {0:"zero",
          1:"jeden",
          2:"dwa",
          3:"trzy",
          4:"cztery",
          5:"pięć",
          6:"sześć",
          7:"siedem",
          8:"osiem",
          9:"dziewięć",
          10:"dziesięć"}

def test_to_text():
    assert to_text(1) == "jeden"

def test_1_10():
    for i in range(0, 11):
        assert to_text(i) == liczby[i]

def test_20():
    assert to_text(20) == "dwadzieścia"

def test_22():
    assert to_text(22) == "dwadzieścia dwa"

def test_35():
    assert to_text(35) == "trzydzieści pięć"

def test_99():
    assert to_text(99) == "dziewięćdziesiąt dziewięć"

def test_100():
    assert to_text(100) == "sto"

def test_102():
    assert to_text(102) == "sto dwa"

def test_125():
    assert to_text(125) == "sto dwadzieścia pięć"

def test_152():
    assert to_text(152) == "sto pięćdziesiąt dwa"

def test_199():
    assert to_text(199) == "sto dziewięćdziesiąt dziewięć"
