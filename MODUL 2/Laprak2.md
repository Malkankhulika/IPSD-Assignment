<h1 align="center">Laporan Praktikum Modul Preprocessing</h1>
<p align="center">Khulika Malkan</p>
<p align="center">2311110057</p>
<p align="center">S1SD04-02</p>

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


# Kesimpulan
Dari pembelajaran dasar-dasar Python, saya belajar banyak hal yang membantu saya memahami cara kerja pemrograman. Pertama, saya belajar tentang berbagai tipe data seperti angka, teks, dan daftar, yang penting untuk menyimpan informasi. Saya juga memahami struktur data seperti list, tuple, dictionary, dan set, yang masing-masing memiliki cara penggunaan yang berbeda.


## Referensi
[1] Rahman, S., Sembiring, A., Siregar, D., Prahmana, I. G., Puspadini, R., & Zen, M. (2023). Python: Dasar dan Pemrograman Berorientasi Objek. Penerbit Tahta Media. (https://tahtamedia.co.id/index.php/issj/article/view/344)

