def hitung_ips():
    jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
    
    total_bobot = 0
    sks_per_mk = 3  
    total_sks = jumlah_mk * sks_per_mk  

    for i in range(jumlah_mk):
        nilai = input(f"Masukkan nilai untuk mata kuliah ke-{i+1} (A/B/C/D): ").upper()
        
        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1
        else:
            print("Nilai tidak valid! Masukkan hanya A, B, C, atau D.")
            return
        
        total_bobot += bobot * sks_per_mk  
    
    ips = total_bobot / total_sks  
    print(f"IPS yang diperoleh: {ips:.2f}")

hitung_ips()
