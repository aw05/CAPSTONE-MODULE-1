data_barang ={
    '3011081':{'Produk':'Ikan Salmon',
            'Proses':'Fillet',
            'Kategori':'Ikan',
            'Kualitas': 'Super',
            'Unit':20000},
    '3022011':{'Produk':'Ikan Tuna Sirip Biru',
            'Proses':'Utuh Beku Laut',
            'Kategori':'Ikan',
            'Kualitas':'Super',
            'Unit':20000},
    '2021021':{'Produk':'Ayam Negeri',
            'Proses':'Fillet',
            'Kategori':'Unggas',
            'Kategori':'Ayam',
            'Kualitas':'Super',
            'Unit':25}}

## FUNGSI READ SEMUA DAFTAR
def read_data_semua():
    if len(data_barang)==0: # JIKA DATA BARANG TIDAK ADA AKAN KELUAR OUTPUT "MAAF BARANG KOSONG"
        print(f''' \n{'Daftar Barang'.center(125)}{'_'*122}''')
        print('Maaf, Barang Kosong'.center(123))
    else: # JIKA BARANG ADA MAKA KELUR OUTPUT DAFTAR BARANG DENGAN DESKRIPSINYA
        print(f''' \n{'Daftar Barang'.center(125)}{'_'*122}''')
        for i in data_barang:
            print(f'''  Id: {i} \t| Nama Produk: {data_barang[i]['Produk']}, Proses: {data_barang[i]['Proses']}, Kategori: {data_barang[i]['Kategori']}, Grade: {data_barang[i]['Kualitas']}, Unit (kg): {data_barang[i]['Unit']}''')

## FUNGSI READ BERDASARKAN NO ID
def read_data_id():
    if len(data_barang)==0: # JIKA DATA BARANG TIDAK ADA AKAN KELUAR OUTPUT "MAAF BARANG KOSONG"
        print(f''' \n{'Daftar Barang'.center(125)}{'_'*122}''')
        print('Maaf, Barang Kosong'.center(123))
    else:
        id_barang=input(' Masukkan no id yang ingin dilihat (7 digit angka): ')
# JIKA BARANG ADA DAN NO ID ADA DI DAFTAR
# MAKA KELUR OUTPUT DAFTAR BARANG DENGAN DESKRIPSINYA BERDASARKAN NO ID
        if id_barang in data_barang:
            print(f''' \n{'Daftar Barang'.center(125)}{'_'*122}''')
            print(f'''  Id: {id_barang} \t| Nama Produk: {data_barang[id_barang]['Produk']}, Proses: {data_barang[id_barang]['Proses']}, Kategori: {data_barang[id_barang]['Kategori']}, Grade: {data_barang[id_barang]['Kualitas']}, Unit (kg): {data_barang[id_barang]['Unit']}''')
# JIKA NO ID YANG DIMASUKKAN SALAH, MASUKKAN KEMBALI NO ID (7 DIGIT ANGKA)
        elif len(id_barang) != 7 or not id_barang.isdigit():
            print(' Coba lagi, mohon masukkan no id dengan 7 digit angka')
            read_data_id()
# JIKA NO ID SUDAH 7 DIGIT ANGKA TETAPI TIDAK ADA DI DAFTAR
        else:
            print(f'''\n         Maaf Barang Dengan No ID {id_barang} Tidak Tersedia''')

##   FUNGSI READ BERDASARKAN KATEGORI
def read_data_kategori():
    if len(data_barang)==0: # JIKA DATA BARANG TIDAK ADA AKAN KELUAR OUTPUT "MAAF BARANG KOSONG"
        print(f''' \n{'Daftar Barang'.center(125)}{'_'*122}''')
        print('Maaf, Barang Kosong'.center(123))
    else:
        jenis_barang=input(' Masukkan jenis barang apa yang ingin dilihat (ikan/daging/unggas): ')
