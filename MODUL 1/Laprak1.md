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
#### penjelasan:
kode ini membuat Fungsi: ambil_ganjil_dan_urutkan(list1, list2)
Fungsi ini memiliki dua daftar input, list1 dan list2. Tugas dari fungsi ini adalah:
- Mengambil elemen-elemen yang berada di indeks ganjil dari kedua daftar.
- Menggabungkan elemen-elemen tersebut menjadi satu daftar.
- Mengurutkan hasil gabungan tadi secara menurun (dari yang terbesar ke yang terkecil).
- Mengembalikan hasil akhir berupa daftar elemen yang sudah diurutkan.


## Kesimpulan
Ringkasan dan interpretasi pandangan kalia dari hasil praktikum dan pembelajaran yang didapat[1].

## Referensi
[1] I. Holm, Narrator, and J. Fullerton-Smith, Producer, How to Build a Human [DVD]. London: BBC; 2002.
