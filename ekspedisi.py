def hitung_biaya(panjang, lebar, tinggi, berat, lokasi):
    """Fungsi untuk menghitung biaya pengiriman berdasarkan dimensi, berat paket, dan lokasi pengiriman."""
    
    # Memeriksa apakah lokasi termasuk dalam area Pasuruan
    if lokasi.lower() not in ["kota pasuruan", "kabupaten pasuruan"]:
        return "Layanan ekspedisi hanya tersedia di Kota dan Kabupaten Pasuruan."

    # Menentukan biaya per kg berdasarkan dimensi
    if panjang <= 50 and lebar <= 50 and tinggi <= 50:
        biaya_per_kg = 5000
        biaya_tambahan = 0  # Tidak ada biaya tambahan
    else:
        biaya_per_kg = 7000
        biaya_tambahan = 50000  # Biaya tambahan untuk dimensi besar

    # Menghitung total biaya
    total_biaya = biaya_per_kg * berat
    
    # Jika berat 1 kg atau kurang, biaya minimum
    if berat <= 1:
        total_biaya = 8000

    # Menambahkan biaya tambahan jika berlaku
    total_biaya += biaya_tambahan

    return total_biaya

# Input dimensi, berat paket, dan lokasi pengiriman
panjang = int(input("Masukkan panjang paket (cm): "))
lebar = int(input("Masukkan lebar paket (cm): "))
tinggi = int(input("Masukkan tinggi paket (cm): "))
berat = float(input("Masukkan berat paket (kg): "))
lokasi = input("Masukkan lokasi pengiriman (Kota Pasuruan/Kabupaten Pasuruan): ")

# Hitung biaya pengiriman
biaya = hitung_biaya(panjang, lebar, tinggi, berat, lokasi)

# Tampilkan biaya pengiriman
print("Biaya pengiriman:", biaya, "rupiah")           
                    
            
    
   
    
    