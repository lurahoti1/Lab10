FJALEKALIMI = "tik12"
tentativa = 3

while tentativa > 0:
    hyrje = input("Fjalekalimi: ")
    if hyrje == FJALEKALIMI:
        print("Hyrje OK")
        break
    else:
        tentativa -= 1
        if tentativa > 0:
            print(f"Gabim. Tentativa te mbetura: {tentativa}")
        else:
            print("Gabim. Nuk ka me tentativa.")
