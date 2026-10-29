def hitung_diskon(total_belanja, is_member):
    diskon = 0.0
    if is_member:
        if total_belanja > 500000:
            diskon = 0.20
        else:
            diskon = 0.10
    else:
        if total_belanja > 500000:
            diskon = 0.05
        else:
            diskon = 0.0
            
    return total_belanja * (1 - diskon)