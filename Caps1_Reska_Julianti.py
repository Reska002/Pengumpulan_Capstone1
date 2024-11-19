from tabulate import tabulate
import datetime
transaksi = [
    ['Trx001', datetime.date(2023, 11, 1), 'Pembelian Bahan Baku', 'Persediaan', 'Kas', 1000000],
    ['Trx002', datetime.date(2023, 11, 2), 'Penjualan Produk', 'Kas', 'Pendapatan', 1000000],
    ['Trx003', datetime.date(2023, 11, 3), 'Pembayaran Gaji', 'Beban Gaji', 'Kas', 500000],
    ['Trx004', datetime.date(2023, 11, 4), 'Pembelian Peralatan', 'Peralatan', 'Kas', 2000000],
    ['Trx005', datetime.date(2023, 11, 5), 'Pendapatan Jasa', 'Kas', 'Pendapatan', 1500000],
    ['Trx006', datetime.date(2023, 11, 6), 'Bayar Listrik', 'Beban Listrik', 'Kas', 300000],
    ['Trx007', datetime.date(2023, 11, 7), 'Penjualan Jasa', 'Kas', 'Pendapatan', 1200000],
    ['Trx008', datetime.date(2023, 11, 8), 'Pembayaran Pajak', 'Beban Pajak', 'Kas', 2500000],
    ['Trx009', datetime.date(2023, 11, 9), 'Pelunasan Utang', 'Utang Usaha', 'Kas', 800000],
    ['Trx010', datetime.date(2023, 11, 10), 'Pendapatan Sewa', 'Kas', 'Pendapatan', 2000000]   
]

