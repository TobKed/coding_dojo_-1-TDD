#! -*- coding: utf-8 -*-
from app import to_text


def test_0():
    assert to_text(0) == 'zero'


def test_1():
    assert to_text(1) == 'jeden'


def test_minus_1():
    assert to_text(-1) == 'minus jeden'


def test_12():
    assert to_text(12) == 'dwanaście'


def test_99():
    assert to_text(99) == 'dziewięćdziesiąt dziewięć'


def test_101():
    assert to_text(101) == 'sto jeden'


def test_200():
    assert to_text(200) == 'dwieście'


def test_520():
    assert to_text(520) == 'pięćset dwadzieścia'


def test_849():
    assert to_text(849) == 'osiemset czterdzieści dziewięć'


def test_1337():
    assert to_text(1337) == 'tysiąc trzysta trzydzieści siedem'


def test_3091():
    assert to_text(3091) == 'trzy tysiące dziewięćdziesiąt jeden'


def test_342900():
    assert to_text(342900) == 'trzysta czterdzieści dwa tysiące dziewięćset'


def test_100000():
    assert to_text(100000) == 'sto tysięcy'


def test_1000000():
    assert to_text(1000000) == 'milion'
