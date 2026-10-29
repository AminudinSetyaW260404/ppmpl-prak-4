def validate_login(username, password, is_active):
    # Menguji ekspresi majemuk dengan operator AND
    if username == "admin" and password == "secret123" and is_active:
        return "Login Berhasil"
    return "Login Gagal"