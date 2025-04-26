# "()"

# def check(s) :
#   op = "({[<"
#   oc = ")}]>"
#   s = s.strip()

#   for l in s :
#     if l in oc :
#       return False
#     else :
#       if l in op :
#         if oc[op.index(l)] in s : return True
#         else: return False


def check(_str):
    s = list(_str)
    o = list("({[<")
    c = list(")}]>")
    res = []
    for l, e in zip(o, c):
        if (l and e) in s:
            if s.count(l) == s.count(e) and s.index(l) < s.index(e):
                res.append(1)
            else:
                res.append(0)
    return all(res)


print(check(""))