# JIKA BARANG ADA DAN INPUT KATEGORI BENAR
# MAKA KELUR OUTPUT DAFTAR BARANG DENGAN DESKRIPSINYA BERDASARKAN KATEGORI
        if jenis_barang.lower()=='ikan' or jenis_barang.lower()=='daging' or jenis_barang.lower()=='unggas':
            print(f''' \n{'Daftar Barang'.center(125)}{'_'*122}''')
            for i in data_barang:
                if data_barang[i]['Kategori']==jenis_barang.capitalize():
                        print(f'''  Id: {i} \t| Nama Produk: {data_barang[i]['Produk']}, Proses: {data_barang[i]['Proses']}, Kategori: {data_barang[i]['Kategori']}, Grade: {data_barang[i]['Kualitas']}, Unit (kg): {data_barang[i]['Unit']}''')
# JIKA BUKAN IKAN/DAGING/UNGGAS MAKA KELUR OUTPUT SEBAGAI BERIKUT DAN INPUT KATEGORI KEMBALI
        else:
            print(' \n        Maaf yang anda masukkan salah \n')
            read_data_kategori()

##   FUNGSI READ BERDASARKAN GRADE
def read_data_grade():
    if len(data_barang)==0: # JIKA DATA BARANG TIDAK ADA AKAN KELUAR OUTPUT "MAAF BARANG KOSONG"
        print(f''' \n{'Daftar Barang'.center(125)}{'_'*122}''')
        print('Maaf, Barang Kosong'.center(123))
    else:
        grade_barang=input(' Masukkan grade barang yang ingin dilihat: ')
        list_grade=[]
        for i in data_barang:
            list_grade.append(data_barang[i]['Kualitas'])
# JIKA BARANG ADA DAN GRADE YANG INGIN DILIHAT ADA DI DAFTAR
# MAKA KELUR OUTPUT DAFTAR BARANG DENGAN DESKRIPSINYA BERDASARKAN GRADE
        if grade_barang.capitalize() in list_grade:
            print(f''' \n{'Daftar Barang'.center(125)}{'_'*120}''')
            for i in data_barang:
                if data_barang[i]['Kualitas']==grade_barang.capitalize():
                    print(f'''  Id: {i} \t| Nama Produk: {data_barang[i]['Produk']}, Proses: {data_barang[i]['Proses']}, Kategori: {data_barang[i]['Kategori']}, Grade: {data_barang[i]['Kualitas']}, Unit (kg): {data_barang[i]['Unit']}''')
# JIKA GRADE YANG DIINGINKAN TIDAK ADA DI DAFTAR
# MAKA OUTPUT SEPERTI BERIKUT DAN KEMBALI KE MENU READ DATA
        else:
            print(f'\n Tidak Ada Barang Dengan Kategori {grade_barang}')

##   FUNGSI MENU UNTUK MENAMPILKAN DAFTAR PRODUK
def read_data():
    while True:
        read_menu=input(f''' \n
    {"="*19} List Menu Read Data: {"="*19}\n
    1. Menampilkan Semua Daftar Barang
    2. Menampilkan Daftar Barang Berdasarkan No Id Barang
    3. Menampilkan Daftar Barang Berdasarkan Kategori
    4. Menampilkan Daftar Barang Berdasarkan Tipe Grade Barang
    0. Kembali Ke Menu Utama \n
    Masukkan angka menu yang ingin dilakukan: ''')

        if read_menu == '1':
            read_data_semua()
        elif read_menu == '2':
            read_data_id()
        elif read_menu == '3':
            read_data_kategori()
        elif read_menu == '4':
            read_data_grade()
        elif read_menu == '0':
            break
        else:
            print('Menu yang diinginkan tidak ada, tolong masukkan kembali')
            read_menu()

##   FUNGSI CREATE DATA BARU
def create_data_baru():
        while True:
            id_barang_baru=input('Masukkan no id barang baru (7 digit angka): ')
# JIKA BARANG ADA DAN NO ID BARANG BARU ADA DI DAFTAR
# MAKA KELUR OUTPUT 'BARANG TERSEDIA
            if id_barang_baru in data_barang:
                print(f'\n      Barang dengan no id {id_barang_baru} sudah terdaftar')
