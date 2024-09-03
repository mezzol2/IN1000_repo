tall1 = 15.7
tall2 = 9.4
sum1 = tall1 + tall2
tall3 = 37
tall4 = 11
sum2 = tall3 + tall4
setning = "Den største summen er: "

if sum1 > sum2:
    print(f'{setning}{sum1}')
elif sum1 < sum2:
    print(f'{setning}{sum2}')
else:
    print(f"Sumene er like: {sum1}")

