# src/domain/tiket_eksekutif.py
from .tiket_kereta import TiketKereta

class TiketEksekutif(TiketKereta):
    """
    Tiket Eksekutif: harga dasar + fasilitas lounge atau layanan khusus.
    Kita tambahkan biaya layanan per penumpang.
    """

    def __init__(self, nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi="Eksekutif", biaya_layanan=50000):
        super().__init__(nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi)
        if not isinstance(biaya_layanan, (int, float)) or biaya_layanan < 0:
            raise ValueError("biaya_layanan harus >= 0")
        self._biaya_layanan = float(biaya_layanan)

    def hitung_total(self) -> float:
        return (self.harga_dasar + self._biaya_layanan) * self.jumlah

    def deskripsi(self) -> str:
        return f"[EKSEKUTIF] {self.nama_kereta} -> {self.tujuan} - Rp {int(self.harga_dasar):,}/orang + Lounge"
    
    def to_dict(self):
         return {
            "nama_kereta": self.nama_kereta,
            "tujuan": self.tujuan,
            "tanggal": self.tanggal,
            "jumlah": self.jumlah,
            "kursi": self.kursi,
            "harga_dasar": self.harga_dasar,
            "total": self.hitung_total(),
            "kelas": self.__class__.__name__
        }
