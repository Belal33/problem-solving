def digital_root(n):
    return n % 9 or (n and 9)


# def digital_root(n):
#     """
#     Given n, take the sum of the digits of n.
#     If that valu has more than one digit,
#     continue reducing in this way until a single-digit number is produced.
#     The input will be a non-negative integer.
#     """

#     str_n = str(n)
#     if len(str_n) > 1:
#         n = 0
#         for e in str_n:
#             n += int(e)
#         if n < 10:
#             return n
#         else:
#             return digital_root(n)

#     else:
#         return n


print(digital_root(104515650))
