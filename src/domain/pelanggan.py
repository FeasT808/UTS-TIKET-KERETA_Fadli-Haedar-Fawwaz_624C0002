# src/domain/pelanggan.py
class Pelanggan:
    """
    Class sederhana untuk menyimpan info penumpang.
    Bukan requirement wajib, tapi membantu struktur program.
    """
    def __init__(self, nama: str):
        if not nama or not isinstance(nama, str):
            raise ValueError("Nama tidak boleh kosong")
        self.nama = nama.strip()

    def __str__(self):
        return self.nama
