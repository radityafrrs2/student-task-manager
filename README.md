# 🎓 Student Task Manager

Student Task Manager adalah aplikasi web sederhana yang dibuat untuk membantu mahasiswa mengelola tugas kuliah, memantau progres pengerjaan, dan menyimpan deadline dalam satu tempat.

Project ini dikembangkan sebagai latihan penerapan dasar pemrograman Python, pengembangan web menggunakan Flask, pengelolaan data menggunakan JSON, serta penggunaan Git, GitHub, dan deployment web melalui PythonAnywhere.

## ✨ Fitur

- ➕ Menambahkan tugas kuliah
- 📋 Melihat daftar tugas yang tersimpan
- 🔴 Menampilkan status **Belum Dikerjakan**
- 🟡 Menampilkan status **Sedang Dikerjakan**
- 🟢 Menampilkan status **Selesai**
- 🔄 Mengubah status pengerjaan tugas
- 🗑️ Menghapus tugas
- 📅 Menyimpan deadline tugas
- 💾 Menyimpan data tugas menggunakan file JSON
- 🔒 Mempertahankan data tugas setelah aplikasi di-restart melalui penyimpanan JSON
- 📊 Menampilkan dashboard statistik tugas
- 📈 Menghitung total tugas, tugas yang belum dikerjakan, sedang dikerjakan, dan selesai
- 📱 Menggunakan tampilan responsif untuk berbagai ukuran layar
- 🌐 Menyediakan akses aplikasi melalui website yang telah di-deploy

## 📊 Dashboard Statistik

Dashboard statistik memberikan gambaran singkat mengenai kondisi tugas yang tersimpan di aplikasi.

Informasi yang ditampilkan meliputi:

- **Total Tugas:** jumlah seluruh tugas yang tersimpan
- **Belum Dikerjakan:** jumlah tugas yang belum mulai dikerjakan
- **Sedang Dikerjakan:** jumlah tugas yang sedang dalam proses pengerjaan
- **Selesai:** jumlah tugas yang telah diselesaikan

Nilai statistik ditampilkan berdasarkan data tugas yang tersimpan pada aplikasi.

## 🛠️ Teknologi

- **Python** — bahasa pemrograman utama
- **Flask** — framework untuk membangun aplikasi web
- **HTML5** — struktur halaman web
- **CSS3** — desain dan tata letak antarmuka
- **JSON** — penyimpanan data tugas
- **Git** — version control
- **GitHub** — penyimpanan repository dan pengelolaan versi kode
- **PythonAnywhere** — platform deployment aplikasi web

## 📂 Struktur Project

```text
Student Task Manager/
│
├── Student Task Manager.py
├── tasks.json
├── requirements.txt
├── README.md
├── DAILY_PROGRESS.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## ⚙️ Persyaratan

Sebelum menjalankan aplikasi secara lokal, pastikan perangkat sudah memiliki:

- Python
- pip untuk mengelola package Python
- Git (opsional, jika ingin menggunakan version control)

## 🚀 Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone https://github.com/radityafrrs2/student-task-manager.git
```

### 2. Masuk ke Folder Project

```bash
cd student-task-manager
```

### 3. Instal Dependencies

```bash
py -m pip install -r requirements.txt
```

Jika perintah `py` tidak tersedia, gunakan perintah `python` sesuai konfigurasi Python pada perangkat.

### 4. Jalankan Aplikasi

```bash
py "Student Task Manager.py"
```

Buka alamat lokal yang ditampilkan oleh Flask di terminal untuk mengakses aplikasi.

## 🌐 Deployment

Aplikasi ini telah di-deploy menggunakan PythonAnywhere.

**Website:** https://radityafrrs2.pythonanywhere.com/

Repository GitHub digunakan untuk menyimpan kode sumber dan mengelola perubahan aplikasi.

## 🔄 Pengembangan Project

Pengembangan dilakukan secara bertahap dengan menambahkan fitur, memperbaiki tampilan, menguji fungsi aplikasi, dan memperbarui repository.

Setiap perubahan yang telah diperiksa dapat disimpan menggunakan Git, dikirim ke GitHub, kemudian diterapkan ke website melalui PythonAnywhere.

Catatan perkembangan harian project disimpan secara terpisah pada file `DAILY_PROGRESS.md`.

## 🎯 Tujuan Project

Project ini bertujuan untuk:

- Memahami dasar pengembangan aplikasi web menggunakan Python dan Flask
- Mempraktikkan penggunaan HTML dan CSS untuk membangun antarmuka
- Memahami penyimpanan dan pengolahan data menggunakan JSON
- Mempelajari penggunaan Git dan GitHub untuk version control
- Memahami proses deployment aplikasi web
- Mengembangkan aplikasi sederhana yang relevan dengan kebutuhan mahasiswa

## 👨‍💻 Developer

**Raditya Farras Azis**

Teknologi Rekayasa Otomasi  
Sekolah Vokasi, Universitas Diponegoro

## 📝 Catatan

Project ini masih dapat dikembangkan dengan penambahan fitur baru sesuai kebutuhan pengguna dan proses pembelajaran.
