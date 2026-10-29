def status_kelulusan(nilai, kehadiran):
    # Perbaikan: Menggunakan '>=' bukan '>' pada kondisi nilai agar sesuai spesifikasi
    if nilai >= 70 and kehadiran >= 75:
        return "Lulus"
    return "Tidak Lulus"