# JIKA NO ID BARANG BARU BUKAN 7 DIGIT ANGKA
# MAKA KELUR OUTPUT SEBAGAI BERIKUT DAN COBA INPUT KEMBALI
            elif len(id_barang_baru) != 7 or not id_barang_baru.isdigit():
                print(' Coba lagi, mohon masukkan no id dengan 7 digit angka')
# JIKA NO ID BARANG BARU SUDAH 7 DIGIT ANGKA DAN TIDAK ADA DI DAFTAR
# MAKA DAPAT MENAMBAHKAN DATA BARANG BARU
            else:
                break

# input nama dari produk baru
        produk_baru=input('Masukkan Nama Barang Baru: ')
# input proses dari produk baru
        proses_barang_baru=input('Masukkan Proses Yang Dilakukan Pada Barang Baru: ')

# input kategori dari produk baru
        while True:
            kategori_barang_baru=input('Masukkan Kategori Barang Baru (Ikan/Daging/Unggas): ')
            if kategori_barang_baru.lower()=='ikan' or kategori_barang_baru.lower()=='daging' or kategori_barang_baru.lower()=='unggas':
                break
# input grade dari produk baru
        grade_barang_baru=input('Masukkan Grade Dari Barang Baru: ')
# input stok dari produk baru
        while True:
            stok_produk_baru=input('Masukkan Jumlah Stok Barang Baru (kg): ')
            if stok_produk_baru.isnumeric() == False:
                print("\n   Masukkan jumlah stok dalam kg")
            else:
                break
    
        data_barang.update({id_barang_baru:{'Produk': produk_baru,
                                        'Proses': proses_barang_baru.capitalize(),
                                        'Kategori': kategori_barang_baru.capitalize(),
                                        'Kualitas': grade_barang_baru.capitalize(),
                                        'Unit': int(stok_produk_baru)}})
        read_data_semua()
        while True:
            tanya_lagi=input('Apakah masih ada yang ingin diinput?(ya/tidak) ')
            if tanya_lagi.lower() == 'ya':
                create_data_baru()
                break
            elif tanya_lagi.lower() == 'tidak':
                create_data()
                break

##       FUNGSI MENU UNTUK MENAMBAHKAN DATA
def create_data():
    while True:
        create_menu=input(f''' \n
    {"="*11} List Menu Input Data {"="*11} \n
    1. Menambahkan Barang Baru Ke Daftar Barang
    0. Kembali Ke Menu Utama \n
    Masukkan angka menu yang ingin dilakukan: ''')

        if create_menu == '1':
            create_data_baru()
            break
        elif create_menu == '0':
            break
        else:
            print(' Menu yang diinginkan tidak ada, tolong masukkan kembali')

##   FUNGSI DELETE DATA
def delete_data():
    read_data_semua()
    if len(data_barang)==0: # JIKA DATA BARANG TIDAK ADA MAKA TIDAK DAPAT MELAKUKAN DELETE
        print(' TIDAK ADA BARANG YANG DAPAT DIHAPUS')
        delete_data_menu()
    else:
        id_barang_dihapus=input('Masukkan no id Barang yang akan dihapus (7 digit angka): ')

# JIKA BARANG ADA DAN NO ID ADA DI DAFTAR
# MAKA BARANG AKAN DIHAPUS DENGAN MEMVALIDASI TERLEBIH DAHULU
        if id_barang_dihapus in data_barang.keys():
            print(f''' \n{'Daftar Barang'.center(125)}{'_'*122}''')
            while True:
                validasi_hapus=input(f'Apakah anda yakin akan menghapus barang dengan no id {id_barang_dihapus} dari daftar?(ya/tidak) ')
                if validasi_hapus.lower() == 'ya':
                    del data_barang[id_barang_dihapus]
                    read_data_semua()
                    while True:
                        coba_tanya_lagi=input('Apakah masih ada yang ingin dihapus?(ya/tidak) ')
                        if coba_tanya_lagi.lower() == 'ya':
                            delete_data()
                        elif coba_tanya_lagi.lower() == 'tidak':
                            delete_data_menu()
                        break
