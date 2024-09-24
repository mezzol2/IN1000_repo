def primes(n):

    if n == 2:
        return [1]
    
    list1 = [1,2]

    for x in range(2, n):
        prime_status = True
        for prime in list1[1:]:
            if x % prime == 0:
                prime_status = False
                break
        if prime_status == True:
            list1.append(x)


    return list1

print(primes(38))