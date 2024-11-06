def smallest_value(a,b,c):
    if (a > b) or (a > c):
        if b < c:
            return b
        else:
            return c
    
    return a

def main():
    x = smallest_value(10,2,3)
    print(x)

main()
