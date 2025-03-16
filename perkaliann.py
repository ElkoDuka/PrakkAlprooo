def perkalian(a, b):
    hasil = 0
    for _ in range(a):
        hasil += b
        print(b, end=" + " if _ < a - 1 else " = ")  # Menampilkan proses penjumlahan
    print(hasil)  # Menampilkan hasil akhir
    return hasil

# Contoh penggunaan
perkalian(6, 5)  # Output: 5 + 5 + 5 + 5 + 5 + 5 = 30
perkalian(7, 10) # Output: 10 + 10 + 10 + 10 + 10 + 10 + 10 = 70
