# TUGAS ANALISA ALGORITMA
# KELOMPOK 6 :
# 1. Gilang Wahyu Ramadhan
# 2. Faridz Panjasela Ramadani
# 3. Riski Nurhadi 
# 4. Yuan MAulana

# <<---------- DATA PEGAWAI ------------->>
pegawai = [
    {'nip': '101', 'nama': 'Andi', 'bagian': 'Direktur Perusahaan',},
    {'nip': '102', 'nama': 'Budi', 'bagian': 'Sekertaris',},
    {'nip': '103', 'nama': 'Wiro', 'bagian': 'Bendahara',},
    {'nip': '104', 'nama': 'Suparno', 'bagian': 'Staf Marketing',},
    {'nip': '105', 'nama': 'Bejo', 'bagian': 'Staf Marketing',},
    {'nip': '106', 'nama': 'Dahlan', 'bagian': 'Staf Marketing',},
    {'nip': '107', 'nama': 'Faridz', 'bagian': 'Staf Pelayanan',},
    {'nip': '108', 'nama': 'Zaky', 'bagian': 'Staf Pelayanan',},
    {'nip': '109', 'nama': 'Jayen', 'bagian': 'Staf Pelayanan',},
    {'nip': '110', 'nama': 'Deni', 'bagian': 'Staf Admin',},
    {'nip': '111', 'nama': 'Wahyu', 'bagian': 'Staf Admin',},
    {'nip': '112', 'nama': 'Sinta', 'bagian': 'Staf Admin',},
    {'nip': '113', 'nama': 'Amel', 'bagian': 'Pengelola Media Sosial',},
    {'nip': '114', 'nama': 'Rara', 'bagian': 'Pengelola Media Sosial',},
    {'nip': '115', 'nama': 'Cintya', 'bagian': 'Costomer Service',},
    {'nip': '116', 'nama': 'Putri', 'bagian': 'Costomer Service',},
    {'nip': '117', 'nama': 'Saepul', 'bagian': 'Costomer Service',},
    {'nip': '118', 'nama': 'Anwar', 'bagian': 'Cleaning Service',},
    {'nip': '119', 'nama': 'Mawar', 'bagian': 'Cleaning Service',},
    {'nip': '120', 'nama': 'Cici', 'bagian': 'Cleaning Service',}
]

def cari_pegawai(nip=None, nama=None):
    hasil_pencarian = []
    for pgw in pegawai:
        if nip and pgw['nip'] == nip:
            hasil_pencarian.append(pgw)
        elif nama and pgw['nama'].lower() == nama.lower():
            hasil_pencarian.append(pgw)
    return hasil_pencarian

print("Selamat Datang Di PT. Muba Electric Power")
print("Cari Data Pegawai berdasarkan Menu")
print("========== Menu ============")
print("1: Cari Pegawai Berdasarkan NIP")
print("2: Cari Pegawai Berdasarkan Nama")

pilihan = input("Masukkan Pilihan:")
if pilihan.lower() == "1":
    nip = input("Masukkan nip pegawai yang ingin dicari: ")
    hasil_pencarian = cari_pegawai(nip=nip)

    print("=========== Hasil ============")
    
    if hasil_pencarian:
        print("pegawai dengan nip", nip, "ditemukan:")
        for pgw in hasil_pencarian:
            print("nip    :", pgw['nip'])
            print("nama   :", pgw['nama'])
            print("bagian :", pgw['bagian'])
        print("========== Terimakasih ========")   
    else:
        print("pegawai dengan nip", nip, "tidak ditemukan.")
        print("========== Terimakasih ========") 


        
elif pilihan.lower() == "2":
    nama = input("Masukkan nama pegawai yang ingin dicari: ")
    hasil_pencarian = cari_pegawai(nama=nama)
    print("=========== Hasil ============")
    if hasil_pencarian:
        print("pegawai dengan nama", nama, "ditemukan:")
        for pgw in hasil_pencarian:
            print("nip    :", pgw['nip'])
            print("nama   :", pgw['nama'])
            print("bagian :", pgw['bagian'])
        print("========== Terimakasih ========")    
    else:
        print("pegawai dengan nama", nama, "tidak ditemukan.")
        print("========== Terimakasih ========") 
else:
    print("Pilihan tidak valid.")

# <<---------- Selesai ----------->