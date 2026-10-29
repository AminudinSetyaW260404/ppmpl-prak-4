def hitung_ongkir(berat_kg, kota_tujuan, express=False):
    if berat_kg <= 0:
        raise ValueError("Berat harus lebih besar dari 0")
    
    if kota_tujuan == "Jakarta":
        tarif = 10000
    elif kota_tujuan == "Bandung":
        tarif = 12000
    elif kota_tujuan == "Surabaya":
        tarif = 15000
    else:
        tarif = 20000
        
    total = berat_kg * tarif
    
    if express:
        total += 20000
        
    return total