temp = float(input("What is the person's body temperature? "))

if temp > 37.5:
    print(f"{temp} is too hot! Put out that fire!")
elif temp < 36.5:
    print(f"{temp} is a tad chilly.  Give that man a blanket.")
else:
    print(f"{temp} is safe, but give them a hug.")
    print("We all just need a hug somtimes.")