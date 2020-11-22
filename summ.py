def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return (one + delimiter + two).upper()

print(get_summ('Learn', 'python'))