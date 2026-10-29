def harga_akhir(harga_awal, kode_promo, is_member):
    diskon = 0.0
    
    if kode_promo == "HEMAT10":
        diskon = 0.10
    elif kode_promo == "HEMAT20":
        diskon = 0.20
    
    if is_member:
        diskon += 0.05  # Bug telah diperbaiki (diubah dari "0.05" ke 0.05)
        
    return harga_awal * (1 - diskon)