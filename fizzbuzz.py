for num in range(1, 11):
    if num & 3 == 0:
        print("Fizz")
    elif num & 5 == 0:
        print("Buzz")
    else:
        print(num)