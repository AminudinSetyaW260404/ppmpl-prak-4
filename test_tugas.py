import pytest
from tugas import status_kelulusan

def test_lulus_normal():
    # True AND True -> Lulus
    assert status_kelulusan(80, 80) == "Lulus"

def test_lulus_nilai_batas():
    # Nilai batas 70 dan 75 -> Membuktikan perbaikan bug
    assert status_kelulusan(70, 75) == "Lulus"

def test_gagal_nilai_kurang():
    # False AND True -> Tidak Lulus
    assert status_kelulusan(69, 80) == "Tidak Lulus"

def test_gagal_kehadiran_kurang():
    # True AND False -> Tidak Lulus
    assert status_kelulusan(80, 74) == "Tidak Lulus"

def test_gagal_keduanya():
    # False AND False -> Tidak Lulus
    assert status_kelulusan(50, 50) == "Tidak Lulus"