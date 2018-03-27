#! -*- coding: utf-8 -*-

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
          10:"dziesięć",
          11:"jedenaście",
          12:"dwanaście",
          13:"trzynaście",
          14:"czternaście",
          15:"piętnaście",
          16:"szesnaście",
          17:"siedemnaście",
          18:"osiemnaście",
          19:"dziewiętnaście",
          20:"dwadzieścia",
          30:"trzydzieści",
          40:"czterdzieści",
          90:"dziewięćdziesiąt",
          100:"sto",
          200:"dwieście",
          300: "trzysta"}


def give_1_99(i, nums):
    base = ""
    space = ""
    if i <= 19:
        base = nums.get(i)
    else:
        tens, ones = divmod(i%100, 10)
        if i > 99 and (tens is not 0 or ones is not 0):
            base += " "
        if tens is 0:
            tens = ""
        elif tens < 5:
            tens = nums.get(tens * 10)
        else:
            tens = nums.get(tens) + "dziesiąt"
        if ones is 0:
            ones = ""
        else:
            ones = liczby.get(ones)
        if tens and ones:
            space = " "
        base += tens + space + ones
    return base


def give_100_999(i, nums):
    if i < 100:
        return ""
    if i is 100:
        return nums.get(100)
    if i is 200:
        return nums.get(200)
    hundreds = i // 100
    hundreds = int(str(hundreds)[-1])
    if hundreds is 0:
        return ""
    elif hundreds is 1:
        return nums.get(hundreds*100)
    elif hundreds is 2:
        return nums.get(hundreds*100)
    elif hundreds < 5:
        return nums.get(hundreds) + "sta"
    else:
        return nums.get(hundreds) + "set"


def to_text(i, nums=None):
    if nums is None:
        nums = liczby
    base = ""
    if i == 0:
        return nums.get(i)

    if i < 0:
        base = "minus "
        i = abs(i)

    # 100-999
    base += give_100_999(i, nums)

    # 1 - 99
    base += give_1_99(i, nums)

    return base
