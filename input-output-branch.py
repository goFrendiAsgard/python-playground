a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
operasi = input("Masukkan operasi (+/-/*): ")
if operasi == "+":
    print(a + b)
elif operasi == "-":
    print(a - b)
elif operasi == "*":
    print(a * b)
else:
    print("operasi tidak dikenali")

