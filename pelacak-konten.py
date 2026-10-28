import json
from datetime import date
from pathlib import Path

FILE_KONTEN = Path(__file__).resolve().parent / "konten.json"

def muat_konten():
    """Baca daftar konten dari file json."""
    if not FILE_KONTEN.exists():
        print("Data konten belum tersedia")
        return []
    else:
        with open(FILE_KONTEN, "r", encoding="utf-8") as file:
            return json.load(file) 


def simpan_konten(daftar_konten):
    """Simpan daftar konten ke file json."""
    with open(FILE_KONTEN, "w", encoding="utf-8") as file:  
        json.dump(daftar_konten, file, indent=4, ensure_ascii=False)


def tambah_konten(daftar_konten):
    judul = input("Judul konten: ").strip()
    konsep = input("Konsep (misal: storytelling, review, tutorial): ").strip()
    while True:
        try:
            views = int(input("Views: "))
            break 
        except ValueError:
            print("Peringatan: Views harus berupa angka! Silakan coba lagi.")
    

    konten = {
        "judul": judul,
        "tanggal_upload": date.today().isoformat(),
        "konsep": konsep,
        "views": views,
    }
    daftar_konten.append(konten)
    simpan_konten(daftar_konten)
    print("Konten tersimpan.")


def lihat_konten(daftar_konten):
    if not konten:
        print ("Data belum tersedia")
    else :
        print(f"\n{'Judul':<20} | {'Konsep':<17} | {'Views':<7}")
        print("=" * 60)
        for item in konten:
            print(f"{item['judul']:<20} | {item['konsep']:<17} | {item['views']:<7} Views")


konten = muat_konten()

while True:
    print("="*40)
    print("Selamat datang di program pelacak konten.")
    print("\n1. Tambah konten\n2. Lihat konten\n3. Keluar")
    pilihan = input("Pilih: ").strip()

    if pilihan == "1":
        tambah_konten(konten)
    elif pilihan == "2":
        lihat_konten(konten)
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak tersedia.")

