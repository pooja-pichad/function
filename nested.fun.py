def f1():
    s=int(input("enter a number"))
    if s%2==0:
        def f2():
            print("even",s)
    else:
        print("odd",s)

    # s=int(input("enter a number"))

    f2()
f1()

