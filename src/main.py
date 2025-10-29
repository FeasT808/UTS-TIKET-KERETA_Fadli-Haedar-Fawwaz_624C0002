# src/main.py
import os
import json
from datetime import datetime

from domain.tiket_ekonomi import TiketEkonomi
from domain.tiket_bisnis import TiketBisnis
from domain.tiket_eksekutif import TiketEksekutif
from domain.pelanggan import Pelanggan

SAVE_FILE = os.path.join(os.path.dirname(__file__), "..", "purchases.json")
SAVE_FILE = os.path.abspath(SAVE_FILE)

# contoh daftar kereta + harga dasar per kelas (bisa dikembangkan)
KERETA_DATA = [
    {"nama": "KA Bengawan", "tujuan": "Surabaya", "harga": {"Ekonomi": 120000, "Bisnis": 350000, "Eksekutif": 600000}},
    {"nama": "KA Argo Lawu", "tujuan": "Yogyakarta", "harga": {"Ekonomi": 100000, "Bisnis": 400000, "Eksekutif": 700000}},
    {"nama": "KA Lokal Nusantara", "tujuan": "Solo", "harga": {"Ekonomi": 80000, "Bisnis": 250000, "Eksekutif": 450000}},
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_purchases():
    if not os.path.exists(SAVE_FILE):
        return []
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # saved entries already have enough info for display
        return data.get("purchases", [])
    except Exception:
        return []

def save_purchases(purchases):
    try:
        os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump({"purchases": purchases}, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Gagal menyimpan:", e)

def pilih_kereta():
    print("Daftar Kereta Tersedia:")
    for i, k in enumerate(KERETA_DATA, start=1):
        print(f"{i}. {k['nama']} - Tujuan: {k['tujuan']}")
    pilih = input("Pilih nomor kereta: ").strip()
    if not pilih.isdigit() or int(pilih) not in range(1, len(KERETA_DATA)+1):
        raise ValueError("Pilihan kereta tidak valid")
    return KERETA_DATA[int(pilih)-1]

def buat_tiket_by_class(kelas: str, nama_kereta: str, tujuan: str, tanggal: str, jumlah: int, harga_dasar: float):
    kelas_norm = kelas.strip().lower()
    if kelas_norm == "ekonomi":
        return TiketEkonomi(nama_kereta, tujuan, tanggal, jumlah, harga_dasar)
    if kelas_norm == "bisnis":
        return TiketBisnis(nama_kereta, tujuan, tanggal, jumlah, harga_dasar)
    if kelas_norm == "eksekutif":
        return TiketEksekutif(nama_kereta, tujuan, tanggal, jumlah, harga_dasar)
    raise ValueError("Kelas tidak dikenal")

def menu():
    purchases = load_purchases()
    while True:
        print("\n=== SISTEM TIKET KERETA API (UTS) ===")
        print("[1] Pesan Tiket")
        print("[2] Lihat Daftar Tiket (contoh objek)")
        print("[3] Lihat Ringkasan Pembelian")
        print("[4] Keluar")
        choice = input("Pilih (1-4): ").strip()
        clear()
        if choice == "1":
            try:
                nama = input("Nama Penumpang : ").strip()
                if not nama:
                    raise ValueError("Nama tidak boleh kosong")
                pelanggan = Pelanggan(nama)

                kereta = pilih_kereta()
                tanggal = input("Tanggal (YYYY-MM-DD) : ").strip()
                # validasi tanggal sederhana
                try:
                    datetime.strptime(tanggal, "%Y-%m-%d")
                except Exception:
                    raise ValueError("Format tanggal harus YYYY-MM-DD")

                kelas = input("Kelas Kereta (Ekonomi/Bisnis/Eksekutif) : ").strip().title()
                jumlah_raw = input("Jumlah Tiket : ").strip()
                if not jumlah_raw.isdigit() or int(jumlah_raw) <= 0:
                    raise ValueError("Jumlah harus bilangan bulat positif")
                jumlah = int(jumlah_raw)

                harga_dasar = kereta["harga"].get(kelas, None)
                if harga_dasar is None:
                    raise ValueError("Kelas tidak tersedia untuk kereta ini")

                tiket = buat_tiket_by_class(kelas, kereta['nama'], kereta['tujuan'], tanggal, jumlah, harga_dasar)
                total = tiket.hitung_total()

                # tampilkan ringkasan transaksi
                print("\n--- RINCIAN TRANSAKSI ---")
                print(f"Nama Penumpang : {pelanggan}")
                print(f"Kereta         : {kereta['nama']} -> {kereta['tujuan']}")
                print(f"Kelas Kereta   : {kelas}")
                print(f"Jumlah Tiket   : {jumlah}")
                print(f"Total Harga    : Rp {int(total):,}")
                konfirmasi = input("Konfirmasi pembelian? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    # simpan ringkasan sederhana
                    purchases.append({
                        "nama": str(pelanggan),
                        "kereta": kereta['nama'],
                        "tujuan": kereta['tujuan'],
                        "kelas": kelas,
                        "jumlah": jumlah,
                        "tanggal": tanggal,
                        "total": int(total)
                    })
                    save_purchases(purchases)
                    print(f"Terima kasih telah membeli tiket, {pelanggan}!")
                else:
                    print("Pembelian dibatalkan.")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            # contoh polimorfisme: buat list of object lalu tampilkan deskripsi masing-masing
            daftar_tiket = []
            # menggunakan data kereta pertama sebagai contoh
            demo = KERETA_DATA[0]
            daftar_tiket.append(TiketEkonomi(demo['nama'], demo['tujuan'], "2025-10-29", 1, demo['harga']['Ekonomi']))
            daftar_tiket.append(TiketBisnis(demo['nama'], demo['tujuan'], "2025-10-29", 1, demo['harga']['Bisnis']))
            daftar_tiket.append(TiketEksekutif(demo['nama'], demo['tujuan'], "2025-10-29", 1, demo['harga']['Eksekutif']))

            print("Contoh daftar tiket (menunjukkan polimorfisme):")
            for t in daftar_tiket:
                print(t.deskripsi())

        elif choice == "3":
            if not purchases:
                print("Belum ada pembelian.")
            else:
                total_semua = 0
                print("--- RINGKASAN PEMBELIAN ---")
                for i, p in enumerate(purchases, start=1):
                    print(f"{i}. {p['nama']} | {p['kereta']} -> {p['tujuan']} | {p['kelas']} | {p['jumlah']} tiket | Rp {p['total']:,} | Tgl: {p['tanggal']}")
                    total_semua += p['total']
                print(f"\nTOTAL SEMUA: Rp {int(total_semua):,}")

        elif choice == "4":
            print("Keluar... Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu()
