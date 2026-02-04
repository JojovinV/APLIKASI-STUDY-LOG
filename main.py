catatan = []
target_harian = None

def tambah_catatan():
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()
    while True:
        durasi_input = input("Durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("Durasi harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("Durasi harus berupa angka (menit). Coba lagi.")

    catatan.append({
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi,
    })
    print("Catatan tersimpan.")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    print("\n=== Daftar Catatan Belajar ===")
    for i, c in enumerate(catatan, 1):
        mapel = c.get("mapel", "-")
        topik = c.get("topik", "-")
        durasi = c.get("durasi", 0)
        print(f"{i}. Mapel: {mapel} | Topik: {topik} | Durasi: {durasi} menit")
    print(f"Total catatan: {len(catatan)}")

def total_waktu():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    total = 0
    for c in catatan:
        try:
            total += int(c.get("durasi", 0))
        except (ValueError, TypeError):
            continue

    print(f"Total waktu belajar: {total} menit")

def set_target_harian():
    global target_harian
    while True:
        inp = input("Masukkan target harian (menit): ").strip()
        try:
            t = int(inp)
            if t <= 0:
                print("Target harus lebih dari 0.")
                continue
            target_harian = t
            print(f"Target harian disimpan: {target_harian} menit")
            break
        except ValueError:
            print("Masukkan angka valid untuk menit. Coba lagi.")

def lihat_target_harian():
    if target_harian is None:
        print("Belum ada target harian.")
    else:
        total = 0
        for c in catatan:
            try:
                total += int(c.get("durasi", 0))
            except (ValueError, TypeError):
                continue

        print(f"Target harian: {target_harian} menit")
        print(f"Total hari ini: {total} menit")
        if total >= target_harian:
            print("Selamat! Target harian tercapai atau terlampaui.")
        else:
            sisa = target_harian - total
            print(f"Sisa untuk mencapai target: {sisa} menit")

    ubah = input("Ingin mengubah target? (y/n): ").strip().lower()
    if ubah == "y":
        set_target_harian()

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Target harian")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "5":
        lihat_target_harian()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")