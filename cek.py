kategori = [
    {"judul": "Bakwan", "konsep": "vlog"},
    {"judul": "Bakso", "konsep": "vlog"},
    {"judul": "Laptop", "konsep": "Tutorial"},
    {"judul": "Kaos", "konsep": "review"},
]

hitung = {}
for b in kategori:
    konsep = b["konsep"]

    if konsep in hitung:
        hitung[konsep] += 1
    else:
        hitung[konsep] = 1

print(hitung)
