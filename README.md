# **Sistem Manajemen Transaksi**

Program manajemen transaksi keuangan berbasis Python yang memungkinkan pengguna untuk melihat, menambah, mengubah, dan menghapus data transaksi. Program ini menggunakan pustaka tabulate untuk menampilkan data dalam bentuk tabel yang rapi.
Fitur utama dalam program ini meliputi:
- Menampilkan transaksi berdasarkan semua data, ID transaksi, atau tanggal tertentu.
- Menambahkan transaksi baru dengan validasi format input.
- Mengubah transaksi, termasuk perubahan pada tanggal, jumlah, atau informasi lain.
- Menghapus transaksi dengan konfirmasi pengguna sebelum eksekusi.
- Antarmuka berbasis menu utama, yang memandu pengguna melalui berbagai fungsi dalam sistem manajemen transaksi.
Program ini dirancang untuk mempermudah pencatatan transaksi dalam bisnis kecil atau keperluan pribadi dengan pendekatan berbasis terminal (CLI).

**Fitur Utamanya**
- Lihat Data Transaksi: Menampilkan data transaksi yang ada, bisa dilihat berdasarkan ID, tanggal, atau menampilkan semua transaksi.
- Tambah Data Transaksi: Menambah transaksi baru dengan memvalidasi input untuk ID, tanggal, deskripsi, akun debit, kredit, dan jumlah.
- Ubah Data Transaksi: Memungkinkan pengubahan data transaksi berdasarkan ID, tanggal, jumlah, atau deskripsi.
- Hapus Data Transaksi: Menghapus transaksi berdasarkan ID transaksi setelah konfirmasi.
- Menu Utama: Menyediakan navigasi untuk mengakses berbagai opsi di program.

**Cara Penggunaannya**
- Lihat Data Transaksi: Pengguna dapat memilih untuk menampilkan semua transaksi atau mencari berdasarkan ID atau tanggal transaksi.
- Tambah Data Transaksi: Pengguna menginput ID transaksi, tanggal, deskripsi, akun debit, kredit, dan jumlah.
- Ubah Data Transaksi: Pengguna memilih transaksi yang ingin diubah dan memasukkan perubahan yang diperlukan, seperti tanggal, deskripsi, akun debit, atau jumlah.
- Hapus Data Transaksi: Pengguna memilih transaksi yang ingin dihapus dan kemudian mengkonfirmasi untuk menghapusnya.

**Catatan Mengenai Kekurangan Program**
- Validasi Input: Meskipun ada validasi input, program ini masih bisa lebih diperketat, terutama di bagian input tanggal dan jumlah.
- Keterbatasan Fitur: Program ini hanya dapat digunakan dalam satu periode tertentu (tanggal November 2023) yang sudah ditentukan. Tidak ada fleksibilitas untuk memilih periode yang berbeda.
- Keamanan: Program ini tidak memiliki sistem autentikasi pengguna, sehingga siapa saja yang memiliki akses ke program bisa melakukan perubahan atau penghapusan data.
