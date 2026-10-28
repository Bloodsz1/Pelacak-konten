semua = [
    {"judul": "Belajar Python", "tanggal_upload": "2026-10-28", "konsep": "storytelling", "views": 1500},
    {"judul": "Review Produk", "tanggal_upload": "2026-10-29", "konsep": "review", "views": 800},
]
for item in semua:
    print(f"{item['judul']:<20} | {item['konsep']:<17} | {item['views']:<7} Views")
