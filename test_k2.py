import pytest
from k2_branch import harga_akhir

def test_promo_hemat10_non_member():
    assert harga_akhir(100000, "HEMAT10", False) == 90000.0

def test_promo_hemat20_member():
    assert harga_akhir(100000, "HEMAT20", True) == 75000.0

def test_tanpa_promo_member():
    assert harga_akhir(100000, "LAINNYA", True) == 95000.0

def test_tanpa_promo_non_member():
    assert harga_akhir(100000, "LAINNYA", False) == 100000.0