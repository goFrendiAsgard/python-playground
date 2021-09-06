def get_luas(p: float, l: float) -> float:
    return p * l

panjang = float(input("Masukkan panjang "))
lebar = float(input("Masukkan lebar "))

luas = get_luas(panjang, lebar)

# print("luas = " + str(luas))
print(f"luas = {luas}")
