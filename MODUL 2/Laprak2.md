<h1 align="center">Laporan Praktikum Modul EDA/Preprocessing</h1>
<p align="center">Khulika Malkan</p>
<p align="center">2311110057</p>
<p align="center">S1SD04-02</p>

## Dasar Teori
Tahapan pertama dalam proses machine learning adalah eksplorasi data. Eksplorasi data merupakan proses pemahaman terhadap data yang akan dianalisis. Dengan mengeksplorasi data terlebih dahulu, kita dapat menentukan teknik mana yang akan digunakan. Dibawah ini adalah contoh eksplorasi data dengan memahami statistika deskriptif dari data [1].

### EDA
“Exploratory Data Analysis (EDA) is an approach/philosophy for data analysis that employs a variety of techniques (mostly graphical) to maximize insight into a data set” [2]
Analisis Data Eksploratif (EDA) adalah pendekatan/filosofi untuk analisis data yang menggunakan berbagai teknik (sebagian besar berupa grafis) untuk memaksimalkan wawasan terhadap sebuah dataset, dengan:
- 1.mengungkap struktur dasar;
- 2.mengekstraksi variabel penting;
- 3.mendeteksi outlier dan anomali;
- 4.test underlying assumptions (menguji asumsi-asumsi yang mendasar;
- 5.mengembangkan model-model yang sederhana
- 6.Menentukan setting faktor yang optimal.

### Preprocessing Data - Missing Value
Setelah proses eksplorasi data,langkah selanjutnya yang dilakukan adalah proses data pre processing. Dalam tahapan ini kita akan menangani data dengan memeriksa apakah ada missing value pada data yang akan dianalisis [3].

### Preprocessing Data - Scaling
Setelah memahami missing value dan berhasil mengatasinya, selanjutnya adalah proses scaling atau biasa dikenal dengan normalisasi. Ada kalanya data yang dimiliki memiliki rentang yang cukup jauh satu sama lain sehingga perlu dinormalisasi.

Normalisasi data ini membutuhkan nilai minimum dan maksimum. Nilai minimum yang biasa digunakan adalah 0 dan nilai maksimum adalah 1. Sehingga, data memiliki rentang 0 sampai 1. Preprocessing data merupakan tahapan penting dalam analisis data. Dengan proses tersebut, data yang akan dianalisis akan lebih siap sehingga hasilnya pun lebih akurat. 

# Langkah-langkah umum EDA pada Python
## 1.  Import Libraries:
### Kode Program:
```python
import pandas as pd
import numpy as np
```
### code:
![image](https://github.com/user-attachments/assets/5c0ebed3-6759-4583-ae18-69195a9b42c1)

### Penjelasan:
Dalam Python, import pandas as pd dan import numpy as np digunakan untuk mengimpor dua pustaka (library) yang digunakan untuk analisis data dan komputasi numerik.

## 2. Load Data: Read data set pada pandas DataFrame menggunakan pd.read_csv() atau pd.read_excel() 
### Kode Program:
```python
film = pd.read_csv("movie_classification.csv")
```
### code:
![image](https://github.com/user-attachments/assets/619a80ef-747d-43ab-a888-66999442a769)

### Penjelasan:
Untuk memuat dataset ke dalam DataFrame menggunakan pandas, menggunakan pd.read_csv() untuk membaca file CSV atau pd.read_excel() untuk membaca file Excel.

## 3. Data Overview: Memahami data melalui examinasi basic properties  
### Kode Program:
```python
# Display the first few rows of the DataFrame
film.head()

# Get summary statistics of numerical columns
film.describe()

# Check data types and missing values
film.info()
```
### code:
![image](https://github.com/user-attachments/assets/5b94979f-d920-4933-8a7d-6cd7dee13088)


### Penjelasan:
1. film.head()
- 1. Fungsi: Menampilkan beberapa baris pertama dari DataFrame (secara default 5 baris).
  2. Tujuan: Untuk memberikan gambaran awal tentang struktur data, kolom yang ada, dan beberapa contoh nilai.
2. film.describe()
- 1. Fungsi: Menghasilkan statistik ringkasan untuk kolom numerik dalam DataFrame.
  2. Tujuan: Untuk memahami distribusi data, seperti mean, median, minimum, maksimum, dan quartiles. Ini membantu Anda mengevaluasi rentang nilai dan potensi outlier.
3. film.info()
- 1. Fungsi: Menampilkan informasi tentang DataFrame, termasuk jumlah total entri, nama kolom, tipe data, dan jumlah nilai non-null untuk setiap kolom.
  2. Tujuan: Untuk memahami jenis data yang ada (misalnya, numerik, kategori) serta memeriksa adanya nilai yang hilang (missing values). Ini penting untuk merencanakan langkah-langkah pembersihan data yang diperlukan.


## 4. Data Cleaning: Penanganan missing values, duplicate records, dan outliers . Pandas menyediakan metode seperti dropna(), fillna(), dan drop_duplicates() untuk data cleaning.  
### Kode Program:
```python
# Remove rows with missing values
movie.dropna(inplace=True)

# Remove duplicate rows
film.drop_duplicates(inplace=True)

# Hndle outliers if needed
```
### code:
![image](https://github.com/user-attachments/assets/4eb93297-31fb-4428-9948-eabca4543076)

### Penjelasan:
- a.Menangani Missing Values
Missing values dapat memengaruhi analisis dan hasil model. Oleh karenanya perlu dilakukan penghapusan baris dengan menggunakan missing value
- b.Menghapus Duplikasi
Duplikat dalam dataset dapat menyebabkan bias dalam analisis.

# Kesimpulan
Dari pembelajaran Preprocessing data dalam bahasa pemrograman Python adalah langkah penting yang memastikan data siap untuk analisis dan pemodelan. Proses ini melibatkan pembersihan data dari nilai hilang dan duplikasi, serta transformasi data seperti normalisasi dan encoding kategori. Python menawarkan berbagai library, seperti Pandas untuk manipulasi data dan Scikit-learn untuk teknik preprocessing, yang memudahkan kita dalam melakukan tugas ini. Dengan melakukan preprocessing yang tepat, kita dapat meningkatkan akurasi dan keandalan model machine learning. Penting untuk menyesuaikan proses ini dengan karakteristik dataset dan tujuan analisis, sehingga hasil yang diperoleh menjadi lebih optimal.


## Referensi
[1] Famili, A., Shen, W. M., Weber, R., & Simoudis, E. (1997). Data preprocessing and intelligent data analysis. Intelligent data analysis, 1(1), 3-23. 

[2] Infrastruktur dan Platform Sains Data/ PERTEMUAN 2 Exploratory Data Analysis (https://lms.telkomuniversity.ac.id/pluginfile.php/5879110/mod_resource/content/1/M2_%20UFI_EDA.pdf)

[3] https://dqlab.id/preprocessing-data-pada-machine-learning-python
