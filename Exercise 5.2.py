def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def prompting():
    a = input("Type your value of a: ")
    b = input("Type your value of b: ")
    c = input("Type your value of c: ")
    n = input("Type your value of n: ")

    check_fermat(int(a), int(b), int(c), int(n))


prompting()