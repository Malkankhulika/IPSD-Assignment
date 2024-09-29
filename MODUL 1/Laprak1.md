# <h1 align="center">Laporan Praktikum Modul Dasar-Dasar Python untuk Sains Data</h1>
<p align="center">Khulika Malkan</p>

## Dasar Teori

Berikan penjelasan teori terkait materi modul ini dengan bahasa anda sendiri serta susunan yang terstruktur per topiknya.

## Guided 

### 1. [Nama Topik]

```python
print("ini adalah file code guided praktikan")
```
Kode di atas digunakan untuk mencetak teks "ini adalah file code guided praktikan" ke layar menggunakan function print untuk mengeksekusi nya.

## Unguided 

### 1. Buatlah program yang dapat menghasilkan pola berbentuk angka seperti di bawah ini, dengan syarat angka yang ditampilkan adalah hasil dari penjumlahan bilangan prima sebelumnya dan Jumlah angka pada setiap baris bertambah 1, dan bilangan yang ditampilkan adalah bilangan prima.
```
1
2 3
5 7 11
13 17 19 23
```
#### Kode Program:
```python
# Fungsi untuk memeriksa apakah suatu bilangan adalah prima
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Fungsi untuk mencetak pola bilangan prima dengan batas tertentu
def print_prime_pattern(limit):
    prime_count = 0  # Menghitung jumlah bilangan prima yang telah ditemukan
    num = 2  # Memulai pencarian bilangan prima dari angka 2

    for row in range(1, limit+1):
        # Cetak bilangan prima sebanyak 'row' buah di baris ini
        for _ in range(row):
            # Cari bilangan prima berikutnya
            while not is_prime(num):
                num += 1
            # Tampilkan bilangan prima
            print(num, end=' ')
            num += 1  # Siapkan untuk bilangan prima berikutnya

            prime_count += 1  # Hitung jumlah bilangan prima yang dicetak
            if prime_count == 9:  # Berhenti jika sudah sampai bilangan prima ke-9 (yaitu 23)
                return
        print()  # Ganti baris setelah mencetak bilangan prima untuk baris ini

# Menjalankan program hingga bilangan prima 23
print_prime_pattern(5)
```
#### Output:
![image](https://github.com/user-attachments/assets/25eefb8f-e30e-4703-9eb0-85a757580bdf)

#### Penjelasan:
Kode di atas menggunakan fungsi is_prime(num) untuk mengecek apakah bilangan adalah bilangan prima
- Tujuan Fungsi: Fungsi ini digunakan untuk memeriksa apakah suatu bilangan num merupakan bilangan prima atau tidak.
- Langkah-langkah:
- Baris if num < 2:: Jika bilangan lebih kecil dari 2, langsung dikembalikan False karena bilangan prima dimulai dari 2.
- Baris for i in range(2, int(num**0.5) + 1):: Untuk bilangan num yang lebih besar dari 1, kita melakukan perulangan dari 2 sampai akar kuadrat dari num. Kita hanya perlu memeriksa faktor hingga akar kuadratnya karena faktor di atasnya sudah pasti simetris dengan yang ada di bawah akar kuadrat.
- Baris if num % i == 0:: Jika ada angka i yang membagi num secara sempurna (tanpa sisa), maka bilangan tersebut bukan bilangan prima, sehingga dikembalikan False.
- Baris return True:: Jika tidak ada angka yang dapat membagi num, bilangan tersebut adalah bilangan prima, maka fungsi mengembalikan True.

### 2. Buatlah sebuah fungsi yang menerima dua input berupa list angka. Fungsi ini harus mengembalikan sebuah list baru yang berisi elemen dari dua list input yang memiliki indeks ganjil. List baru tersebut juga harus diurutkan secara menurun berdasarkan nilai elemen.
#### kode program:
```python
def ambil_ganjil_dan_urutkan(list1, list2):  
    # Ambil elemen dengan indeks ganjil dari list1 dan list2
    ganjil_list1 = [list1[i] for i in range(1, len(list1), 2)]  # Mengambil elemen dengan indeks ganjil dari list1
    ganjil_list2 = [list2[i] for i in range(1, len(list2), 2)]  # Mengambil elemen dengan indeks ganjil dari lis2

    # Menggabungkan elemen-elemen dari kedua daftar
    gabungan = ganjil_list1 + ganjil_list2

    # Mengurutkan daftar gabungan secara menurun
    gabungan.sort(reverse=True)

    return gabungan   # Mengembalikan daftar yang sudah diurutkan

# Contoh penggunaan
list1 = [10, 21, 32, 43, 54, 65]
list2 = [11, 22, 33, 44, 55, 66]

hasil = ambil_ganjil_dan_urutkan(list1, list2)
print(hasil)
```
#### Output:
![image](https://github.com/user-attachments/assets/883b1867-a66f-41ea-ae5a-fec3aad6358b)

#### penjelasan:
kode ini membuat Fungsi: ambil_ganjil_dan_urutkan(list1, list2)
Fungsi ini memiliki dua daftar input, list1 dan list2. Tugas dari fungsi ini adalah:
- Mengambil elemen-elemen yang berada di indeks ganjil dari kedua daftar.
- Menggabungkan elemen-elemen tersebut menjadi satu daftar.
- Mengurutkan hasil gabungan tadi secara menurun (dari yang terbesar ke yang terkecil).
- Mengembalikan hasil akhir berupa daftar elemen yang sudah diurutkan.

### 3. Buat sebuah program untuk mensimulasikan transaksi ATM. Program harus: 
1. Meminta pengguna memasukkan PIN (dibatasi 3 kali percobaan).
2. Setelah PIN benar, meminta jumlah penarikan.
3. Jika saldo kurang dari jumlah yang ditarik, munculkan pesan kesalahan.
4. Jika penarikan berhasil, tampilkan saldo akhir.
#### kode program:
```python
# Simulasi ATM dengan penanganan PIN dan saldo
def atm_simulasi():
  # Deklarasi variabel utama
    pin_terdaftar = "1234"  # PIN yang benar
    saldo = 100000  # Saldo awal pengguna dalam rupiah
    kesempatan_pin = 3  # Kesempatan memasukkan PIN

    # Proses input PIN
    while kesempatan_pin > 0:
        pin_input = input("Masukkan PIN Anda: ")
        if pin_input == pin_terdaftar:
            print("PIN benar.\n")
            break  # Keluar dari loop jika PIN benar
        else:
            kesempatan_pin -= 1
            print(f"PIN salah. Kesempatan tersisa: {kesempatan_pin}")
            if kesempatan_pin == 0:
                print("Anda telah gagal memasukkan PIN 3 kali. Akun diblokir.")
                return  # Keluar dari fungsi jika kesempatan habis

    # Proses penarikan Uang
    while True:
        try:
            penarikan = int(input("Masukkan jumlah penarikan: "))

            if penarikan <= 0:
                print("Jumlah penarikan harus lebih dari nol.")
                continue

            if penarikan > saldo:
                print("Saldo tidak mencukupi. Silakan masukkan jumlah yang lebih kecil.")
            else:
                saldo -= penarikan
                print(f"Penarikan berhasil. Sisa saldo Anda: Rp {saldo}")
                break  # Penarikan berhasil, keluar dari loop
        except ValueError:
            print("Masukkan jumlah penarikan dalam angka yang valid.")

# Menjalankan simulasi ATM
atm_simulasi()
```
#### Output:
![image](https://github.com/user-attachments/assets/67226bb9-41c6-4224-8bef-a128658392b0)


#### Penjelasan:
1. Proses input PIN
•  Looping PIN: Program akan meminta pengguna untuk memasukkan PIN hingga PIN yang dimasukkan benar atau hingga kesempatan habis.
•  Jika PIN yang dimasukkan benar, program akan menampilkan pesan "PIN benar" dan keluar dari proses ini.
•  Jika PIN yang dimasukkan salah, jumlah kesempatan akan berkurang, dan pengguna akan diberitahu berapa banyak kesempatan yang tersisa.
•  Jika kesempatan habis (setelah 3 kali percobaan salah), akun akan diblokir, dan program akan berhenti.
2.	PROSES PENARIKAN UANG
•  Looping Penarikan: Setelah PIN benar, program meminta pengguna memasukkan jumlah uang yang ingin ditarik.
•  Penanganan Kesalahan Input:
•	Jika pengguna memasukkan jumlah penarikan yang tidak valid (misalnya, bukan angka), program akan menampilkan pesan error dan meminta input ulang.
•  Validasi Penarikan:
•	Jika jumlah yang dimasukkan kurang dari atau sama dengan nol, program menolak dan meminta ulang input.
•	Jika jumlah yang diminta lebih besar dari saldo yang tersedia, program menampilkan pesan bahwa saldo tidak mencukupi dan meminta jumlah yang lebih kecil.
•  Jika jumlah yang diminta valid dan tidak melebihi saldo, maka saldo dikurangi dan penarikan berhasil. Sisa saldo ditampilkan, dan program berhenti.
3.	Representatif Output
Contoh Kasus Penggunaan:
1.	Pengguna diminta untuk memasukkan PIN.
o	Jika PIN benar, pengguna bisa lanjut ke proses penarikan.
o	Jika PIN salah 3 kali berturut-turut, akun diblokir, dan program berhenti.
2.	Setelah PIN benar, pengguna diminta memasukkan jumlah uang yang ingin ditarik.
o	Jika penarikan lebih besar dari saldo, program menolak dan meminta input yang lebih kecil.
o	Jika penarikan valid, penarikan dilakukan dan sisa saldo ditampilkan.


## Kesimpulan
Ringkasan dan interpretasi pandangan kalia dari hasil praktikum dan pembelajaran yang didapat[1].

## Referensi
[1] I. Holm, Narrator, and J. Fullerton-Smith, Producer, How to Build a Human [DVD]. London: BBC; 2002.
