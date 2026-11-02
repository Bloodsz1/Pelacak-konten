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
    konsep = input("Konsep (misal: storytelling, review, tutorial): ").strip().lower()
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
        print("Data belum tersedia")
        return
    else:
        urut = sorted(daftar_konten, key=lambda item: item["views"], reverse=True)
        print(f"\n{'Judul':<22} | {'Konsep':<17} | {'Views':<7}")
        print("=" * 60)
        nomor = 1
        for item in urut:
            print(
                f"{nomor} {item['judul']:<20} | {item['konsep']:<17} | {item['views']:<7} Views"
            )
            nomor += 1


def hapus_konten(daftar_konten):
    if not daftar_konten:
        print("Tidak ada konten yang tersedia")
        return
    else:
        urut = sorted(daftar_konten, key=lambda item: item["views"], reverse=True)
        print(f"\n{'Judul':<22} | {'Konsep':<17} | {'Views':<7}")
        print("=" * 60)
        nomor = 1
        for item in urut:
            print(
                f"{nomor} {item['judul']:<20} | {item['konsep']:<17} | {item['views']:<7} Views"
            )
            nomor += 1
    while True:
        try:
            hapus_nomor = int(
                input("\nMasukkan nomor konten yang ingin dihapus: ").strip()
            )
            if 1 <= hapus_nomor <= len(urut):
                break
            else:
                print("Nomor konten tidak valid,coba lagi!")
        except (IndexError, ValueError):
            print("Input tidak valid. Harap masukkan nomor konten yang benar.")

    konten_dipilih = urut[hapus_nomor - 1]
    yakin = (
        input("Apakah Anda yakin ingin menghapus konten ini? (y/n): ").strip().lower()
    )
    if yakin == "y":
        daftar_konten.remove(konten_dipilih)
        simpan_konten(daftar_konten)
        print("Nomor konten yang dihapus: ", hapus_nomor)
    else:
        print("Penghapusan konten dibatalkan.")


def hitung_konsep(daftar_konsep):
    hitung = {}
    for b in daftar_konsep:
        konsep = b["konsep"]

        if konsep in hitung:
            hitung[konsep] += 1
        else:
            hitung[konsep] = 1
    return hitung


def ringkasan_konsep(daftar_konten):
    if not daftar_konten:
        print("Data belum tersedia")
        return

    hasil = hitung_konsep(daftar_konten)

    print(f"\n{'Konsep':<17} | {'Jumlah':<6}")
    print("=" * 26)
    for konsep, jumlah in hasil.items():
        print(f"{konsep:<17} | {jumlah:<6}")


def total_views_konsep(daftar_konten):
    total = {}
    for item in daftar_konten:
        konsep = item["konsep"]
        if konsep in total:
            total[konsep] += item["views"]
        else:
            total[konsep] = item["views"]
    return total


def dashboard_statistik(daftar_konten):
    """Menampilkan statistik keseluruhan konten."""

    if not daftar_konten:
        print("Data konten belum tersedia.")
        return

    total_konten = len(daftar_konten)

    total_views = sum(item["views"] for item in daftar_konten)

    rata_rata = total_views / total_konten

    konten_tertinggi = max(daftar_konten, key=lambda item: item["views"])

    konten_terendah = min(daftar_konten, key=lambda item: item["views"])

    print("\n" + "=" * 40)
    print("          DASHBOARD STATISTIK")
    print("=" * 40)

    print(f"Total konten       : {total_konten}")
    print(f"Total views        : {total_views:,}")
    print(f"Rata-rata views    : {rata_rata:,.2f}")

    print("\nKONTEN TERBAIK")
    print(f"Judul              : {konten_tertinggi['judul']}")
    print(f"Views              : {konten_tertinggi['views']:,}")

    print("\nKONTEN TERENDAH")
    print(f"Judul              : {konten_terendah['judul']}")
    print(f"Views              : {konten_terendah['views']:,}")

    print("=" * 40)


def analisis_performa(daftar_konten):
    """Menganalisis performa konten berdasarkan konsep."""

    if not daftar_konten:
        print("Data konten belum tersedia.")
        return

    analisis = {}

    for item in daftar_konten:
        konsep = item["konsep"]
        views = item["views"]

        if konsep not in analisis:
            analisis[konsep] = {"jumlah_konten": 0, "total_views": 0}

        analisis[konsep]["jumlah_konten"] += 1
        analisis[konsep]["total_views"] += views

    print("\n" + "=" * 45)
    print("          ANALISIS PERFORMA KONTEN")
    print("=" * 45)

    for konsep, data in analisis.items():
        rata_rata = data["total_views"] / data["jumlah_konten"]

        data["rata_rata"] = rata_rata

        print(f"\nKonsep: {konsep.upper()}")
        print(f"Jumlah konten : {data['jumlah_konten']}")
        print(f"Total views  : {data['total_views']:,}")
        print(f"Rata-rata    : {rata_rata:,.2f}")

    konsep_terbaik = max(analisis.items(), key=lambda item: item[1]["rata_rata"])

    print("\n" + "=" * 45)
    print("             KONSEP TERBAIK")
    print("=" * 45)

    print(f"Konsep       : {konsep_terbaik[0].upper()}")
    print(f"Rata-rata    : {konsep_terbaik[1]['rata_rata']:,.2f}")
    print("=" * 45)


konten = muat_konten()

while True:
    print("\n")
    print("=" * 40)
    print("Selamat datang di program pelacak konten.")
    print(
        "\n1. Tambah konten\n2. Lihat konten\n3. Hapus konten\n4. Ringkasan konsep\n5. Total views per konsep\n6. Dashboard Statistik\n7. Analisis Performa Konten\n8. Keluar"
    )
    pilihan = input("Pilih: ").strip()

    if pilihan == "1":
        tambah_konten(konten)
    elif pilihan == "2":
        lihat_konten(konten)
    elif pilihan == "3":
        hapus_konten(konten)
    elif pilihan == "4":
        ringkasan_konsep(konten)
    elif pilihan == "5":
        total_views_konsep(konten)
    elif pilihan == "6":
        dashboard_statistik(konten)
    elif pilihan == "7":
        analisis_performa(konten)
    elif pilihan == "8":
        break
    else:
        print("Pilihan tidak tersedia.")
print("Sekian terima gaji")
print("Terima kasih telah menggunakan program ini")
