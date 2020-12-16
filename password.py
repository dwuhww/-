def is_eight():
    passwd = input("please input your password:")
    if len(passwd) >= 8:
        return passwd
    else:
        print("invalid password")
        return 0


def is_number_char(str1):
    number = 0
    for i in str1:
        if (i in "1234567890") or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<122):
            number += 1
    if number == len(str1):
        return str1
    else:
        print("invalid number")
        return 0




def is_two_number(str1):
    number = 0
    for i in str1:
        if i in "1234567890":
            number += 1
    if number >= 2:
        print("valid number")
    else:
        print("invalid password")


first = is_eight()
if first != 0:
    second = is_number_char(first)
    if second != 0:
        is_two_number(second)