def hapus_transaksi():
     if transaksi:
            for data in range(len(transaksi)): #untuk menambahkan semua transaksi yang ada di dalam list ke dalam tabel untuk ditampilkan
                    print("\n\t\t\t     ----- Data Transaksi -----")
                    print(tabulate(transaksi,headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                    break
            id_transaksi = input("\nMasukkan ID Transaksi Yang Ingin Diubah (Trx00_): ").capitalize()

            # for i, data in enumerate(transaksi):
            for data in transaksi:
                if data[0] == id_transaksi:
                    print("\n\t\t\t----- Data Transaksi Ditemukan -----")
                    print(tabulate([data],headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline')) 
                # transaksi[0] == id_transaksi
                    print("\nApakah Anda Ingin Menghapus Transaksi Ini?")
                    simpan = input("Ketik 'Y' Untuk Menyimpan Atau 'N' Untuk Batal: ").upper()
                    if simpan == 'Y':
                        print(f"\n---------------------------- Transaksi Dengan ID {id_transaksi} Berhasil Dihapus ----------------------------")
                        transaksi.remove(data)
                        for data in range(len(transaksi)): #untuk menambahkan semua transaksi yang ada di dalam list ke dalam tabel untuk ditampilkan
                            print("\n\t\t\t----- Data Transaksi -----")
                            print(tabulate(transaksi,headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                            break
                    elif simpan=='N':
                        print("\n----------------------------- Transaksi Batal Dihapus -----------------------------")
                        for data in range(len(transaksi)): #untuk menambahkan semua transaksi yang ada di dalam list ke dalam tabel untuk ditampilkan
                            print("\n\t\t\t----- Data Transaksi -----")
                            print(tabulate(transaksi,headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                            break
                    return
            print("\n-------------------- Data tidak ditemukan --------------------\n")



def menu_utama():
    while True:
        print('\n======= MENU UTAMA =======\n1. Lihat Data Transaksi\n2. Tambah Data Transaksi\n3. Ubah Data Transaksi\n4. Hapus Data Transaksi\n5. Keluar\n==========================')
        pilihan=input('Pilih menu (1-5) :')

        if pilihan == '1': # menu untuk menampilkan transaksi
            submenu_1()

        elif pilihan == '2': # Menambahkan data transaksi
            submenu_2()

        elif pilihan == '3':# Menu untuk mengubah data transaksi
            submenu_3()
                
        elif pilihan == '4':# Menu untuk menghapus data transkasi
            submenu_4()

        elif pilihan == '5':
            print("\n------- Keluar Dari Program -------\n")
            break# Menu untuk keluar dari looping
        else: # Bila pilihan diluar 1-5 makan akan muncul 
            print("\n----------------------- Pilihan Tidak Valid. Coba Lagi -----------------------\n")
        # else:Bila pilihan diluar 1-5 makan akan muncul
def submenu_1():
    while True:
        print('\n\t    Lihat Data Transaksi\n------------------------------------------\n1. Tampilkan Semua Transaksi\n2. Tampilkan Transaksi Berdasarkan ID\n3. Tampilkan Transaksi Berdasarkan Tanggal\n4. Keluar\n------------------------------------------')
        pilihan=input('Pilih menu (1-4): ')
        if pilihan=='1':
            if transaksi:
                print("\n\t\t\t     ----- Data Transaksi -----")
                empty_list=[]
                # print('Data Transaksi\n')
                if transaksi:
                    for data in range(len(transaksi)): #untuk menambahkan semua transaksi yang ada di dalam list ke dalam tabel untuk ditampilkan
                    # for data in transaksi:
                        empty_list.append([transaksi[data][0], transaksi[data][1], transaksi[data][2], transaksi[data][3], transaksi[data][4],transaksi[data][5]])
                    print(tabulate(empty_list,headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                else:
                    print("\n---------------------------------- Data Transaksi Tidak Ditemukan ----------------------------------\n")
                    break

        elif pilihan=='2':
            id_transaksi = input("\nMasukkan ID Transaksi (Trx00_) : ").capitalize()
            # Cari transaksi dengan ID yang sesuai
            for data in transaksi:
                if data[0] == id_transaksi:
                    print("\n\t\t\t----- Data Transaksi Ditemukan -----")
                    print(tabulate([data],headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                    break  # Keluar dari perulangan jika data sudah ditemukan
            else:
                print("\n------- Transaksi Dengan ID", id_transaksi, "Tidak Ditemukan -------\n")
            
                
        elif pilihan=='3':
            tanggal= input("\nMasukkan tanggal (2023-11-DD (1-30)): ")
            try:
                tanggal = datetime.datetime.strptime(tanggal, "%Y-%m-%d").date()
                # Pengecekan batas tanggal
                tanggal_awal = datetime.date(2023, 11, 1)
                tanggal_akhir = datetime.date(2023, 11, 30)
                if  (tanggal < tanggal_awal) or (tanggal > tanggal_akhir):
                    print("Tanggal Harus Berada di Antara 2023-11-01 dan 2023-11-30.")
                    continue
            except ValueError:
                print("Format Tanggal Salah. Gunakan Format YYYY-MM-DD.")
                continue
            found = False
            for data in transaksi:
                if data[1]==tanggal:
                    print("\n\t\t----- Data Transaksi Ditemukan -----")
                    print(tabulate([data],headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                    found = True
                    break 
            if not found:
                print(f"\n----- Tidak Ada Transaksi Pada Tanggal {tanggal} -----\n")
                continue
                    
        elif pilihan=='4': # Menu untuk keluar dari looping
                print("\n----- Keluar Dari Program Menu Melihat Data Transaksi -----\n")
                break
        
        else: # Bila pilihan diluar 1-4 makan akan muncul 
                print("\n----------------------- Pilihan Tidak Valid. Coba Lagi -----------------------\n")
def submenu_2():
    while True:
        print('\n   Menu Tambah Data\n-------------------------\n1. Tambah Data Transaksi\n2. Keluar\n-------------------------')
        pilihan=input('Pilih menu (1-2): ')
        if pilihan=='1':
            print("\n\t\t\t     ----- Data Transaksi -----")
            print(tabulate(transaksi, headers=['ID', 'Tanggal', 'Keterangan', 'Debit', 'Kredit', 'Jumlah'], tablefmt='double_outline'))
            id_transaksi = input("\nMasukkan ID Transaksi (Trx00_) : ").capitalize()
            # Cari transaksi dengan ID yang sesuai
            for data in transaksi:
                if data[0] == id_transaksi:
                    print("\n\t\t   ------- Data Transaksi Sudah Ada -------\n")
                    print(tabulate([data],headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                    break  # Keluar dari perulangan jika data sudah ditemukan

            else:  # Jika tidak ditemukan
                print(f"\n-------------------------- ID {id_transaksi} Tidak Ditemukan --------------------------\n")
                print("\nTambah Transaksi Baru")
                id_transaksi = input("Masukkan ID transaksi Baru (Trx00_): ").capitalize()
                while True:
                    tanggal = input("Masukkan Tanggal (2023-11-DD (1-30))) Baru: ")
                    try:
                        tanggal = datetime.datetime.strptime(str(tanggal), "%Y-%m-%d").date()
                        # Pengecekan batas tanggal
                        tanggal_awal = datetime.date(2023, 11, 1)
                        tanggal_akhir = datetime.date(2023, 11, 30)
                        if  (tanggal < tanggal_awal) or (tanggal > tanggal_akhir):
                            print("Tanggal Harus Berada di Antara 2023-11-01 dan 2023-11-30.")
                            continue
                    except ValueError:
                        print("Format Tanggal Salah. Gunakan Format YYYY-MM-DD.")
                        continue
                    keterangan =input("Masukkan Deskripsi Transaksi Baru: ").title()
                    while not keterangan.isalpha()and keterangan.isspace():
                        print('Data Yang Dimasukan Salah Coba Lagi')
                        keterangan = input("Masukkan Deskripsi Transaksi Baru: ").title()
                    debit = input("Masukkan Akun Debet Baru: ").title()
                    while not debit.isalpha()and debit.isspace():
                        print('Data Yang Dimasukan Salah Coba Lagi')
                        debit =input("Masukkan Akun Debet Baru: ").title()
                    kredit = input("Masukkan Akun Kredit Baru: ").title()
                    while not kredit.isalpha()and kredit.isspace():
                        print('Data Yang Dimasukan Salah Coba Lagi')
                        kredit =input("Masukkan Akun Kredit Baru: ").title()
                    jumlah = int(input("Masukkan Jumlah Baru : "))
                    print("Apakah Anda Ingin Menyimpan Data Ini?")
                    simpan = input("Ketik 'Y' Untuk Menambah Atau 'N' Untuk Batal: ").upper()
                    if simpan == 'Y':
                        print("\n------------------ Transaksi Berhasil Ditambahkan ------------------")
                        transaksi.append([id_transaksi, tanggal, keterangan, debit, kredit, jumlah])
                        for data in range(len(transaksi)):
                            print("\n\t\t\t     ----- Data Transaksi -----")
                            print(tabulate(transaksi,headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                        break
                    else:
                        print("\n------------ Data Batal Disimpan ------------")

        elif pilihan=='2': # Menu untuk keluar dari looping
                print("\n----- Keluar Dari Program Menu Menambah Data Transaksi -----\n")
                break

        else: # Bila pilihan diluar 1-2 makan akan muncul 
                print("\n----------------------- Pilihan Tidak Valid. Coba Lagi -----------------------\n")
def submenu_3():
    while True:
        print('\n       Menu Ubah Data\n--------------------------\n1. Ubah Berdasarkan ID\n2. Ubah Jumlah Transaksi\n3. Ubah Tanggal Transaksi\n4. Keluar\n--------------------------')
        pilihan = input('Pilih menu (1-4): ')
        if pilihan == '1':
            if transaksi:
                print("\n\t\t\t     ----- Data Transaksi -----")
                print(tabulate(transaksi, headers=['ID', 'Tanggal', 'Keterangan', 'Debit', 'Kredit', 'Jumlah'], tablefmt='double_outline'))
                id_transaksi = input("\nMasukkan ID Transaksi Yang Ingin Diubah (Trx00_): ").capitalize()
                # Mencari data berdasarkan ID
                for data in transaksi:
                    if data[0] == id_transaksi:  # ID ditemukan
                        print("\n\t\t\t----- Data Transaksi -----")
                        print(tabulate([data], headers=['ID', 'Tanggal', 'Keterangan', 'Debit', 'Kredit', 'Jumlah'], tablefmt='double_outline'))
                        # Meminta data baru
                        while True:
                            tanggal_baru = input("Tanggal Baru (2023-11-DD (1-30)): ")
                            try:
                                tanggal_baru = datetime.datetime.strptime(tanggal_baru, "%Y-%m-%d").date()
                                # Pengecekan batas tanggal
                                tanggal_awal = datetime.date(2023, 11, 1)
                                tanggal_akhir = datetime.date(2023, 11, 30)
                                if  (tanggal_baru < tanggal_awal) or (tanggal_baru > tanggal_akhir):
                                    print("Tanggal Harus Berada di Antara 2023-11-01 dan 2023-11-30.")
                                    continue
                            except ValueError:
                                print("Format Tanggal Salah. Gunakan Format YYYY-MM-DD.")
                                continue
                            break
                        keterangan_baru=input("Masukkan Deskripsi Transaksi Baru: ").title()
                        while not keterangan_baru.isalpha():
                            print('Data Yang Dimasukan Salah Coba Lagi')
                            keterangan_baru =input("Keterangan Baru: ").title()
                        akun_debit_baru =input("Akun Debit Baru: ").title()
                        while not akun_debit_baru.isalpha():
                            print('Data Yang Dimasukan Salah Coba Lagi')
                            akun_debit_baru =input("Akun Debit Baru: ").title()
                        akun_kredit_baru =input("Akun Kredit Baru: ").title()
                        while not akun_kredit_baru.isalpha():
                            print('Data Yang Dimasukan Salah Coba Lagi')
                            akun_kredit_baru =input("Akun Debit Baru: ").title()
                        jumlah_baru = int(input("Jumlah Baru: "))

                        print("Apakah Anda Ingin Menyimpan Data Ini?")
                        simpan = input("Ketik 'Y' Untuk Menyimpan Atau 'N' Untuk Batal: ").upper()
                        if simpan == 'Y':
                            # Update data
                            data[1] = tanggal_baru.strftime("%Y-%m-%d")
                            data[2] = keterangan_baru
                            data[3] = akun_debit_baru
                            data[4] = akun_kredit_baru
                            data[5] = jumlah_baru

                            print("\n---------------------------- Transaksi Berhasil Diubah ----------------------------")
                            print("\n\t\t\t     ----- Data Transaksi -----")
                            print(tabulate(transaksi, headers=['ID', 'Tanggal', 'Keterangan', 'Debit', 'Kredit', 'Jumlah'], tablefmt='double_outline'))
                        else:
                            print("\n----------------------------- Data Batal Disimpan -----------------------------")
                        break
                else:
                    print(f"\n---------------------------- Transaksi Dengan ID {id_transaksi} Tidak Ditemukan ----------------------------\n")
                continue

        elif pilihan=='2':
            if transaksi:
                # Tampilkan data transaksi yang ada
                print("\n\t\t\t     ----- Data Transaksi -----")
                print(tabulate(transaksi, headers=['ID', 'Tanggal', 'Keterangan', 'Debit', 'Kredit', 'Jumlah'], tablefmt='double_outline'))

                id_transaksi = input("\nMasukkan ID Transaksi Yang Ingin Diubah (Trx00_): ").capitalize()
                # Cari transaksi dengan ID yang sesuai
                for data in transaksi:
                    if data[0] == id_transaksi:
                        print("\n\t\t\t----- Data Transaksi -----")
                        print(tabulate([data],headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                        # Keluar dari perulangan jika data sudah ditemukan
                        if  id_transaksi <= len(transaksi):
                                jumlah_baru= int(input("Masukan Jumlah Baru: "))
                                print("Apakah Anda Ingin Menyimpan Data Ini?")
                                simpan = input("Ketik 'Y' Untuk Menyimpan Atau 'N' Untuk Batal: ").upper()
                                if simpan == 'Y':
                                    data[5]=jumlah_baru
                                    print("\n---------------------------- Transaksi Berhasil Diubah ----------------------------")
                                    for data in range(len(transaksi)): #untuk menambahkan semua transaksi yang ada di dalam list ke dalam tabel untuk ditampilkan
                                        print("\n\t\t\t     ----- Data Transaksi -----")
                                        print(tabulate(transaksi,headers=['ID','Tanggal','Keterangan','Debit','Kredit','Jumlah'],tablefmt='double_outline'))
                                        break
                                    break 
                                elif simpan=='N':
                                        print("\n----------------------------- Data Batal Disimpan -----------------------------")
                                        break
                else:
                    print("\n---------------------------- Transaksi Dengan ID", id_transaksi, "Tidak Ditemukan ----------------------------\n")   

        elif pilihan == "3":
            if transaksi:
            # Tampilkan data transaksi yang ada
                print("\n\t\t\t     ----- Data Transaksi -----")
                print(tabulate(transaksi, headers=['ID', 'Tanggal', 'Keterangan', 'Debit', 'Kredit', 'Jumlah'], tablefmt='double_outline'))
            # Meminta input ID Transaksi
                id_transaksi = input("\nMasukkan ID Transaksi Yang Ingin Diubah (Trx00_): ").capitalize()
                # Cari transaksi berdasarkan ID
                for data in transaksi:
                    if data[0] == id_transaksi:  # Jika ID ditemukan
                        print("\n\t\t\t----- Data Transaksi -----")
                        print(tabulate([data], headers=['ID', 'Tanggal', 'Keterangan', 'Debit', 'Kredit', 'Jumlah'], tablefmt='double_outline'))
                        # Meminta tanggal baru
                        while True:
                            tanggal_baru = input("Masukkan Tanggal Transaksi Baru (2023-11-DD (1-30)): ")
                            try:
                                tanggal_baru = datetime.datetime.strptime(tanggal_baru, "%Y-%m-%d").date()
                                # Pengecekan batas tanggal
                                tanggal_awal = datetime.date(2023, 11, 1)
                                tanggal_akhir = datetime.date(2023, 11, 30)
                                if  (tanggal_baru < tanggal_awal) or (tanggal_baru > tanggal_akhir):
                                    print("Tanggal Harus Berada di Antara 2023-11-01 dan 2023-11-30.")
                                    continue
                            except ValueError:
                                print("Format Tanggal Salah. Gunakan Format YYYY-MM-DD.")
                                continue
                            print("Apakah Anda Ingin Menyimpan Data Ini?")
                            simpan = input("Ketik 'Y' Untuk Menyimpan Atau 'N' Untuk Batal: ").upper()
                            if simpan == 'Y':
                                # Update tanggal pada data yang ditemukan
                                data[1] = tanggal_baru.strftime("%Y-%m-%d")
                                print("\n---------------------------- Transaksi Berhasil Diubah ----------------------------")
                                print("\n\t\t\t     ----- Data Transaksi -----")
                                print(tabulate(transaksi, headers=['ID', 'Tanggal', 'Keterangan', 'Debit', 'Kredit', 'Jumlah'], tablefmt='double_outline'))
                            else:
                                print("\n----------------------------- Data Batal Disimpan -----------------------------")
                            tanggal_baru = input("Tanggal Baru (2023-11-DD (1-30)): ")
                else:
                    # Jika ID tidak ditemukan
                    print(f"\n---------------------------- Transaksi Dengan ID {id_transaksi} Tidak Ditemukan ----------------------------\n")
                    continue
def submenu_4():
    while True:
        print('\n     Menu Menghapus Data Transaksi\n---------------------------------------\n1. Hapus Data\n2. Keluar\n---------------------------------------')
        pilihan=input('Pilih menu (1-2): ')
        if pilihan=='1':
            hapus_transaksi()

        elif pilihan=='2': # Menu untuk keluar dari looping
                print("\n----- Keluar Dari Program Menu Menghapus Data Transaksi -----\n")
                break
        
        else: # Bila pilihan diluar 1-2 makan akan muncul 
                print("\n----------------------- Pilihan Tidak Valid. Coba Lagi -----------------------\n")

menu_utama()


# submenu 2 juga salah 
# submenu 3 masih ada yang salah (ga bisa nambah transaksi gara" ID nya campuran ins sama str)
# masih banyak yg harus diperbaiki

