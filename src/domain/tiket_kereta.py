# src/domain/tiket_kereta.py
from abc import ABC, abstractmethod

class TiketKereta(ABC):
    """
    Class abstrak untuk tiket kereta.
    Menyediakan enkapsulasi untuk harga dasar dan kursi (private attributes).
    Subclass wajib mengimplementasikan hitung_total() dan deskripsi().
    """

    def __init__(self, nama_kereta: str, tujuan: str, tanggal: str, jumlah: int, harga_dasar: float, kursi: str):
        self.nama_kereta = nama_kereta
        self.tujuan = tujuan
        self.tanggal = tanggal

        # private attributes
        self.__set_harga_dasar(harga_dasar)
        self.__set_kursi(kursi)

        # jumlah tiket (public, tapi kita validasi)
        if not isinstance(jumlah, int) or jumlah <= 0:
            raise ValueError("jumlah harus bilangan bulat positif")
        self.jumlah = jumlah

    # --- enkapsulasi harga_dasar ---
    def __set_harga_dasar(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("harga dasar harus bilangan >= 0")
        self.__harga_dasar = float(value)

    def __get_harga_dasar(self) -> float:
        return self.__harga_dasar

    harga_dasar = property(__get_harga_dasar, __set_harga_dasar)

    # --- enkapsulasi kursi ---
    def __set_kursi(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("kursi tidak boleh kosong")
        self.__kursi = value.strip()

    def __get_kursi(self) -> str:
        return self.__kursi

    kursi = property(__get_kursi, __set_kursi)

    # ---- abstrak methods ----
    @abstractmethod
    def hitung_total(self) -> float:
        """Menghitung total harga (harus diimplementasi subclass)."""
        pass

    @abstractmethod
    def deskripsi(self) -> str:
        """Mengembalikan deskripsi singkat tiket (harus diimplementasi subclass)."""
        pass
