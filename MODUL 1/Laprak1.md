<h1 align="center">Laporan Praktikum Modul Dasar-Dasar Python untuk Sains Data</h1>
<p align="center">Khulika Malkan</p>
<p align="center">2311110057</p>
<p align="center">S1SD0-02</p>

## Dasar Teori
Python  adalah  bahasa  pemrograman  yang  menggunakan  interpreter untuk     menjalankan     kode     programnya.     Interpreter     tersebut     dapat menerjemahkan  kode  secara  langsung,  dan  Python  dapat  dijalankan  di berbagai platform seperti Windows, Linux, dan lain-lain. Pythonmengadopsi paradigma  pemrograman  dari  beberapa  bahasa  lain,  termasuk  paradigma pemrograman  prosedural  seperti  bahasa  C,  pemrograman  berorientasi  objek seperti  Java,  dan  bahasa  fungsional  seperti  Lisp.  Kombinasi  paradigma  ini memudahkan  para  programmer  dalam  mengembangkan  berbagai  proyek menggunakan Python [1].
### Variabel dan Tipe Data
Sebuah variabel dapat memiliki nama pendek (seperti x dan y) atau nama yang lebih deskriptif (umur, namalengkap, total_volume).
Aturan untuk penulisanan variabel Python:
- Nama variabel harus dimulai dengan huruf atau karakter garis bawah
- Nama variabel tidak boleh dimulai dengan angka
- Nama variabel hanya boleh berisi karakter alfanumerik dan garis bawah (Az, 0-9, dan _ )
- Nama variabel membedakan antara huruf besar/kecil (usia, Usia, dan USIA adalah tiga variabel berbeda). [2]
>> beberapa tipe data yang umum dalam bahasa pemrograman Python:
- int (Integer): Tipe data untuk bilangan bulat, misalnya: 10, -3, 129.
- float: Tipe data untuk bilangan desimal (pecahan), misalnya: 3.14, 0.5, -7.8.
- str (String): Tipe data untuk teks atau kumpulan karakter, misalnya: "Halo", 'Python'.
- bool (Boolean): Tipe data yang hanya memiliki dua nilai, yaitu True atau False.
- list: Tipe data untuk menyimpan kumpulan nilai dalam bentuk daftar, misalnya: [1, 2, 3], ['a', 'b', 'c'].
- tuple: Mirip dengan list, tapi bersifat immutable (tidak dapat diubah), misalnya: (1, 2, 3).
- dict (Dictionary): Tipe data yang menyimpan pasangan kunci-nilai (key-value pairs), misalnya: {"nama": "Ali", "umur": 25}.
- set: Kumpulan data yang tidak berurutan dan tidak memiliki elemen yang sama (unik), misalnya: {1, 2, 3}, {3, 4, 5}.
- NoneType: Tipe data khusus yang hanya memiliki nilai None, biasanya digunakan untuk merepresentasikan ketiadaan nilai.

  
### Percabangan (If-Else)
Pemilihan  (selection),  yaitu  instruksi  yang dikerjakan berdasarkan kondisi tertentu atau syarat tertentu dimana  suatu  kondisi atau syarat  tersebut dapat   bernilai   benar   atau   salah.   Intruksi   akan dilaksanakan manakala kondisi atau syarat bernilai benar,  dan  suatu  instruksi  tidak  akan  dikerjakan apabila kondisi atau syarat tidak terpenuhi.Pemilihan atau percabangan  menggunakan statemen   If,   If/Else,   If/Elif/Else.   Statemen   If digunakan   saatter  dapat  satu  pilihan,   statemen If/Else   digunakan   saatter   dapat   dua   pilihan, statemen  If/Elif/Else  digunakan  apabila  terapat lebih  dari  dua  pilihan [3].


  
### Perulangan (Loops)
![image](https://github.com/user-attachments/assets/f22675c5-8d8a-4f3e-b0c1-35f24f18c686)

- sumber : https://repository.penerbiteureka.com/id/publications/560015/fundamental-bahasa-pemrograman-python
  
Untuk  memenuhi  kebutuhan  perulangan  perintahpada bahasa  pemrograman  Python.Terdapat  3  pilihanloop.  Secara teknik  fungsionalitas  dasar  3  pilihanloop  ini  adalah  sama, meskipun  sintaks  dan jumlah  waktu  yang  diperlukan  untuk memeriksa kondisinya berbeda.

### Fungsi (Functions)
Fungsi (functions) dalam Python adalah blok kode yang dirancang untuk menjalankan tugas tertentu dan dapat dipanggil berulang kali. Fungsi digunakan untuk mengorganisasi kode agar lebih modular, mudah dipelihara, dan dapat digunakan kembali. Fungsi didefinisikan menggunakan kata kunci def diikuti dengan nama fungsi, tanda kurung (), dan tanda titik dua :. Di dalam tanda kurung, fungsi dapat menerima argumen, dan setelahnya diikuti oleh blok kode yang menjadi isi fungsi. 

### List dan Tuple
- List adalah seperti daftar yang fleksibel. Kamu bisa menambah, menghapus, atau mengganti item sesukamu. Misalnya, saat kamu pergi ke pasar dan teringat butuh membeli telur selain apel dan pisang, kamu bisa dengan mudah menambahkannya ke dalam List. List didefinisikan dengan menggunakan tanda kurung siku [], dan di dalamnya kamu bisa menyimpan berbagai macam jenis data seperti angka, teks, atau bahkan List lain.
- Tuple, di sisi lain, adalah seperti daftar yang tidak bisa diubah. Setelah kamu membuatnya, kamu tidak bisa menambah, menghapus, atau mengganti item di dalamnya. Bayangkan kamu punya daftar hari dalam seminggu: hari Senin sampai Minggu tidak pernah berubah, jadi kamu bisa menggunakan Tuple. Ini membantu memastikan bahwa data tersebut tetap sama dan tidak ada yang bisa mengubahnya tanpa disengaja. Tuple didefinisikan dengan tanda kurung biasa ().

### Dictionary
Dictionary dalam Python adalah struktur data yang digunakan untuk menyimpan pasangan kunci (key) dan nilai (value). Setiap item dalam dictionary terdiri dari dua bagian: kunci dan nilai yang terkait dengan kunci tersebut. Dictionary sangat berguna saat kamu ingin mengaitkan satu data dengan data lainnya, mirip seperti kamus yang menghubungkan kata (kunci) dengan definisinya (nilai).

### Set
Set dalam Python adalah tipe data yang digunakan untuk menyimpan sekumpulan item yang unik dan tidak berurutan. Set mirip dengan himpunan dalam matematika, di mana setiap elemen hanya muncul satu kali dan urutannya tidak penting. Set sangat berguna jika kamu ingin menyimpan data tanpa duplikasi dan tidak peduli dengan urutannya.

### File Handling
File Handling dalam Python adalah cara untuk membaca dari, menulis ke, dan memanipulasi file yang tersimpan di komputer. File handling memungkinkan kita menyimpan data secara permanen dan mengaksesnya kembali di kemudian hari. Python menyediakan fungsi-fungsi bawaan untuk bekerja dengan file, sehingga kita dapat membuka, membaca, menulis, dan menutup file dengan mudah.

### List Comprehension
List Comprehension dalam Python adalah untuk membuat atau memodifikasi list. List comprehension memungkinkan kita untuk menulis loop dan kondisi untuk menghasilkan list baru dalam satu baris kode, menjadikannya lebih ringkas dan mudah dibaca dibandingkan dengan cara tradisional menggunakan loop for.

### Exception Handling
Exception Handling dalam Python adalah mekanisme untuk menangani kesalahan atau exception yang terjadi saat program dijalankan. Exception adalah situasi di mana ada sesuatu yang salah saat program dijalankan, seperti pembagian dengan nol, mencoba membuka file yang tidak ada, atau mengakses indeks list yang tidak valid. Dengan exception handling, kamu dapat menangkap dan menangani kesalahan ini sehingga program tidak berhenti secara tiba-tiba dan dapat terus berjalan atau memberikan pesan error yang lebih informatif.

### OOP (Object-Oriented Programming)
OOP (Object-Oriented Programming) atau Pemrograman Berbasis Objek adalah paradigma pemrograman yang berfokus pada objek dan penggunaan konsep seperti kelas (class), objek (object), pewarisan (inheritance), enkapsulasi (encapsulation), dan polimorfisme (polymorphism) untuk membangun program. Dalam OOP, data dan fungsi yang memanipulasi data dikelompokkan bersama dalam unit yang disebut objek, yang dibuat berdasarkan blueprint yang disebut kelas.



### Modules dan Packages
Modules dan Packages dalam Python adalah cara untuk mengorganisir dan mengelola kode, memungkinkan pengembang untuk membuat aplikasi yang lebih besar dan terstruktur dengan baik. Modul adalah file Python yang berisi kode, seperti fungsi, kelas, dan variabel, yang dapat digunakan kembali di program lain. Modul membantu dalam menyusun kode agar lebih terorganisir dan lebih mudah dibaca. Untuk membuat modul, cukup buat file dengan ekstensi .py. Misalnya, jika kamu memiliki file bernama matematika.py, maka ini adalah modul yang berisi fungsi-fungsi matematika.

### Lambda dan Higher-Order Functions
Lambda Functions dan Higher-Order Functions adalah dua konsep penting dalam pemrograman fungsional di Python. Keduanya memungkinkan kamu untuk menulis kode yang lebih ringkas, efisien, dan fleksibel. 
- Lambda Functions: fungsi anonim (tanpa nama) yang didefinisikan dengan menggunakan kata kunci lambda. Fungsi ini biasanya digunakan untuk menulis fungsi kecil yang hanya digunakan sekali atau untuk fungsi yang tidak memerlukan penamaan.
- Higher-Order Functions: fungsi yang dapat menerima fungsi lain sebagai argumen atau mengembalikan fungsi sebagai hasil. Ini memungkinkan kamu untuk membuat fungsi yang lebih fleksibel dan dapat digunakan kembali.


### Miscellaneous
Dalam konteks pemrograman Python, miscellaneous mengacu pada berbagai topik atau konsep yang tidak termasuk dalam kategori utama seperti tipe data, kontrol alur, atau pemrograman berorientasi objek, tetapi tetap penting untuk dipahami. Berikut adalah beberapa topik miscellaneous yang sering ditemui dalam pemrograman Python:
- List Comprehensions: adalah cara singkat untuk membuat list baru dengan cara yang lebih elegan. Ini adalah sintaks yang lebih ringkas dibandingkan menggunakan loop untuk menambahkan elemen ke dalam list.
- Fungsi Built-in Python memiliki banyak fungsi built-in yang dapat digunakan langsung tanpa perlu mendefinisikannya. Beberapa contoh fungsi built-in adalah:
  - len(): Menghitung panjang suatu objek.
  - sum(): Menjumlahkan semua elemen dalam iterable.
  - max(): Mengembalikan nilai maksimum dari iterable.
- Exception Handling: memungkinkan program untuk menangani kesalahan yang terjadi saat runtime. Dengan menggunakan try, except, else, dan finally, kita dapat menangani situasi tak terduga tanpa menghentikan eksekusi program.
- Decorators: cara untuk memodifikasi atau meningkatkan fungsi atau metode tanpa mengubah strukturnya. Ini sangat berguna untuk menambah fungsionalitas seperti logging, akses kontrol, dan caching.
- Generators: cara untuk membuat iterator dengan menggunakan yield. Fungsi generator akan mengembalikan nilai satu per satu, memungkinkan penggunaan memori yang lebih efisien.
- Modul dan Paket: adalah file Python yang berisi definisi fungsi dan variabel, sedangkan paket adalah kumpulan modul dalam direktori. Modul dan paket membantu dalam mengorganisir kode.
- Context Managers: digunakan untuk mengelola sumber daya seperti file, memastikan bahwa sumber daya dibersihkan dengan benar setelah digunakan. Hal ini sering dilakukan menggunakan with statement.
- Type hinting memperkenalkan anotasi tipe pada fungsi dan variabel, membantu dalam dokumentasi dan pemeriksaan tipe.
- F-strings adalah cara untuk melakukan interpolasi string yang lebih mudah dan lebih cepat menggunakan awalan f sebelum string.
- List, Set, dan Dictionary Comprehensions Seperti list comprehensions, kita juga dapat membuat set dan dictionary dengan cara yang mirip.

# Guided 
## 1. Variabel
```python
nama = "Yanto"
umur = 38
print(f"Nama : {nama} \nUmur : {umur}")
```
### Kode Program
![image](https://github.com/user-attachments/assets/df9ee3dc-6fbe-43f7-b62f-13202488d30d)
Kode program di atas mendeklarasikan dua variabel, yaitu nama yang menyimpan string "Yanto" dan umur yang menyimpan angka 38. Kemudian, fungsi print() digunakan dengan format string (f-string) untuk mencetak teks yang menyisipkan nilai dari kedua variabel tersebut. Dalam hal ini, {nama} di dalam string akan digantikan oleh nilai "Yanto", dan {umur} akan digantikan oleh nilai 38. Karakter \n berfungsi untuk membuat baris baru sehingga teks "Umur : 38" dicetak di baris selanjutnya. Hasil dari program ini adalah menampilkan informasi nama dan umur secara rapi sebagai output, yaitu: "Nama : Yanto" diikuti dengan "Umur : 38" pada baris berikutnya.
### Output
![image](https://github.com/user-attachments/assets/922a46c9-214a-49be-ac9b-710e77dacaad)

## 2. Variabel
```python
from math import pi

jari = 8
luas = pi *jari**2
keliling = 2*pi*jari
print(f"Luas Lingkaran : {luas} \nKeliling Lingkaran : {keliling}")
```
### Kode Program
![image](https://github.com/user-attachments/assets/79dfe230-95e7-4620-b8c7-d4958ac1d69a)
Kode program di atas menghitung luas dan keliling sebuah lingkaran dengan jari-jari 8 menggunakan modul math dari Python untuk mengakses nilai konstanta π (pi). Variabel jari menyimpan nilai 8 sebagai panjang jari-jari lingkaran. Luas lingkaran dihitung dengan rumus π * jari² dan disimpan dalam variabel luas, sedangkan keliling lingkaran dihitung dengan rumus 2 * π * jari dan disimpan dalam variabel keliling. Fungsi print() kemudian mencetak hasil perhitungan luas dan keliling tersebut menggunakan format string (f-string), sehingga outputnya menampilkan luas dan keliling lingkaran dalam dua baris, yaitu "Luas Lingkaran" dan "Keliling Lingkaran".
### Output
![image](https://github.com/user-attachments/assets/f54b2d18-af8e-4796-9bbe-3ae767ebf52e)

## 3. Variabel
```python
angka = 129
teks = 'ini angka'
print(f"Tipe Data Angka : {type(angka)} \nTipe Data Teks : {type(teks)}")
```
### Kode Program
![image](https://github.com/user-attachments/assets/25dd9988-6206-4c1c-80c7-75075c175ae8)
Kode program di atas mendefinisikan dua variabel, yaitu angka yang menyimpan nilai integer 129 dan teks yang menyimpan string 'ini angka'. Kemudian, fungsi print() digunakan bersama format string (f-string) untuk menampilkan tipe data dari kedua variabel tersebut menggunakan fungsi type(). Fungsi type() mengembalikan tipe data dari objek yang diberikan, dalam hal ini type(angka) akan mengembalikan <class 'int'> untuk tipe integer, dan type(teks) akan mengembalikan <class 'str'> untuk tipe string. Hasilnya, output akan menampilkan tipe data masing-masing variabel dalam dua baris, yaitu "Tipe Data Angka: <class 'int'>" dan "Tipe Data Teks: <class 'str'>".
### Output
![image](https://github.com/user-attachments/assets/9dc40e1c-6019-4b48-9620-d07f7da3e797)




# Unguided 

## 1. Buatlah program yang dapat menghasilkan pola berbentuk angka seperti di bawah ini, dengan syarat angka yang ditampilkan adalah hasil dari penjumlahan bilangan prima sebelumnya dan Jumlah angka pada setiap baris bertambah 1, dan bilangan yang ditampilkan adalah bilangan prima.
```
1
2 3
5 7 11
13 17 19 23
```
### Kode Program:
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
### Output:
![image](https://github.com/user-attachments/assets/25eefb8f-e30e-4703-9eb0-85a757580bdf)

### Penjelasan:
Kode di atas menggunakan fungsi is_prime(num) untuk mengecek apakah bilangan adalah bilangan prima
- Tujuan Fungsi: Fungsi ini digunakan untuk memeriksa apakah suatu bilangan num merupakan bilangan prima atau tidak.
- Langkah-langkah:
- Baris if num < 2:: Jika bilangan lebih kecil dari 2, langsung dikembalikan False karena bilangan prima dimulai dari 2.
- Baris for i in range(2, int(num**0.5) + 1):: Untuk bilangan num yang lebih besar dari 1, kita melakukan perulangan dari 2 sampai akar kuadrat dari num. Kita hanya perlu memeriksa faktor hingga akar kuadratnya karena faktor di atasnya sudah pasti simetris dengan yang ada di bawah akar kuadrat.
- Baris if num % i == 0:: Jika ada angka i yang membagi num secara sempurna (tanpa sisa), maka bilangan tersebut bukan bilangan prima, sehingga dikembalikan False.
- Baris return True:: Jika tidak ada angka yang dapat membagi num, bilangan tersebut adalah bilangan prima, maka fungsi mengembalikan True.

## 2. Buatlah sebuah fungsi yang menerima dua input berupa list angka. Fungsi ini harus mengembalikan sebuah list baru yang berisi elemen dari dua list input yang memiliki indeks ganjil. List baru tersebut juga harus diurutkan secara menurun berdasarkan nilai elemen.
### kode program:
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
### Output:
![image](https://github.com/user-attachments/assets/883b1867-a66f-41ea-ae5a-fec3aad6358b)

### penjelasan:
kode ini membuat Fungsi: ambil_ganjil_dan_urutkan(list1, list2)
Fungsi ini memiliki dua daftar input, list1 dan list2. Tugas dari fungsi ini adalah:
- Mengambil elemen-elemen yang berada di indeks ganjil dari kedua daftar.
- Menggabungkan elemen-elemen tersebut menjadi satu daftar.
- Mengurutkan hasil gabungan tadi secara menurun (dari yang terbesar ke yang terkecil).
- Mengembalikan hasil akhir berupa daftar elemen yang sudah diurutkan.

## 3. Buat sebuah program untuk mensimulasikan transaksi ATM. Program harus: 
1. Meminta pengguna memasukkan PIN (dibatasi 3 kali percobaan).
2. Setelah PIN benar, meminta jumlah penarikan.
3. Jika saldo kurang dari jumlah yang ditarik, munculkan pesan kesalahan.
4. Jika penarikan berhasil, tampilkan saldo akhir.
### kode program:
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
### Output:
![image](https://github.com/user-attachments/assets/67226bb9-41c6-4224-8bef-a128658392b0)


### Penjelasan:
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

## 4. Anda diberikan file CSV berisi data nilai ujian mahasiswa. Tugas Anda adalah menulis sebuah program yang:
1. Membaca file CSV dan menyimpan datanya ke dalam dictionary.
2. Menghitung rata-rata nilai tiap mahasiswa.
3. Menampilkan mahasiswa dengan nilai tertinggi dan terendah.
   
### Kode Program:
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


### Output:
![image](https://github.com/user-attachments/assets/7933dd27-8fd2-4b88-a7a0-019f51d9a51c)


### Penjelasan:
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

## 5. Buatlah permainan sederhana menggunakan Python, di mana komputer akan memilih sebuah angka secara acak antara 1 hingga 100, dan pengguna harus menebak angka tersebut. Setiap tebakan yang salah akan memberikan petunjuk apakah angka yang ditebak lebih besar atau lebih kecil dari angka sebenarnya. Batasi jumlah percobaan menjadi 5 kali. Setelah permainan selesai, tampilkan apakah pemain menang atau kalah.
### Kode Program:
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
### Output:
![image](https://github.com/user-attachments/assets/1b9c0728-b783-4fa3-9648-e915636b666e)

### Penjelasan:
random adalah modul yang menyediakan fungsi untuk menghasilkan angka acak. Di sini, digunakan untuk memilih angka rahasia yang harus ditebak oleh pengguna.
1.	Proses menebak angka
- Looping Percobaan: Program menggunakan for loop untuk memberi pengguna 5 kesempatan. Setiap loop mewakili satu percobaan.
- Program meminta pengguna untuk memasukkan angka tebakan, yang akan dikonversi menjadi integer menggunakan int(input()).
- try-except block digunakan untuk menangani jika input yang diberikan bukan angka, sehingga mencegah error.
  
2. Membandingkan tebakan dengan angka rahasia
- Jika tebakan pengguna tepat (sama dengan angka rahasia), program menampilkan pesan kemenangan dan keluar dari loop menggunakan break.
- Jika tebakan pengguna terlalu kecil, program menampilkan pesan "Tebakan Anda terlalu kecil".
- Jika tebakan pengguna terlalu besar, program menampilkan pesan "Tebakan Anda terlalu besar".
  
3. Interpretasi atau alur permainan
- Komputer memilih angka rahasia, misalnya 55.
- Pengguna diminta menebak angka, misalnya menebak 30: Program memberi tahu bahwa tebakan terlalu kecil.
- Pengguna menebak lagi, misalnya 60: Program memberi tahu bahwa tebakan terlalu besar.
- Pengguna menebak angka 55 : Program memberi tahu bahwa tebakan benar, dan pengguna menang dan Jika pengguna tidak berhasil menebak dalam 5 percobaan, program akan memberi tahu angka yang benar.

## 6. Buat fungsi rekursif yang menerima input bilangan bulat `n` dan menghasilkan urutan bilangan seperti berikut ini:
```
Input: n = 4
Output: 1, 1, 2, 6, 24
```
Dan Fungsi ini harus menggunakan konsep rekursi untuk menghitung faktorial setiap angka hingga `n`.
### Kode Program:
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
### Output:
![image](https://github.com/user-attachments/assets/e4c34982-3a73-4d55-a1d4-9aeb385c46d1)

### Penjelasan:
Dalam kode program ini ada dua fungsi utama:
1.	Fungsi faktorial(n): Menghitung faktorial dari suatu bilangan menggunakan rekursi.
2.	Fungsi deret_faktorial(n): Menghasilkan deret faktorial dari 0 hingga n menggunakan rekursi, dengan memanfaatkan fungsi faktorial().
Faktorial dari suatu bilangan nnn adalah hasil perkalian semua bilangan bulat positif dari 1 hingga nnn. Sebagai contoh, faktorial dari 4 (ditulis sebagai 4!) adalah 4×3×2×1=244 \times 3 \times 2 \times 1 = 244×3×2×1=24.
**Fungsi_faktorial(n):**
- Tujuan Fungsi: Menghitung faktorial dari bilangan nnn.
- Cara Kerja:
  - Fungsi ini menggunakan konsep rekursi, yaitu memanggil dirinya sendiri hingga mencapai kondisi dasar.
  - Kondisi dasar: Jika nnn adalah 0 atau 1, fungsi langsung mengembalikan nilai 1, karena faktorial dari 0 dan 1 adalah 1.
  - Langkah rekursif: Jika n>1n > 1n>1, fungsi mengalikan nnn dengan hasil faktorial dari n−1n-1n−1 (yaitu memanggil dirinya sendiri dengan nilai n−1n-1n−1).
  - Contoh untuk menghitung faktorial 4: faktorial(4) = 4 * faktorial(3) = 4 * 3 * faktorial(2) = 4 * 3 * 2 * faktorial(1) = 4 * 3 * 2 * 1 = 24.
- Fungsi deret_faktorial(n): Menghasilkan sebuah deret/list yang berisi nilai faktorial dari angka 0 hingga nnn.
- Cara Kerja:
    - Fungsi ini juga menggunakan rekursi.
    - Kondisi dasar: Jika n=0n = 0n=0, maka fungsi mengembalikan list berisi nilai [1], karena faktorial 0 adalah 1.
    - Langkah rekursif: Jika n>0n > 0n>0, fungsi akan memanggil dirinya sendiri untuk menghasilkan deret faktorial hingga n−1n-1n−1. Setelah deret sebelumnya (dari 0 hingga n−1n-1n−1) selesai dihitung, fungsi menambahkan hasil faktorial nnn ke dalam list.
Contoh untuk menghasilkan deret faktorial dari 0 hingga 4: deret_faktorial(4):
- Memanggil deret_faktorial(3): Menghasilkan deret dari 0 hingga 3.
- Memanggil deret_faktorial(2): Menghasilkan deret dari 0 hingga 2.
- Memanggil deret_faktorial(1): Menghasilkan deret dari 0 hingga 1.
- Memanggil deret_faktorial(0): Menghasilkan [1] (basis kasus).

>> Lalu, pada setiap langkah rekursi, hasil faktorial masing-masing nnn (dihitung menggunakan fungsi faktorial()) ditambahkan ke dalam list:
- Pada n=1n = 1n=1, hasilnya [1, 1].
- Pada n=2n = 2n=2, hasilnya [1, 1, 2].
- Pada n=3n = 3n=3, hasilnya [1, 1, 2, 6].
- Pada n=4n = 4n=4, hasilnya [1, 1, 2, 6, 24].
>> Contoh Menjalankan Program
- n = 4 berarti kita ingin menghitung deret faktorial dari 0 hingga 4.
- Fungsi deret_faktorial(n) akan menghasilkan deret [1, 1, 2, 6, 24], yang kemudian dicetak sebagai string dengan pemisah koma.
- Program menghasilkan output deret faktorial dari 0 hingga 4


## 7. Buatlah program untuk memecahkan masalah "minimum coin change". Diberikan jumlah uang dan daftar nilai koin yang tersedia (misalnya, 1, 5, 10, 25), tentukan kombinasi minimum koin yang diperlukan untuk mencapai jumlah uang tersebut. Namun, program Anda harus bisa menangani koin-koin yang nilai dan jumlahnya ditentukan pengguna.
```python
def minimum_coin_change(total, koin_tersedia):
    # Mengurutkan koin dari yang terbesar ke terkecil
    koin_tersedia.sort(reverse=True)

# Menginisialisasi variabel hasil dan sisa uang
    hasil = {}
    sisa_uang = total

# Menghitung jumlah koin yang bisa digunakan untuk tiap denominasi:
    for koin in koin_tersedia:
        if sisa_uang >= koin:
            jumlah_koin = sisa_uang // koin  # Berapa banyak koin ini bisa digunakan
            sisa_uang = sisa_uang % koin  # Sisa uang yang belum dibayar
            hasil[koin] = jumlah_koin  # Simpan hasil ke dictionary

    # Jika sisa_uang masih lebih besar dari 0, berarti kombinasi koin tidak dapat mencapai jumlah yang diinginkan
    if sisa_uang > 0:
        print(f"Jumlah uang {total} tidak bisa dicapai dengan kombinasi koin yang tersedia.")
   # Menampilkan kombinasi koin yang digunakan
    else:
        print(f"Kombinasi minimum untuk mencapai {total}:")
        for koin, jumlah in hasil.items():
            print(f"Koin {koin}: {jumlah} koin")

# Fungsi utama untuk input dari pengguna
def main():
    try:
        total_uang = int(input("Masukkan jumlah uang yang ingin dicapai: "))
        koin_tersedia = list(map(int, input("Masukkan nilai koin yang tersedia (pisahkan dengan spasi): ").split()))

        # Memanggil fungsi untuk menghitung kombinasi minimum koin
        minimum_coin_change(total_uang, koin_tersedia)

    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka yang benar.")

# Menjalankan program
main()
```
### Output:
![image](https://github.com/user-attachments/assets/6cb3b3b0-b548-48ee-a8c4-51f6c95d1e86)

### Penjelasan:
1.	Mengurutkan koin dari yang terbesar ke terkecil
- Program mengurutkan nilai koin dari yang terbesar ke yang terkecil, karena dengan menggunakan koin yang lebih besar terlebih dahulu, kita bisa mengurangi jumlah koin yang dibutuhkan.
- Misalnya, jika kita punya koin 25, 10, dan 1, maka lebih efisien menggunakan koin 25 dulu daripada menggunakan koin 1 atau 10.
  
2. Menginisialisasi variabel hasil dan sisa uang
- hasil adalah dictionary (kamus) yang akan menyimpan berapa banyak setiap jenis koin yang digunakan.
- sisa_uang adalah variabel yang menyimpan sisa uang yang belum dibayar dengan koin. Pada awalnya, sisa uang sama dengan jumlah uang yang ingin dicapai (total).

3. Menghitung jumlah koin yang bisa digunakan untuk tiap denominasi
- Program melakukan iterasi melalui setiap koin dalam koin_tersedia.
- sisa_uang // koin menghitung berapa banyak koin tersebut yang bisa digunakan. Misalnya, jika kita punya sisa 87 dan koin 25, maka kita bisa menggunakan 3 koin 25 (karena 87//25=387 // 25 = 387//25=3).
- sisa_uang % koin menghitung sisa uang setelah menggunakan koin tersebut. Misalnya, 87%25=1287 \% 25 = 1287%25=12, jadi setelah menggunakan 3 koin 25, sisa uangnya adalah 12.
- hasil[koin] = jumlah_koin menyimpan jumlah koin yang digunakan dalam dictionary hasil.
  
4. Memeriksa apakah jumlah uang bisa dicapai:
- Jika setelah semua koin digunakan masih ada sisa uang yang belum bisa dibayar (sisa_uang > 0), program akan menampilkan pesan bahwa jumlah uang tidak bisa dicapai dengan koin yang ada.

5. Menampilkan kombinasi koin yang digunakan:
- Jika sisa_uang menjadi 0 (artinya uang sudah bisa dibayar sepenuhnya dengan koin yang tersedia), program akan menampilkan kombinasi minimum koin yang digunakan.

6. Penjelasan Fungsi main():
- Input dari pengguna: Program meminta pengguna memasukkan jumlah uang yang ingin dicapai dan nilai koin yang tersedia. Pengguna harus memasukkan nilai koin dipisahkan dengan spasi.
- Menangani kesalahan input: Penggunaan try-except untuk menangani kemungkinan kesalahan input, seperti ketika pengguna memasukkan nilai yang bukan angka. Jika terjadi kesalahan input, program akan menampilkan pesan "Input tidak valid".
  
Cara Kerja Program:
1.	Program meminta pengguna untuk memasukkan jumlah uang dan nilai koin yang tersedia.
2.	Program akan mencoba mencari kombinasi minimum koin untuk mencapai jumlah uang tersebut.
3.	Jika jumlah uang bisa dicapai dengan kombinasi koin yang tersedia, program menampilkan kombinasi koin yang digunakan. Jika tidak bisa dicapai, program memberi tahu pengguna bahwa kombinasi koin tidak cukup.


## 8. Buat sebuah program yang menerima string dari pengguna dan mengonversi string tersebut menjadi sebuah list berisi kata-kata terbalik. Misalnya:
```
Input: "Saya suka Python"
Output: ["ayaS", "akus", "nohtyP"]
```
### Kode Program:
```python
def balik_kata(string):
    # Memecah string menjadi list kata-kata
    kata_list = string.split()

    # Membalik setiap kata dan menyimpan dalam list baru
    kata_terbalik = [kata[::-1] for kata in kata_list]

    return kata_terbalik

# Fungsi utama untuk input dari pengguna
def main():
    # Menerima input dari pengguna
    input_string = input("Masukkan sebuah kalimat: ")

    # Memanggil fungsi untuk membalik kata-kata
    hasil = balik_kata(input_string)

    # Menampilkan hasil
    print("Output:", hasil)

# Menjalankan program
main()
```
### Output:
![image](https://github.com/user-attachments/assets/fb5c0440-29cf-40e7-b9be-b4c90134e863)

### Penjelaan:
Fungsi balik_kata(string):
1.	Memecah kalimat menjadi list kata-kata:
- string.split() memisahkan kalimat berdasarkan spasi dan mengubahnya menjadi list yang berisi kata-kata. Misalnya, jika input kalimatnya adalah "Halo dunia", maka kata_list akan berisi ["Halo", "dunia"].
2.	Membalik setiap kata:
- Kode ini menggunakan list comprehension untuk membalik setiap kata yang ada di dalam kata_list. kata[::-1] adalah cara untuk membalik urutan karakter dalam string. Sebagai contoh, "Halo" menjadi "olaH", dan "dunia" menjadi "ainud".
List comprehension ini menghasilkan list baru, yaitu kata_terbalik, yang berisi kata-kata yang sudah dibalik.
3.	Mengembalikan hasil:
- Fungsi ini mengembalikan list kata-kata yang sudah dibalik.

Penjelasan Fungsi main():
1.	Menerima input dari pengguna: Program meminta pengguna memasukkan sebuah kalimat, dan hasil input disimpan dalam variabel input_string.
2.	Memanggil fungsi balik_kata:
- Program memanggil fungsi balik_kata() dengan parameter input_string (kalimat yang dimasukkan pengguna).
- Fungsi ini akan mengembalikan list yang berisi kata-kata yang sudah dibalik.
3.	Menampilkan hasil:
Program menampilkan hasil, yaitu list dari kata-kata yang sudah dibalik.

## 9. Buat class bernama `Buku` yang memiliki atribut `judul`, `penulis`, dan `tahun_terbit`. Buat method dalam class untuk menampilkan informasi buku, serta method untuk menghitung usia buku berdasarkan tahun saat ini. Buatlah 3 objek dari class `Buku` dan tampilkan informasi serta usia masing-masing buku.
### Kode Progrram:
```python
from datetime import datetime

# Definisi class Buku
class Buku:
    # Constructor untuk menginisialisasi atribut
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    # Method untuk menampilkan informasi buku
    def info_buku(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

    # Method untuk menghitung usia buku
    def usia_buku(self):
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - self.tahun_terbit
        return usia

# Membuat tiga objek dari class Buku
buku1 = Buku("Infrastruktur dan Struktur Data", "Siti Khomsah", 1977)
buku2 = Buku("Fisolofi Hidup", "K. Malkan", 2005)
buku3 = Buku("Mencintai dalam hati", "RWP", 2004)

# Menampilkan informasi dan usia dari setiap buku
for buku in [buku1, buku2, buku3]:
    buku.info_buku()
    print(f"Usia Buku: {buku.usia_buku()} tahun")
    print("-" * 30)
```
### Output:
![image](https://github.com/user-attachments/assets/da49032c-4435-457f-a55e-cef31ae28917)

### Penyelesaian:
1. Class Buku:
- Class ini memiliki 3 atribut: judul, penulis, dan tahun_terbit.
- Method tampilkan_info() digunakan untuk mencetak informasi buku (judul, penulis, dan tahun terbit).
- Method hitung_usia() digunakan untuk menghitung usia buku berdasarkan tahun saat ini yang diambil menggunakan fungsi datetime.now().year.
2. Pembuatan Objek:
- Tiga objek dari class Buku dibuat: buku1, buku2, dan buku3.
- Setiap objek diberi nilai judul, penulis, dan tahun terbit.
3. Tampilan Output:
- Informasi buku ditampilkan menggunakan method tampilkan_info().
- Usia buku dihitung dan ditampilkan menggunakan method hitung_usia().

## 10. Buatlah program yang mengimplementasikan algoritma pencarian biner, namun dengan modifikasi: algoritma harus bisa mencari nilai di list yang hanya berisi angka genap, dan jika nilai yang dicari adalah angka ganjil, program harus menampilkan pesan bahwa nilai tersebut tidak bisa ditemukan.
#### Kode Program:
```python
def binary_search_genap(arr, target):
    # Pastikan nilai yang dicari adalah bilangan genap
    if target % 2 != 0:
        print(f"Nilai {target} adalah bilangan ganjil dan tidak bisa ditemukan.")
        return -1

    # Implementasi pencarian biner
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Jika tidak ditemukan
    return -1

# Fungsi utama untuk input dari pengguna
def main():
    # List hanya berisi angka genap
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    try:
        # Input nilai yang ingin dicari
        target = int(input("Masukkan nilai yang ingin dicari: "))

        # Panggil fungsi binary search yang dimodifikasi
        index = binary_search_genap(arr, target)

        if index != -1:
            print(f"Nilai {target} ditemukan pada indeks {index}.")
        else:
            if target % 2 == 0:
                print(f"Nilai {target} tidak ditemukan dalam list.")

    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")

# Menjalankan program
main()
```
### Output:
![image](https://github.com/user-attachments/assets/834c218a-ec72-43ee-8abf-d9e34ec00e02)

### Penyelesaian:
Penjelasan Kode:
1. Fungsi binary_search_genap(arr, target):
- Fungsi ini melakukan pencarian bilangan genap dengan metode binary search.Bagian ini memeriksa apakah bilangan yang dicari (target) adalah ganjil. Jika iya, maka fungsi langsung mengembalikan nilai -1 dan mengeluarkan pesan bahwa bilangan tersebut tidak bisa dicari, karena hanya bilangan genap yang akan dicari.
- low dan high digunakan sebagai batas bawah dan batas atas dari list selama pencarian. Pada awalnya, low dimulai dari indeks 0, dan high dari indeks terakhir (panjang list - 1).
- Selama batas bawah tidak melebihi batas atas, pencarian tetap dilakukan. mid dihitung sebagai nilai tengah dari indeks saat ini.
- Jika nilai tengah (nilai di arr[mid]) sama dengan target, maka indeks mid dikembalikan sebagai hasil.
- Jika nilai tengah lebih kecil dari target, batas bawah low diperbarui ke mid + 1 untuk memfokuskan pencarian di bagian kanan list.
- Jika nilai tengah lebih besar dari target, batas atas high diperbarui ke mid - 1 untuk memfokuskan pencarian di bagian kiri list.
- Jika tidak ditemukan setelah pencarian selesai, fungsi mengembalikan -1 untuk menunjukkan bahwa target tidak ada di dalam list.
  
2. Fungsi main():
- Bagian ini adalah fungsi utama yang menerima input dari pengguna dan menjalankan logika pencarian.
- List ini hanya berisi bilangan genap yang telah diurutkan.
- Pengguna diminta memasukkan angka yang ingin dicari, dan input tersebut dikonversi menjadi integer.
- Fungsi binary_search_genap() dipanggil dengan list arr dan target yang diinputkan pengguna. Fungsi ini akan mengembalikan indeks tempat target ditemukan, atau -1 jika target tidak ditemukan atau merupakan bilangan ganjil.
- Jika hasil pencarian (index) bukan -1, maka program menampilkan bahwa nilai tersebut ditemukan pada indeks tertentu.
- Jika tidak ditemukan dan target adalah bilangan genap, program akan menampilkan pesan bahwa target tidak ada di list.
- Jika pengguna memasukkan bilangan ganjil, pesan "Nilai X adalah bilangan ganjil dan tidak bisa ditemukan" akan muncul sebelumnya di fungsi binary_search_genap().
3. Penanganan Input yang Tidak Valid: Jika pengguna memasukkan input yang bukan angka, program akan menangani kesalahan tersebut dan menampilkan pesan bahwa input tidak valid.
4. Kesimpulan:
Program ini menggunakan algoritma binary search untuk mencari bilangan genap dalam list yang sudah diurutkan. Program juga menangani kasus ketika pengguna memasukkan bilangan ganjil atau input yang tidak valid.


# Kesimpulan
Dari pembelajaran dasar-dasar Python, saya belajar banyak hal yang membantu saya memahami cara kerja pemrograman. Pertama, saya belajar tentang berbagai tipe data seperti angka, teks, dan daftar, yang penting untuk menyimpan informasi. Saya juga memahami struktur data seperti list, tuple, dictionary, dan set, yang masing-masing memiliki cara penggunaan yang berbeda.

Saya belajar cara menggunakan if dan loop seperti for dan while untuk mengatur alur program. Selain itu, saya juga mengenal fungsi yang membuat kode lebih terorganisir dan mudah digunakan kembali. Konsep pemrograman berorientasi objek (OOP) memperlihatkan bagaimana kita bisa membuat kelas dan objek, yang membuat program lebih terstruktur.

Hal lain yang penting adalah saya belajar cara menangani kesalahan dengan penanganan exception, sehingga program bisa berjalan lebih stabil. Dengan memahami modul dan paket, saya bisa mengorganisir kode menjadi bagian-bagian kecil yang lebih mudah dikelola.

Secara keseluruhan, pembelajaran ini memberikan saya dasar yang kuat untuk melanjutkan belajar lebih jauh dalam pemrograman Python. Meskipun masih banyak yang harus dipelajari, saya merasa lebih percaya diri untuk menerapkan apa yang sudah saya pelajari dalam proyek-proyek mendatang.

## Referensi
[1] Rahman, S., Sembiring, A., Siregar, D., Prahmana, I. G., Puspadini, R., & Zen, M. (2023). Python: Dasar dan Pemrograman Berorientasi Objek. Penerbit Tahta Media. (https://tahtamedia.co.id/index.php/issj/article/view/344)

[2] Python, T. D. P. (2024). BAB 2 VARIABEL DAN TIPE DATA PYTHON. Bahasa Pemrograman Python, 12. 

[3] Romzi, M., & Kurniawan, B. (2020). Pembelajaran Pemrograman Python Dengan Pendekatan Logika Algoritma. JTIM: Jurnal Teknik Informatika Mahakarya, 3(2), 37-44.
