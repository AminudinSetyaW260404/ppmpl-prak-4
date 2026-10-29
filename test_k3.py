import pytest
from k3_condition import validate_login

def test_login_sukses():
    # True AND True AND True -> Valid
    assert validate_login("admin", "secret123", True) == "Login Berhasil"

def test_username_salah():
    # False -> Short-circuit terjadi di username (password & is_active tidak dievaluasi)
    assert validate_login("user", "secret123", True) == "Login Gagal"

def test_password_salah():
    # True AND False -> Evaluasi berhenti di password
    assert validate_login("admin", "wrongpass", True) == "Login Gagal"

def test_user_tidak_aktif():
    # True AND True AND False -> Semua ekspresi dievaluasi
    assert validate_login("admin", "secret123", False) == "Login Gagal"