# APABILA SAAT VALIDASI TIDAK JADI MAKA KEMBALI KE MENU DELETE DATA
                elif validasi_hapus.lower() == 'tidak':
                    delete_data_menu()
                break
# JIKA NO ID BUKAN 7 DIGIT ANGKA
# MAKA KELUR OUTPUT SEBAGAI BERIKUT DAN COBA INPUT KEMBALI
        elif len(id_barang_dihapus) != 7:
            print(' Coba lagi, mohon masukkan no id dengan 7 digit angka')
            delete_data()
        elif id_barang_dihapus.isdigit() == False:
            print(' Coba lagi, mohon masukkan no id dengan 7 digit angka')
            delete_data()
# JIKA NO ID BARANG BARU SUDAH 7 DIGIT ANGKA DAN TIDAK ADA DI DAFTAR
# MAKA KEMBALI KE MENU DELETE DATA
        else:
            print(f'''\n Maaf barang dengan no id {id_barang_dihapus} tidak tersedia''')
            delete_data_menu()

##       FUNGSI MENU UNTUK MENGHAPUS DATA
def delete_data_menu():
    while True:
        delete_menu=input(f''' \n
    {'='*10} List Menu Hapus Data {'='*10} \n
    1. Menghapus Barang Dari Daftar Barang
    0. Kembali Ke Menu Utama \n
    Masukkan angka menu yang ingin dilakukan: ''')

        if delete_menu == '1':
            delete_data()
            break
        elif delete_menu == '0':
            break
        else:
            print('Menu yang diinginkan tidak ada, tolong masukkan kembali')
            delete_data_menu()

##   FUNGSI UPDATE DATA UNTUK BARANG DATANG
def update_data_datang():
    id_datang=input('Masukkan no id barang yang datang (7 digit): ')

# JIKA BARANG ADA DAN NO ID ADA DI DAFTAR
# MAKA BARANG AKAN DITAMBAH JUMLAH STOKNYA DENGAN JUMLAH YANG DIINGINKAN DALAM KG
    if id_datang in data_barang.keys():
        while True:
            jumlah_produk_datang=input(' Masukkan jumlah barang yang datang (dalam kg): ')
            if jumlah_produk_datang.isdigit() == False:
                print('Tolong masukkan jumlah barang dalam  angka kg')
            else:
                data_barang[id_datang]['Unit']+= int(jumlah_produk_datang)
                read_data_semua()
                update_data_menu()
                break
# JIKA NO ID BUKAN 7 DIGIT ANGKA
# MAKA KELUR OUTPUT SEBAGAI BERIKUT DAN COBA INPUT KEMBALI        
    elif len(id_datang) != 7 or not id_datang.isdigit():
        print(' Coba lagi, mohon masukkan no id dengan 7 digit angka')
        update_data_datang()
# JIKA NO ID BARANG BARU SUDAH 7 DIGIT ANGKA DAN TIDAK ADA DI DAFTAR
# MAKA KEMBALI KE MENU PENGIRIMAN 
    else:
        print(f'\n  Barang dengan nomor id {id_datang} tidak ada')
        update_data_menu()

##   FUNGSI UPDATE DATA UNTUK MENGIRIM BARANG
def update_data_kirim():
    if len(data_barang)==0: # JIKA DATA BARANG TIDAK ADA MAKA TIDAK DAPAT MELAKUKAN PENGIRIMAN
        print(' MAAF BARANG KOSONG, TIDAK DAPAT MELAKUKAN PENGIRIMAN')
        update_data_menu()
    else:
        id_kirim=input('Masukkan no id barang yang akan dikirim (7 digit): ')
# JIKA BARANG ADA DAN NO ID ADA DI DAFTAR
# DAN BARANG AKAN DIKIRIM JUMLAH PENGIRIMAN DALAM KG DAN STOK MENCUKUPI
# PENGIRIMAN DAPAT DILAKUKAN
        if id_kirim in data_barang.keys():

            x = 'ya' # Untuk kondisi TRUE WHILE
            while x == 'ya':
                jumlah_produk_kirim=input('Masukkan jumlah barang yang dikirim (dalam kg): ')
                if jumlah_produk_kirim.isdigit() == False:
                    print(' Tolong masukkan jumlah barang dalam angka kg')
