# 🎓 Student Task Manager

### Manage your tasks. Track your progress. Stay organized.

Aplikasi pengelola tugas kuliah berbasis web yang dirancang untuk membantu mahasiswa mencatat tugas, memantau deadline, dan mengelola progres pengerjaan dalam satu tempat.

Student Task Manager dikembangkan sebagai proyek pembelajaran untuk menerapkan Python, Flask, HTML, CSS, pengelolaan data menggunakan JSON, version control dengan Git, serta deployment aplikasi web.

<p align="center">
  <a href="https://radityafrrs2.pythonanywhere.com/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Open_App-2563EB?style=for-the-badge" alt="Live Demo">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Status-Active_Development-16A34A?style=for-the-badge" alt="Development Status">
</p>

---

## 🌐 Live Demo

**Coba aplikasinya langsung tanpa perlu instalasi!**

🔗 **[Student Task Manager — Open Website](https://radityafrrs2.pythonanywhere.com/)**

## ✨ Key Features

| Fitur | Deskripsi |
|---|---|
| ➕ **Add Tasks** | Menambahkan tugas dengan nama, mata kuliah, dan deadline |
| 📋 **Task List** | Melihat daftar tugas yang tersimpan |
| 🔎 **Task Search** | Mencari tugas berdasarkan nama tugas |
| 🏷️ **Status Filter** | Menyaring tugas berdasarkan status pengerjaan |
| 🔄 **Progress Tracking** | Mengubah status tugas sesuai progres pengerjaan |
| 📊 **Statistics Dashboard** | Melihat ringkasan jumlah dan kondisi seluruh tugas |
| 🗑️ **Delete Tasks** | Menghapus tugas yang tidak lagi diperlukan |
| 💾 **JSON Persistence** | Menyimpan data tugas agar tetap tersedia setelah aplikasi dimulai ulang |
| 📱 **Responsive Interface** | Menyesuaikan tampilan untuk berbagai ukuran layar |

### 🚦 Task Status

- 🔴 **Belum Dikerjakan** — tugas belum mulai dikerjakan
- 🟡 **Sedang Dikerjakan** — tugas sedang dalam proses pengerjaan
- 🟢 **Selesai** — tugas telah diselesaikan

### 📊 Statistics Dashboard

Dashboard memberikan gambaran cepat tentang beban tugas melalui empat metrik utama:

- **Total Tugas** — seluruh tugas yang tersimpan
- **Belum Dikerjakan** — tugas yang belum mulai dikerjakan
- **Sedang Dikerjakan** — tugas yang sedang diproses
- **Selesai** — tugas yang telah diselesaikan

Statistik dihitung berdasarkan data tugas yang tersimpan pada aplikasi.

## 🖥️ Built With

| Teknologi | Peran |
|---|---|
| 🐍 **Python** | Logika dan pemrosesan aplikasi |
| ⚗️ **Flask** | Routing dan pengelolaan request web |
| 🌐 **HTML5** | Struktur halaman |
| 🎨 **CSS3** | Styling dan layout antarmuka |
| 📦 **JSON** | Penyimpanan data tugas |
| 🔧 **Git** | Version control |
| 🐙 **GitHub** | Hosting repository dan kolaborasi kode |
| ☁️ **PythonAnywhere** | Deployment aplikasi web |

## 📂 Project Structure

```text
student-task-manager/
├── Student Task Manager.py   # Main Flask application
├── tasks.json                # Task data storage
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── DAILY_PROGRESS.md         # Development progress log
├── templates/
│   └── index.html             # Main page template
└── static/
    └── style.css              # Application styling
```

## ⚙️ Getting Started

Ikuti langkah berikut untuk menjalankan aplikasi di perangkat lokal.

### 1. Prerequisites

Pastikan perangkat sudah memiliki:

- Python
- pip
- Git (opsional)

### 2. Clone Repository

```bash
git clone https://github.com/radityafrrs2/student-task-manager.git
```

### 3. Navigate to Project Directory

```bash
cd student-task-manager
```

### 4. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

Jika perintah `py` tidak tersedia, gunakan:

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
py "Student Task Manager.py"
```

Atau, jika menggunakan perintah `python`:

```bash
python "Student Task Manager.py"
```

### 6. Open in Browser

Buka alamat lokal berikut:

```text
http://127.0.0.1:5000/
```

## 💾 Data Storage

Aplikasi menggunakan file `tasks.json` untuk menyimpan daftar tugas dalam format JSON.

Data mencakup informasi seperti nama tugas, mata kuliah, deadline, dan status pengerjaan. Data disimpan ke file saat operasi penambahan, perubahan status, atau penghapusan dilakukan.

> **Catatan:** `tasks.json` merupakan file data lokal. Jika ingin mempertahankan data tugas pribadi, buat cadangan file tersebut sebelum melakukan perubahan besar pada proyek.

## 🚀 Development & Deployment

Pengembangan Student Task Manager dilakukan secara bertahap melalui siklus:

1. **Plan** — menentukan fitur yang akan dikembangkan
2. **Build** — mengimplementasikan perubahan pada kode
3. **Test** — memeriksa fungsi dan tampilan aplikasi
4. **Version Control** — menyimpan perubahan menggunakan Git dan GitHub
5. **Deploy** — memperbarui versi aplikasi pada PythonAnywhere

Riwayat perkembangan dan fitur yang telah dikerjakan dicatat dalam [`DAILY_PROGRESS.md`](DAILY_PROGRESS.md).

## 🎯 Project Goals

Proyek ini dibuat untuk memperkuat pemahaman mengenai:

- Pengembangan aplikasi web menggunakan Python dan Flask
- Integrasi backend dengan template HTML dan styling CSS
- Pengolahan serta penyimpanan data menggunakan JSON
- Penerapan routing dan HTTP request pada Flask
- Penggunaan Git dan GitHub untuk mengelola perubahan kode
- Deployment aplikasi web ke lingkungan hosting
- Pengembangan solusi digital sederhana untuk kebutuhan mahasiswa

## 👨‍💻 Developer

**Raditya Farras Azis**

Teknologi Rekayasa Otomasi  
Sekolah Vokasi — Universitas Diponegoro

---

<p align="center">
  <i>Built as a learning project — one feature at a time.</i>
</p>
