import json
import os

class FileManager:
    def __init__(self, filename="data_tiket.json"):
        self.filename = filename

    def simpan_data(self, data):
        """Menyimpan list atau dict ke file JSON."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def muat_data(self):
        """Membaca data JSON dan mengembalikannya sebagai list/dict."""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as f:
            return json.load(f)