# JIKA STOK TIDAK MENCUKUPI JUMLAH PENGIRIMAN
# MAKA DITANYAKAN KEMBALI APAKAH INGIN MELAKUKAN PENGIRIMAN DENGAN JUMLAH BARU
# ATAU KEMBALI KE MENU PENGIRIMAN
                elif int(jumlah_produk_kirim)>data_barang[id_kirim]['Unit']:
                    print('\n       Stok tidak cukup')
                    while True:
                        input_lagi_tidak=input('Apakah ingin tetap mengirim barang dengan jumlah berbeda?(ya/tidak) ')
                        if input_lagi_tidak.lower() == 'tidak':
                            x = 'tidak' # Agar while dapat ke break
                            update_data_menu()
                            break
                        elif input_lagi_tidak.lower() == 'ya':
                            break
                        else:
                            print('Masukkan hanya dengan ya atau tidak')
                else:
                    data_barang[id_kirim]['Unit']-=int(jumlah_produk_kirim)
                    read_data_semua()
                    update_data_menu()
                    break

# JIKA NO ID BUKAN 7 DIGIT ANGKA
# MAKA KELUR OUTPUT SEBAGAI BERIKUT DAN COBA INPUT KEMBALI
        elif len(id_kirim) != 7 or not id_kirim.isdigit():
            print(' Coba lagi, mohon masukkan no id dengan 7 digit angka')
            update_data_kirim()
# JIKA NO ID BARANG BARU SUDAH 7 DIGIT ANGKA DAN TIDAK ADA DI DAFTAR
# MAKA KEMBALI KE MENU PENGIRIMAN 
        else:
            print(f'\n      Barang dengan nomor id {id_kirim} tidak ada')
            update_data_menu()

##       FUNGSI MENU UNTUK UPDATE DATA
def update_data_menu():
    while True:
        update_menu=input(f''' \n
    {'='*11} List Menu Pengiriman {'='*11} \n
    1. Barang Datang Ke Gudang
    2. Pengiriman Pesanan Ke Customer
    0. Kembali Ke Menu Utama \n
    Masukkan angka menu yang ingin dilakukan: ''')
        if update_menu == '1':
            update_data_datang()
            break
        elif update_menu == '2':
            update_data_kirim()
            break
        elif update_menu == '0':
            break
        else:
            print('Menu yang diinginkan tidak ada, tolong masukkan kembali')
            update_data_menu()



##       FUNGSI UTAMA       ##
def gudang_ikan():
    while True:
        list_menu=input(f''' {'-'*46} SELAMAT DATANG DI GUDANG IKAN {'-'*46} 
    {'List Menu:'.center(50)}
    {'1. Menampilkan Daftar Barang'.center(72)}
    {'2. Menambahkan Barang Baru'.center(70)}
    {'3. Menghapus Barang Yang Tidak Diinginkan'.center(85)}
    {'4. Proses Pengiriman'.center(63)}
    {'5. Exit Program'.center(60)}\n
 Masukkan angka menu yang ingin dijalankan: ''')

        if list_menu == '1':
            read_data()
        
        elif list_menu == '2':
            create_data()

        elif list_menu == '3' :
            delete_data_menu()

        elif list_menu == '4':
            update_data_menu()

        elif list_menu== '5':
            while True:
                tanya_selesai=input(' Apakah anda yakin selesai?(ya/tidak) ')
                if tanya_selesai.lower() == 'tidak':
                    gudang_ikan()
                    break
                elif tanya_selesai.lower() == 'ya':
                    print(f''' \n Baik, terima kasih! \n
 {'-'*50} SAMPAI JUMPA KEMBALI {'-'*50} ''')
                    break
                else:
                    print('Jawaban hanya ya/tidak')
            break
       
        else:
            print('Pilihan menu hanya 1-5, silahkan coba lagi!\n')

gudang_ikan()