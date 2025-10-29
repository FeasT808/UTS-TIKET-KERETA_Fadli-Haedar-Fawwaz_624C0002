# src/domain/tiket_ekonomi.py
from .tiket_kereta import TiketKereta

class TiketEkonomi(TiketKereta):
    """
    Tiket Ekonomi: harga dasar dikali jumlah.
    Tambahan: tidak ada fasilitas ekstra.
    """

    def __init__(self, nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi="Ekonomi"):
        super().__init__(nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi)

    def hitung_total(self) -> float:
        return self.harga_dasar * self.jumlah

    def deskripsi(self) -> str:
        return f"[EKONOMI] {self.nama_kereta} -> {self.tujuan} - Rp {int(self.harga_dasar):,}/orang"
