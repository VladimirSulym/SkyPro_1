# dic = {
#     1: 'da',
#     0: 'net',
# }
#
# print(dic[4 > 2])
#
# text = ['ноль', 'one']
#
# print(text[3 > 2])
#
# for a, b in dic.items():
#     print(a, end=' ')
#     print(b)
#
# print(dic)


def func_with_param(a, b=3):
    print(f'{a} and {b}')


func_with_param(b=2, a=1)
