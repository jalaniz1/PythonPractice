__author__ = 'James'


def first_half(str):
    length = len(str)
    if length > 0:
        length = (int)(length/2)  # Truncate
    return str[0:length]


str = first_half('Helloaaa')
print(str)