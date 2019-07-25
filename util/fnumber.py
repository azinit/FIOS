"""
..............................................................................................................
................................................ METHODS SUMMARY ......................................................
..............................................................................................................
"""

def extract(expression: str):
    import re
    return re.findall(r'\d+', expression)


# def digits_by_pow(digits, parser, pow_=1):
#     try:
#         if not isinstance(digits, (list, str)):
#             digits = [digits]
#         for j, i in enumerate(digits):
#             if str(i).isdigit():
#                 i = int(i)
#                 if i < 10**(pow_-1):
#                     digits[j] = (pow_ - len(str(i))) * '0' + str(i)
#     except():
#         pass
#     return [parser(x) for x in digits]


# def digits_set(digit_seq):
#     count_list = [0] * 10
#     for e in digit_seq:
#         if str(e).isdigit():
#             count_list[int(e)] += 1
#     return count_list

"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    def __test__extract():
        print(":::::::::::::::::::::extract:::::::::::::::::::::")
        sub = 'defin123ition4_1.txt'
        sub1 = 'definition1.txt'
        sub2 = 'defini1tion1.txt'
        print(extract(sub))
        print(extract(sub1))
        print(extract(sub2))

    __test__extract()

    # print(digits_by_pow(digits=['1', '0002', '3', 'abs', 12.3, '04', '25', '23', '04', '107'], pow_=5, parser=str))
    # print(digits_by_pow(digits=1, pow_=2, parser=str))

    # print(digit(digit_seq="12349501"))