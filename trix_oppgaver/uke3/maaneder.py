months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

a = int(input("Enter a number for to choose a month: "))

if (a>12) or (a<1):
    exit("Please enter a valid number.")

a = a-1

print(months[a])