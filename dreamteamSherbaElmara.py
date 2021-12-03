# # #                                   # 1
# # # import random as rd
# # # random_number = rd.randint(0,10)
# # #
# # # i = 1
# # # while i <= 3:
# # #     user = int(input('Find the number which choose computer (0,10):  '))
# # #     if user == random_number:
# # #         print('Вы угадали с %d-й попытки' % i)
# # #
# # #     i += 1
# # # else:
# # #         print('Вы исчерпали 3 попыток. Было загадано', random_number)
# # #                                      # 2
# # # while True:
# # #     symbol = int(input())
# # #     if symbol == 0:
# # #         break
# # #     print(chr(symbol))
# # #
# # #                                       # 3
# # #
# # # s = input()
# # # if len(s) > 10:
# # #     print("WARNING!")
# # # else :
# # #     for i in range (len(s),10):
# # #         s += "*"
# # #         print(s)
# # #
# # #                                          # 4
# # #
# # # lst = []
# # #
# # # for i in range(6):
# # #     lst.append(float(input("Введите вещественные числа: ")))
# # #
# # # maximus = lst[0]
# # # minimus = lst[0]
# # #
# # # for i in lst:
# # #     if maximus > i:
# # #         maximus = i
# # #     else:
# # #         minimus = i
# # #
# # # print(f"Max: {round(maximus, 2)} | Min: {round(minimus, 2)}")
# # #
# # #                                    # 5
# # #
# # # c = int(input())
# # # b = [int(a) for a in str(c)]
# # # print(max(b), min(b))
# # #
# # #                                       #6
# # texx = """
# # The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
# # Simple is better than complex.Complex is better than complicated.
# # Flat is better than nested.Sparse is better than dense.
# # Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
# # Errors should never pass silently.Unless explicitly silenced.
# # In the face of ambiguity, refuse the temptation to guess.
# # There should be one--and preferably only one --obvious way to do it.
# # Although that way may not be obvious at first unless you're Dutch.
# # Now is better than never.
# # Although never is often better than *right* now.
# # If the implementation is hard to explain, it's a bad idea.
# # If the implementation is easy to explain, it may be a good idea.
# # Namespaces are one honking great idea --let's do more of those!
# # """
# # up_text = ''
# # a = texx.split()
# # for i in a:
# #     for ii in i:
# #         if ii == ii.upper() and ii not in [',', '.', '-', "'", '*']:
# #             up_text += ii
# # print(up_text)
# #
# # #                                         #7
# # text = """
# # The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
# # Simple is better than complex.Complex is better than complicated.
# # Flat is better than nested.Sparse is better than dense.
# # Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
# # Errors should never pass silently.Unless explicitly silenced.
# # In the face of ambiguity, refuse the temptation to guess.
# # There should be one--and preferably only one --obvious way to do it.
# # Although that way may not be obvious at first unless you're Dutch.
# # Now is better than never.
# # Although never is often better than *right* now.
# # If the implementation is hard to explain, it's a bad idea.
# # If the implementation is easy to explain, it may be a good idea.
# # Namespaces are one honking great idea --let's do more of those!
# # """
# # # lst = []
# # # a = text.index('s')
# # # lst.append(a)
# # # print(lst)
# # #
# #                                   # 13
# # def divide(array):
# #     positive = []
# #     negative = []
# #     for i in array:
# #         if i > 0:
# #             positive.append(i)
# #         elif i < 0:
# #             negative.append(i)
# #     return positive, negative
# #
# #
# # arr = [1, 2, 3, -1, -2, -3]
# # pos, neg = divide(arr)
# # print(pos)
# # print(neg)
# #                                   14
# seasons = {'Winter': (1, 2, 12),
#           'Spring': (3, 4, 5),
#           'Summer': (6, 7, 8),
#           'Autumn': (9, 10, 11)}
#
# month = int(input('Choose a month: '))
# for key in seasons.keys():
#     if month in seasons[key]:
#         print(key)
#
# #                                   15
# n = int(input())
# m = int(input())
# y = int(input())
#
# def bank(n,m,y):
#     n = 'nal'
#     y = 'year'
#     def money():
#         if year > 0:
#             nal = n * 1.1 + m
#             year = year -1
#             return money()
#         else:
#             return nal
#
# print (n)
# #                       16
# a = 0
# days = -1
# summ = 0
# while a > -300:
#     summ += a
#     days += 1
#     a = float(input())
# print(summ / days )