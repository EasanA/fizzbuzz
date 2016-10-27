import sys

try:
    n = int(sys.argv[1])
except (IndexError,ValueError):
    while True:
         try:
            n = int(input("Please enter a number: "))
            break
         except ValueError:
            print("Please enter a number...")

print("Fizz buzz counting up to {}".format(n))
for o in range(1,n+1):
    if o % 3 == 0 and o % 5 == 0:
        print('fizzbuzz')
    elif o % 3 == 0:
        print('fizz')
    elif o % 5 == 0:
        print('buzz')
    else:
        print(o)