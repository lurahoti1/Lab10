shuma = 0.0

while True:
    hyrje = input("Vlera: ")
    if hyrje.lower() == "stop":
        break
    try:
        numri = float(hyrje)
        shuma += numri
    except ValueError:
        print("Vlerë e pavlefshme")
        continue

print(f"Shuma: {shuma:.2f}")
