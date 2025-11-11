# src/domain/tiket_bisnis.py
from .tiket_kereta import TiketKereta

class TiketBisnis(TiketKereta):
    """
    Tiket Bisnis: ada tambahan fasilitas (mis. snack per orang).
    Contoh: biaya snack fixed per orang.
    """

    def __init__(self, nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi="Bisnis", biaya_snack=20000):
        super().__init__(nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi)
        # enkapsulasi kecil untuk biaya snack: property tidak wajib, gunakan validasi sederhana
        if not isinstance(biaya_snack, (int, float)) or biaya_snack < 0:
            raise ValueError("biaya_snack harus >= 0")
        self._biaya_snack = float(biaya_snack)

    def hitung_total(self) -> float:
        return (self.harga_dasar + self._biaya_snack) * self.jumlah

    def deskripsi(self) -> str:
        return f"[BISNIS] {self.nama_kereta} -> {self.tujuan} - Rp {int(self.harga_dasar):,}/orang + Snack"
    
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

