# 5! = 5 * 4 * 3 * 2 * 1

# input: n
# output: n!

hasil = 1
n = int(input("Masukkan n: "))
for i in range(n, 0, -1):
    hasil = hasil * i

print(hasil)