s = input("Enter a string : ")
l = len(s)
l_ = int(l / 2)
a = s[:l_]
if l % 2 == 0:
    b = s[l_:]
else:
    b = s[l_ + 1:]


def s_sort(var):
    t = list(var)
    t.sort()
    return t


a_list = s_sort(a)
b_list = s_sort(b)

a_str, b_str = "", ""
for i in a_list:
    a_str += i
for i in b_list:
    b_str += i

if a_str == b_str:
    print(f"{s} is Lapindrome.")
else:
    print(f"{s} is not a Lapindrome.")
