![image](https://github.com/user-attachments/assets/535bdb5e-4406-4ebf-9144-6a4166cc3340)<h1 align="center">Laporan Praktikum Modul EDA/Preprocessing</h1>
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
!pip install pandas
!pip install numpy
!pip install seaborn
!pip install matplotib.pyplot
!pip install openpyxl
!pip install wordcloud
!pip install imblearn
!pip install scikit-learn
!pip install sklearn
```
### code:
![image](https://github.com/user-attachments/assets/7c218950-23f4-4de7-8327-02cf0988f9fc)

### Penjelasan:
- pandas: Library untuk manipulasi dan analisis data, menyediakan struktur data seperti DataFrame untuk memudahkan pengolahan data tabular.
- numpy: Library untuk komputasi numerik, menyediakan array multidimensi dan fungsi-fungsi matematika untuk operasi pada array tersebut.
- seaborn: Library untuk visualisasi data.
- matplotlib.pyplot: Modul dari matplotlib yang digunakan untuk membuat grafik dan plot secara interaktif.
- openpyxl: Library untuk membaca dan menulis file Excel dengan format .xlsx.
- wordcloud: Library untuk membuat visualisasi cloud kata dari teks, menunjukkan frekuensi kata dalam bentuk grafik.
- imblearn: Library untuk menangani ketidakseimbangan kelas dalam dataset, menyediakan metode untuk oversampling dan undersampling.
- scikit-learn: Library untuk machine learning, menyediakan berbagai algoritma dan tools untuk klasifikasi, regresi, dan clustering.
- sklearn: Digunakan untuk import library yang sama.

## 2. Load Data: Read data set pada pandas DataFrame menggunakan pd.read_csv()
### Kode Program:
```python
db = pd.read_csv ("diabetes.csv")
db
```
### code:
![image](https://github.com/user-attachments/assets/4cea8b5a-66bb-432c-9577-ce6291181fd6)


### Penjelasan:
Untuk memuat dataset ke dalam DataFrame menggunakan pandas, menggunakan pd.read_csv() untuk membaca file CSV.

## 3. Data Cleaning: Penanganan missing values untuk data cleaning.  
### Kode Program:
```python
print("\nMissing values per kolom:")
db.isnull().sum()
```
### code:
![image](https://github.com/user-attachments/assets/b9ee5bbf-d2c2-4bb0-8ff4-1fa7551352ac)

### Penjelasan:
- Menangani Missing Values
Missing values dapat memengaruhi analisis dan hasil model. Oleh karenanya perlu dilakukan penghapusan baris dengan menggunakan missing value
- Menghapus Duplikasi
Duplikat dalam dataset dapat menyebabkan bias dalam analisis.

## 4. Pilih kolom numerik untuk imputasi
### Kode Program:
```python
# Hanya kolom numerik yang akan diimputasi dengan mean, median, modus
numerical_cols = db.select_dtypes(include=[np.number]).columns

print("\nKolom numerik yang akan diimputasi:", numerical_cols)
```
### code:
![image](https://github.com/user-attachments/assets/c9a82fea-baa5-4a75-93b2-5cb9b59b2386)

### Penjelasan:
Pilih kolom numerik saja karena jika tidak kode program akan error karena ada data yang berupa string juga.

## 5. Imputasi missing values pada kolom numerik saja
### Kode Program:
```python
imputer_mean = SimpleImputer(strategy="mean")
imputer_median = SimpleImputer(strategy="median")
imputer_mode = SimpleImputer(strategy="most_frequent")
```

### code:

![image](https://github.com/user-attachments/assets/14c82708-bfbf-4f41-b571-53762d6606e6)

### Mean:

![image](https://github.com/user-attachments/assets/55dc8ba9-5392-4637-a85b-4d6472dd1aa1)

### Median:

![image](https://github.com/user-attachments/assets/5e27e553-7dc4-4a39-adf9-7755ccda2c9e)

### Modus:

![image](https://github.com/user-attachments/assets/d24b9a4d-ca2d-422f-ad7d-328cd2741fe6)

### Penjelasan:
kolom numerik yang teridentifikasi dalam numerical_cols diimputasi dengan nilai rata-rata menggunakan imputer_mean.fit_transform(). Setelah proses ini, data yang hilang digantikan oleh rata-rata kolom, dan hasilnya ditampilkan menggunakan db_mean.head().


## 5. Imputasi missing values pada kolom numerik saja
### Kode Program:
```python
imputer_mean = SimpleImputer(strategy="mean")
imputer_median = SimpleImputer(strategy="median")
imputer_mode = SimpleImputer(strategy="most_frequent")
### code:
### Penjelasan:



# Kesimpulan
Dari pembelajaran Preprocessing data dalam bahasa pemrograman Python adalah langkah penting yang memastikan data siap untuk analisis dan pemodelan. Proses ini melibatkan pembersihan data dari nilai hilang dan duplikasi, serta transformasi data seperti normalisasi dan encoding kategori. Python menawarkan berbagai library, seperti Pandas untuk manipulasi data dan Scikit-learn untuk teknik preprocessing, yang memudahkan kita dalam melakukan tugas ini. Dengan melakukan preprocessing yang tepat, kita dapat meningkatkan akurasi dan keandalan model machine learning. Penting untuk menyesuaikan proses ini dengan karakteristik dataset dan tujuan analisis, sehingga hasil yang diperoleh menjadi lebih optimal.


## Referensi
[1] Famili, A., Shen, W. M., Weber, R., & Simoudis, E. (1997). Data preprocessing and intelligent data analysis. Intelligent data analysis, 1(1), 3-23. 

[2] Infrastruktur dan Platform Sains Data/ PERTEMUAN 2 Exploratory Data Analysis (https://lms.telkomuniversity.ac.id/pluginfile.php/5879110/mod_resource/content/1/M2_%20UFI_EDA.pdf)

[3] https://dqlab.id/preprocessing-data-pada-machine-learning-python
