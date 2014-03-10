__author__ = 'James'


def string_match(a, b):
    ""
    if a is None or b is None:
        return 0

    c = 0
    index = 0

    while index < len(a)-1 and index < len(b)-1:
        print (index)
        if (a[index]+a[index+1]) == (b[index]+b[index+1]):
            c += 1
        index += 1


    return c


ret = string_match('xxcaazz','xxbaazz')

print ('%d'%ret)