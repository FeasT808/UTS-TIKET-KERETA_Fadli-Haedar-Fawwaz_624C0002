# UTS_TiketKereta_<FADLI_HAEDAR_FAWWAZ>_<624C0002>

**Nama:** <FADLI HAEDAR FAWWAZ>  
**NPM:** <624C0002>


Proyek ini adalah implementasi sederhana Sistem Pemesanan Tiket Kereta Api menggunakan prinsip OOP di Python. Program berjalan di terminal dan memenuhi persyaratan UTS: menggunakan abstraksi (class abstrak), pewarisan, polimorfisme, dan enkapsulasi.

## Struktur folder
├─ src/
│ ├─ domain/
│ │ ├─ init.py
│ │ ├─ tiket_kereta.py
│ │ ├─ tiket_ekonomi.py
│ │ ├─ tiket_bisnis.py
│ │ ├─ tiket_eksekutif.py
│ │ └─ pelanggan.py
│ └─ main.py
├─ README.md



## Penjelasan penerapan 4 pilar OOP

1. **Abstraksi**
   - `TiketKereta` (file `tiket_kereta.py`) adalah class abstrak (menggunakan `abc.ABC`) yang mendefinisikan interface wajib:
     - `hitung_total(self) -> float`
     - `deskripsi(self) -> str`

2. **Pewarisan**
   - `TiketEkonomi`, `TiketBisnis`, `TiketEksekutif` mewarisi `TiketKereta`. Mereka mengimplementasikan method abstrak dan menambah perilaku masing-masing.

3. **Enkapsulasi**
   - Atribut sensitif seperti `__harga_dasar` dan `__kursi` disimpan sebagai private di `TiketKereta`. Akses dilakukan melalui property dengan validasi pada setter sehingga harga tidak negatif dan kursi tidak kosong.

4. **Polimorfisme**
   - Semua subclass mengimplementasikan `hitung_total()` dan `deskripsi()` sendiri. Program menunjukkan polimorfisme lewat `daftar_tiket` — ketika kita melakukan:
     ```py
     for tiket in daftar_tiket:
         print(tiket.deskripsi())
     ```
     Output berbeda sesuai tipe objek.

## Contoh input dan output singkat

Input:
Nama Penumpang : Ahmad
Pilih Kereta : 1 (KA Bengawan)
Tanggal : 2025-11-01
Kelas Kereta : Bisnis
Jumlah Tiket : 2
Konfirmasi : y
