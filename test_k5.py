import pytest
from k5_studi_kasus import hitung_ongkir

def test_berat_invalid():
    # Menguji exception saat berat <= 0
    with pytest.raises(ValueError):
        hitung_ongkir(0, "Jakarta")

def test_jakarta_regular():
    # Menguji pengiriman ke Jakarta tanpa express
    assert hitung_ongkir(2, "Jakarta", False) == 20000

def test_bandung_express():
    # Menguji pengiriman ke Bandung dengan express
    assert hitung_ongkir(1, "Bandung", True) == 32000

def test_surabaya_regular():
    # Menguji pengiriman ke Surabaya tanpa express
    assert hitung_ongkir(1, "Surabaya", False) == 15000

def test_luar_jawa_express():
    # Menguji kota lainnya dengan express
    assert hitung_ongkir(2, "Medan", True) == 60000