for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print(f"{x}, fizzbuzz")
    elif x % 3 == 0:
        print(f"{x}, fizz")
    elif x % 5 == 0:
        print(f"{x}, buzz")
    else:
        print(x)