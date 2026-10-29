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
    if not daftar_konten:
        print ("Data belum tersedia")
    else :
        urut = sorted(daftar_konten, key=lambda item: item["views"],reverse=True)
        print(f"\n{'Judul':<22} | {'Konsep':<17} | {'Views':<7}")
        print("=" * 60)
        nomor = 1
        for item in urut:
            print(f"{nomor} {item['judul']:<20} | {item['konsep']:<17} | {item['views']:<7} Views")
            nomor += 1

def hapus_konten(daftar_konten):
    try:
        if not daftar_konten:
            print("Tidak ada konten yang tersedia")
        else:
            urut = sorted(daftar_konten, key=lambda item: item["views"],reverse=True)
            print(f"\n{'Judul':<22} | {'Konsep':<17} | {'Views':<7}")
            print("=" * 60)
            nomor = 1
            for item in urut:
                print(f"{nomor} {item['judul']:<20} | {item['konsep']:<17} | {item['views']:<7} Views")
                nomor += 1

        hapus_nomor = int(input("\nMasukkan nomor tugas yang ingin dihapus: ").strip())
        if 1 <= hapus_nomor <= len(daftar_konten):
            index = hapus_nomor - 1
            yakin = input("Apakah Anda yakin ingin menghapus tugas ini? (y/n): ").strip().lower()
            if yakin == 'y':
                del daftar_konten[index]
                simpan_konten(daftar_konten)
                print("Nomor konten yang dihapus: ", hapus_nomor)
            else:
                print("Penghapusan konten dibatalkan.")
        else:
            print("Nomor konten tidak valid")
    except (IndexError, ValueError):
        print("Input tidak valid. Harap masukkan nomor konten yang benar.")


konten = muat_konten()

while True:
    print("\n")
    print("="*40)
    print("Selamat datang di program pelacak konten.")
    print("\n1. Tambah konten\n2. Lihat konten\n3. Hapus konten\n4. Keluar")
    pilihan = input("Pilih: ").strip()

    if pilihan == "1":
        tambah_konten(konten)
    elif pilihan == "2":
        lihat_konten(konten)
    elif pilihan == "3":
        hapus_konten(konten)
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak tersedia.")

