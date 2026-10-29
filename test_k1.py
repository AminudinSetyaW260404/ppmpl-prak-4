import pytest
from k1_statement import hitung_diskon

def test_member_belanja_besar():
    assert hitung_diskon(600000, True) == 480000.0

def test_member_belanja_kecil():
    assert hitung_diskon(200000, True) == 180000.0

def test_non_member_belanja_besar():
    assert hitung_diskon(600000, False) == 570000.0

def test_non_member_belanja_kecil():
    assert hitung_diskon(200000, False) == 200000.0