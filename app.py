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
          1000:"tysiąc",
          1000000:"milion"}


def give_1_99(i, nums):
    base = ""
    space = ""
    tens = int(str(i).zfill(2)[-2:])
    if 0 < tens <= 19:
        # if i > 99:
        #     base += " "
        base += nums.get(tens)
    else:
        tens, ones = divmod(tens, 10)
        # if i > 99 and (tens is not 0 or ones is not 0):
        #     base += " "
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
    base = ""
    if i < 100:
        return base
    if i is 100:
        base += nums.get(100)
    elif i is 200:
        base += nums.get(200)
    else:
        hundreds = i // 100
        hundreds = int(str(hundreds)[-1])
        if hundreds is 0:
            return ""
        elif hundreds is 1:
            base += nums.get(hundreds*100)
        elif hundreds is 2:
            base += nums.get(hundreds*100)
        elif hundreds < 5:
            base += nums.get(hundreds) + "sta"
        else:
            base += nums.get(hundreds) + "set"
    if int(str(i).zfill(2)[-2:]) > 0:
        base += " "
    return base


def give_1000_999000(i, nums):
    base = ""
    if i < 1000:
        return base

    thousands = i // 1000
    thousands = int(str(thousands).zfill(3)[-3:])
    if thousands is 0:
        return base
    if thousands is 1:
        base += "tysiąc"
    else:
        ending = "tysięcy"
        if int(str(thousands).zfill(3)[-1]) in [2, 3, 4]:
            ending = "tysiące"
        base += "{}{} {}".format(give_100_999(thousands, nums), give_1_99(thousands, nums), ending)

    if i > 999:
        if int(str(i).zfill(3)[-3:]) > 0:
            base += " "
    return base


def give_1000000(i, nums):
    base = ""
    milions, rest = divmod(i, 1000000)
    if milions is 1:
        base += nums.get(1000000)
    if milions and rest:
        base += " "
    return base


def to_text(i, nums=None):
    if nums is None:
        nums = liczby
    base = ""
    if i == 0:
        return nums.get(i)

    if i < 0:
        base = "minus "
        i = abs(i)

    # 1000000
    base += give_1000000(i, nums)

    # 1000-999000
    base += give_1000_999000(i, nums)

    # 100-999
    base += give_100_999(i, nums)

    # 1 - 99
    base += give_1_99(i, nums)

    return base
