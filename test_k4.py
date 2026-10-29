import pytest
from k4_path import evaluate_score

def test_tidak_lulus_kehadiran():
    # Jalur 1: Kehadiran < 75
    assert evaluate_score(90, 70) == "Tidak Lulus (Kehadiran)"

def test_lulus_sangat_memuaskan():
    # Jalur 2: Kehadiran >= 75 dan score >= 85 (nilai batas 85)
    assert evaluate_score(85, 75) == "Lulus Sangat Memuaskan"

def test_lulus_memuaskan():
    # Jalur 3: Kehadiran >= 75 dan 70 <= score < 85 (nilai batas 70)
    assert evaluate_score(70, 80) == "Lulus Memuaskan"

def test_tidak_lulus_nilai():
    # Jalur 4: Kehadiran >= 75 dan score < 70 (nilai batas 69)
    assert evaluate_score(69, 100) == "Tidak Lulus (Nilai)"