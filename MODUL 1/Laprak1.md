![image](https://github.com/user-attachments/assets/893ba859-8995-476c-91ec-86188858584d)# <h1 align="center">Laporan Praktikum Modul Dasar-Dasar Python untuk Sains Data</h1>
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
- Looping PIN: Program akan meminta pengguna untuk memasukkan PIN hingga PIN yang dimasukkan benar atau hingga kesempatan habis.
- Jika PIN yang dimasukkan benar, program akan menampilkan pesan "PIN benar" dan keluar dari proses ini.
- Jika PIN yang dimasukkan salah, jumlah kesempatan akan berkurang, dan pengguna akan diberitahu berapa banyak kesempatan yang tersisa.
- Jika kesempatan habis (setelah 3 kali percobaan salah), akun akan diblokir, dan program akan berhenti.
2. Proses Penarikan Uang
- Looping Penarikan: Setelah PIN benar, program meminta pengguna memasukkan jumlah uang yang ingin ditarik.
- Penanganan Kesalahan Input:
- Jika pengguna memasukkan jumlah penarikan yang tidak valid (misalnya, bukan angka), program akan menampilkan pesan error dan meminta input ulang.
- Validasi Penarikan:
- Jika jumlah yang dimasukkan kurang dari atau sama dengan nol, program menolak dan meminta ulang input.
- Jika jumlah yang diminta lebih besar dari saldo yang tersedia, program menampilkan pesan bahwa saldo tidak mencukupi dan meminta jumlah yang lebih kecil.
- Jika jumlah yang diminta valid dan tidak melebihi saldo, maka saldo dikurangi dan penarikan berhasil. Sisa saldo ditampilkan, dan program berhenti.
3. Interpretasi Output:
- Pengguna diminta untuk memasukkan PIN : Jika PIN benar, pengguna bisa lanjut ke proses penarikan dan Jika PIN salah 3 kali berturut-turut, akun diblokir, dan program berhenti.
- Setelah PIN benar, pengguna diminta memasukkan jumlah uang yang ingin ditarik: Jika penarikan lebih besar dari saldo, program menolak dan meminta input yang lebih kecil dan Jika penarikan valid, penarikan dilakukan dan sisa saldo ditampilkan.

### 4. Anda diberikan file CSV berisi data nilai ujian mahasiswa. Tugas Anda adalah menulis sebuah program yang:
1. Membaca file CSV dan menyimpan datanya ke dalam dictionary.
2. Menghitung rata-rata nilai tiap mahasiswa.
3. Menampilkan mahasiswa dengan nilai tertinggi dan terendah.
   
#### Kode Program:
```python
import pandas as pd
data = pd.read_csv('siswa_nilai.csv')
rata_rata = data ['Nilai'].mean()
nilai_tertinggi = data ['Nilai'].max()
nilai_terendah = data ['Nilai'].min()

print(f"rata-rata nilai siswa: {rata_rata}")
print(f"\nMahasiswa dengan nilai rata-rata tertinggi: {nilai_tertinggi} ")
print(f"Mahasiswa dengan nilai rata-rata terendah: {nilai_terendah} ")
```


#### Output:
![image](https://github.com/user-attachments/assets/7933dd27-8fd2-4b88-a7a0-019f51d9a51c)


#### Penjelasan:
csv adalah modul Python yang digunakan untuk membaca dan menulis file CSV (Comma-Separated Values). Dalam kode ini, modul ini digunakan untuk membaca data dari file CSV yang berisi data nilai mahasiswa.
- Membuka file CSV dengan mode baca ('r').
- Menggunakan csv.reader untuk membaca baris-baris data dari file.
- next(csv_reader): Digunakan untuk melewati baris pertama (header) dari file CSV.
- Untuk setiap baris, nilai pada indeks pertama dianggap sebagai nama mahasiswa, dan nilai-nilai berikutnya dianggap sebagai nilai mata kuliah.
- map(int, baris[1:]): Mengonversi semua nilai yang merupakan string dari file CSV menjadi integer.
- Data ini kemudian dimasukkan ke dalam dictionary, di mana nama mahasiswa adalah kunci, dan nilai-nilai adalah daftar integer.
- Mengembalikan dictionary data_mahasiswa.

>> proses Run Code
- Fungsi main() bertugas untuk menjalankan program.
- Nama file CSV yang akan dibaca ditentukan dalam variabel nama_file (misalnya data_nilai_mahasiswa.csv).
- Fungsi baca_data_csv() dipanggil untuk membaca data mahasiswa dari file CSV.
- Fungsi hitung_rata_rata() dipanggil untuk menghitung rata-rata nilai setiap mahasiswa.
- Program kemudian menampilkan rata-rata nilai setiap mahasiswa.
- Fungsi cari_nilai_tertinggi_terendah() dipanggil untuk menemukan mahasiswa dengan nilai rata-rata tertinggi dan terendah, lalu hasilnya ditampilkan.

### 5. Buatlah permainan sederhana menggunakan Python, di mana komputer akan memilih sebuah angka secara acak antara 1 hingga 100, dan pengguna harus menebak angka tersebut. Setiap tebakan yang salah akan memberikan petunjuk apakah angka yang ditebak lebih besar atau lebih kecil dari angka sebenarnya. Batasi jumlah percobaan menjadi 5 kali. Setelah permainan selesai, tampilkan apakah pemain menang atau kalah.
#### Kode Program:
```python
# import modul untuk menyediakan fungsi yang menghasilkan angka acak
import random

# Fungsi tebak_angka()
def tebak_angka():
    angka_rahasia = random.randint(1, 100)  # Komputer memilih angka acak antara 1 dan 100
    kesempatan = 5  # Pengguna memiliki 5 kesempatan

# Pesan Selamat Datang
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih angka antara 1 hingga 100.")
    print(f"Anda memiliki {kesempatan} kali percobaan untuk menebak angka tersebut.")

    # Mulai loop untuk 5 percobaan/proses menebak angka
    for percobaan in range(1, kesempatan + 1):
        try:
            tebakan = int(input(f"Tebakan {percobaan}: Masukkan angka tebakan Anda: "))

            if tebakan < 1 or tebakan > 100:    # validasi input
                print("Angka harus antara 1 hingga 100. Coba lagi.")
                continue

            if tebakan == angka_rahasia:    # Membandingkan Tebakan dengan Angka Rahasia
                print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
                break
            elif tebakan < angka_rahasia:
                print("Tebakan Anda terlalu kecil.")
            else:
                print("Tebakan Anda terlalu besar.")

        except ValueError:    # Penanganan Error Input
            print("Input tidak valid. Masukkan angka yang benar.")
            continue

    else:
        # Jika tidak menebak dengan benar dalam 5 kali percobaan
        print(f"Maaf, Anda kehabisan kesempatan. Angka yang benar adalah {angka_rahasia}.")

# Menjalankan permainan/memanggil fungsi tebak_angka() untuk memulai
tebak_angka()
```
#### Output:
![image](https://github.com/user-attachments/assets/1b9c0728-b783-4fa3-9648-e915636b666e)

#### Penjelasan:
random adalah modul yang menyediakan fungsi untuk menghasilkan angka acak. Di sini, digunakan untuk memilih angka rahasia yang harus ditebak oleh pengguna.
1.	Proses menebak angka
•	•  Looping Percobaan: Program menggunakan for loop untuk memberi pengguna 5 kesempatan. Setiap loop mewakili satu percobaan.
•	•  Program meminta pengguna untuk memasukkan angka tebakan, yang akan dikonversi menjadi integer menggunakan int(input()).
•	•  try-except block digunakan untuk menangani jika input yang diberikan bukan angka, sehingga mencegah error.
2. Membandingkan tebakan dengan angka rahasia
•  Jika tebakan pengguna tepat (sama dengan angka rahasia), program menampilkan pesan kemenangan dan keluar dari loop menggunakan break.
•  Jika tebakan pengguna terlalu kecil, program menampilkan pesan "Tebakan Anda terlalu kecil".
•  Jika tebakan pengguna terlalu besar, program menampilkan pesan "Tebakan Anda terlalu besar".
3. Interpretasi atau alur permainan
•  Komputer memilih angka rahasia, misalnya 55.
•  Pengguna diminta menebak angka, misalnya menebak 30.
    o	Program memberi tahu bahwa tebakan terlalu kecil.
•  Pengguna menebak lagi, misalnya 60.
    o	Program memberi tahu bahwa tebakan terlalu besar.
4.	Pengguna menebak angka 55.
    o	Program memberi tahu bahwa tebakan benar, dan pengguna menang dan Jika pengguna tidak berhasil menebak dalam 5 percobaan, program akan memberi tahu angka yang benar.

### 5. Buat fungsi rekursif yang menerima input bilangan bulat `n` dan menghasilkan urutan bilangan seperti berikut ini:
```
Input: n = 4
Output: 1, 1, 2, 6, 24
```
Dan Fungsi ini harus menggunakan konsep rekursi untuk menghitung faktorial setiap angka hingga `n`.
#### Kode Program:
```python
# Fungsi rekursif untuk menghitung faktorial dari bilangan n
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Fungsi rekursif untuk menghasilkan deret faktorial dari 0 hingga n
def deret_faktorial(n):
    if n == 0:
        return [1]  # Basis kasus: faktorial dari 0 adalah 1
    else:
        deret_sebelumnya = deret_faktorial(n - 1)  # Rekursi
        deret_sebelumnya.append(faktorial(n))  # Tambahkan faktorial n ke deret
        return deret_sebelumnya

# Tes fungsi
n = 4
hasil = deret_faktorial(n)
print("Output:", ", ".join(map(str, hasil)))
```
#### Output:
![image](https://github.com/user-attachments/assets/e4c34982-3a73-4d55-a1d4-9aeb385c46d1)

#### Penjelasan:
Dalam kode program ini ada dua fungsi utama:
1.	Fungsi faktorial(n): Menghitung faktorial dari suatu bilangan menggunakan rekursi.
2.	Fungsi deret_faktorial(n): Menghasilkan deret faktorial dari 0 hingga n menggunakan rekursi, dengan memanfaatkan fungsi faktorial().
Faktorial dari suatu bilangan nnn adalah hasil perkalian semua bilangan bulat positif dari 1 hingga nnn. Sebagai contoh, faktorial dari 4 (ditulis sebagai 4!) adalah 4×3×2×1=244 \times 3 \times 2 \times 1 = 244×3×2×1=24.
Fungsi_faktorial(n):
•	Tujuan Fungsi: Menghitung faktorial dari bilangan nnn.
•	Cara Kerja:
o	Fungsi ini menggunakan konsep rekursi, yaitu memanggil dirinya sendiri hingga mencapai kondisi dasar.
o	Kondisi dasar: Jika nnn adalah 0 atau 1, fungsi langsung mengembalikan nilai 1, karena faktorial dari 0 dan 1 adalah 1.
o	Langkah rekursif: Jika n>1n > 1n>1, fungsi mengalikan nnn dengan hasil faktorial dari n−1n-1n−1 (yaitu memanggil dirinya sendiri dengan nilai n−1n-1n−1).
Contoh untuk menghitung faktorial 4:
•	faktorial(4) = 4 * faktorial(3) = 4 * 3 * faktorial(2) = 4 * 3 * 2 * faktorial(1) = 4 * 3 * 2 * 1 = 24.
Fungsi deret_faktorial(n):
•	Tujuan Fungsi: Menghasilkan sebuah deret/list yang berisi nilai faktorial dari angka 0 hingga nnn.
•	Cara Kerja:
o	Fungsi ini juga menggunakan rekursi.
o	Kondisi dasar: Jika n=0n = 0n=0, maka fungsi mengembalikan list berisi nilai [1], karena faktorial 0 adalah 1.
o	Langkah rekursif: Jika n>0n > 0n>0, fungsi akan memanggil dirinya sendiri untuk menghasilkan deret faktorial hingga n−1n-1n−1. Setelah deret sebelumnya (dari 0 hingga n−1n-1n−1) selesai dihitung, fungsi menambahkan hasil faktorial nnn ke dalam list.
Contoh untuk menghasilkan deret faktorial dari 0 hingga 4:
•	deret_faktorial(4):
o	Memanggil deret_faktorial(3): Menghasilkan deret dari 0 hingga 3.
o	Memanggil deret_faktorial(2): Menghasilkan deret dari 0 hingga 2.
o	Memanggil deret_faktorial(1): Menghasilkan deret dari 0 hingga 1.
o	Memanggil deret_faktorial(0): Menghasilkan [1] (basis kasus).
o	Lalu, pada setiap langkah rekursi, hasil faktorial masing-masing nnn (dihitung menggunakan fungsi faktorial()) ditambahkan ke dalam list:
	Pada n=1n = 1n=1, hasilnya [1, 1].
	Pada n=2n = 2n=2, hasilnya [1, 1, 2].
	Pada n=3n = 3n=3, hasilnya [1, 1, 2, 6].
	Pada n=4n = 4n=4, hasilnya [1, 1, 2, 6, 24].
MENJALANKAN PROGRAM
•  n = 4 berarti kita ingin menghitung deret faktorial dari 0 hingga 4.
•  Fungsi deret_faktorial(n) akan menghasilkan deret [1, 1, 2, 6, 24], yang kemudian dicetak sebagai string dengan pemisah koma.
•  Program menghasilkan output deret faktorial dari 0 hingga 4


## Kesimpulan
Ringkasan dan interpretasi pandangan kalia dari hasil praktikum dan pembelajaran yang didapat[1].

## Referensi
[1] I. Holm, Narrator, and J. Fullerton-Smith, Producer, How to Build a Human [DVD]. London: BBC; 2002.
