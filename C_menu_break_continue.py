while True:
    print("\nMenu:")
    print("1) Pershendetje")
    print("2) Katerkendeshi: perimeteri")
    print("3) Ndihme")
    print("0) Dalje")
    zgjedhja = input("Zgjedhja: ")

    if zgjedhja == "1":
        print("Përshëndetje! Mirë se erdhe.")
        continue
    elif zgjedhja == "2":
        try:
            a = float(input("a= "))
            b = float(input("b= "))
            P = 2 * (a + b)
            print(f"Perimetri: {P:.2f}")
        except ValueError:
            print("Vlera të pavlefshme për a ose b.")
        continue
    elif zgjedhja == "3":
        print("Zgjidh 1 për përshëndetje, 2 për llogaritje, 0 për dalje.")
        continue
    elif zgjedhja == "0":
        print("Dalje nga menuja.")
        break
    else:
        print("Zgjedhje e pavlefshme.")
        continue
