import cmath

a = float(input("type in your first coefficient: "))
b = float(input("type in your second coefficient: "))
c = float(input("type in your third coefficient: "))

if a != 0:
    d = float((b ** 2))
    e = float((4 * a * c))
    f = float((2 * a))
    g = float((-1 * b))

    ans1 = (complex(((g + cmath.sqrt(d - e)) / f)))
    ans2 = (complex(((g - cmath.sqrt(d - e)) / f)))

    print(ans1, ans2)

elif b != 0:
    ans3 = ((-1 * c) / b)
    print(ans3)

else:
    print(c)
