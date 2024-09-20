def double_it(number):
    number *=2
    return number

def test_length(string, number):
    if len(string) == number:
        return True
    else:
        return False

def count_length(number):
    n = len(str(number))
    return n

print(double_it(12))
print(test_length('qwe', 4))
print(count_length(987234))