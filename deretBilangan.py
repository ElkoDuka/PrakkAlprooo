def ganjil(bawah, atas):
    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 == 1:
                print(i, end=", ")
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 == 1:
                print(i, end=", ")

print("Hasil untuk batas bawah = 10, batas atas = 30:")
ganjil(10, 30)  
print("\nHasil untuk batas bawah = 97, batas atas = 82:")
ganjil(97, 82)  
