import json
daftar_buku = []

def menu() :
    nama_file = "perpustakaan.json"
    muat_dari_json(nama_file)

    while True :
        try :
            print("="*10, "INVENTORY PERPUSTAKAAN", "="*10)
            print("1. Tambah Buku\n2. Tampilkan semua buku\n3. Hapus buku\n4. Simpan buku\n5. Keluar")
            pilih = int(input("Masukan (1-5) : "))

            if pilih == 1 :
                print("\nTAMBAHKAN BUKU")
                judul = input("Masukan judul : ")
                penulis = input("Masukan penulis : ")
                tahun_terbit = input("Masukan tahun terbit : ")
                jumlah_halaman = input("Masukan jumlah halaman : ")
                tambah_buku(judul, penulis, tahun_terbit, jumlah_halaman)


            elif pilih == 2 :
                tampilkan_buku()

            elif pilih == 3 :
                judul = input("Masukan judul yang ingin dihapus : ")
                hapus_buku(judul)

            elif pilih == 4 :
                simpan_buku(nama_file)
                

            elif pilih == 5 :
                print("TERIMAKASIH!!!")
                break

            pilih_2 = input("Apakah anda ingin mengulangi lagi? (y/n) : ")
            if pilih_2.lower() == 'n' :
                print("BYEEE")
                break

        except ValueError : print("Input harus angka!!!")

def tambah_buku(judul, penulis, tahun_terbit, jumlah_halaman) :
    if not judul.strip() or not penulis.strip() or not tahun_terbit.strip() or not jumlah_halaman.strip() :
        print("Input tidak boleh kosong")
        return
    
    if not tahun_terbit.isdigit() or not jumlah_halaman.isdigit() or len(jumlah_halaman) > 4 :
        print("Tahun atau jumlah halaman harus angka!!! dan jumlah halaman kurang dari 4 digit!!!")
        return
    
    buku = {'judul' : judul, 'penulis' : penulis, 'tahun terbit' : tahun_terbit, 'jumlah halaman' : jumlah_halaman}
    daftar_buku.append(buku)
    print(f"Buku {buku['judul']} berhasil ditambahkan!!!")

def tampilkan_buku() :
    if not daftar_buku :
        print("Data buku kosong")
        return
    
    print("-"*10,"DATA BUKU", "-"*10)
    for i, buku in enumerate(daftar_buku,  1) :
        print(f"Buku ke {i}")
        print(f"Judul : {buku['judul']}")
        print(f"Penulis : {buku['penulis']}")
        print(f"Tahun terbit : {buku['tahun terbit']}")
        print(f"Jumlah halaman : {buku['jumlah halaman']}")    
        print("\n")

def hapus_buku(judul) :
  global daftar_buku
  judul = judul.strip()
  awal = len(daftar_buku)
  daftar_buku = [k for k in daftar_buku if k["judul"].lower() != judul.lower()]
  if len(daftar_buku) < awal:
      print(f"Buku dengan judul '{judul}' berhasil dihapus.")
  else:
      print(f"Buku dengan judul '{judul}' tidak ditemukan.")

def simpan_buku(nama_file) :
    try:
        with open(nama_file, "w") as file:
            json.dump(daftar_buku, file, indent=4)
        print(f"Data berhasil disimpan ke '{nama_file}'")
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")

def muat_dari_json(nama_file):
    global daftar_buku
    try:
        with open(nama_file, "r") as file:
            daftar_buku = json.load(file)
        print(f"Data berhasil dimuat dari '{nama_file}'")
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan. Membuat file baru...")
        daftar_buku = []
    except json.JSONDecodeError:
        print(f"File '{nama_file}' rusak atau kosong.")
        daftar_buku = []

menu()