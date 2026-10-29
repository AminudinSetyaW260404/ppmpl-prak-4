def evaluate_score(score, attendance):
    if attendance < 75:
        return "Tidak Lulus (Kehadiran)"
    
    if score >= 85:
        return "Lulus Sangat Memuaskan"
    elif score >= 70:
        return "Lulus Memuaskan"
    else:
        return "Tidak Lulus (Nilai)"