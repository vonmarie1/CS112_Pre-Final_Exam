def prime(x, y):
    z = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                z.append(i)
    return z


while True:
    start = int(input("Enter a number [start]: "))
    end = int(input("Enter a number [end]: "))

    if start < 0 or end < 0 or start > end or start == 0:
        print(
            "Enter a non-negative number.")
    else:
        break


pl = prime(start, end)
if len(pl) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers between ", start, "and", end, ": ", pl)
