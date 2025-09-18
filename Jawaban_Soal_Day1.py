# =========================
# 1. Marathon Netflix
# =========================
print("=== Soal 1: Marathon Netflix ===")
durasi_episode = int(input("Masukkan durasi 1 episode (menit): "))
jumlah_episode = int(input("Masukkan jumlah episode: "))

total_menit = durasi_episode * jumlah_episode
total_jam = total_menit / 60
print(f"Total waktu menonton: {total_menit} menit atau {total_jam:.2f} jam\n")


# =========================
# 2. Membeli Cupang dan Koi
# =========================
print("=== Soal 2: Membeli Cupang & Koi ===")
nim_3 = int(input("Masukkan 3 angka terakhir NIM: "))
uang = (nim_3 + 100) * 1000  # Rp.XXX000
print(f"Uang yang dibawa: Rp {uang}")

harga_cupang = 10000
harga_koi = 20000

jumlah_cupang = int(input("Masukkan jumlah cupang yang dibeli: "))
jumlah_koi = int(input("Masukkan jumlah koi yang dibeli: "))

total_belanja = (jumlah_cupang * harga_cupang) + (jumlah_koi * harga_koi)
sisa_uang = uang - total_belanja

print(f"Total belanja: Rp {total_belanja}")
print(f"Sisa uang: Rp {sisa_uang}\n")


# =========================
# 3. Liburan naik motor
# =========================
print("=== Soal 3: Liburan Naik Motor ===")
nim_3 = int(input("Masukkan 3 angka terakhir NIM: "))
nim_last = int(input("Masukkan 1 angka terakhir NIM: "))

jarak = nim_3  # total km
bbm_perliter = 2.7
kapasitas_tangki = nim_last
harga_bensin = int("1" + str(nim_3) + "0")  # Rp.1XXX0

# Hitung total bensin yang dibutuhkan
total_bensin = jarak / bbm_perliter

# Cek diskon
if total_bensin > 3:
    harga_perliter = harga_bensin - 500
else:
    harga_perliter = harga_bensin

# Hitung total biaya bensin
total_biaya = total_bensin * harga_perliter

# Hitung berapa kali isi bensin
if kapasitas_tangki > 0:
    kali_isi = -(-total_bensin // kapasitas_tangki)  # ceil division
else:
    kali_isi = 0

print(f"Total bensin dibutuhkan: {total_bensin:.2f} liter")
print(f"Harga bensin per liter: Rp {harga_perliter}")
print(f"Total biaya bensin: Rp {total_biaya:.2f}")
print(f"Perkiraan isi bensin: {int(kali_isi)} kali (isi full setiap kali)\n")
