
def compute_risk_score(rainfall, humidity, temperature):
    score = 0.0
    if rainfall > 10: score += 0.4
    elif rainfall > 5: score += 0.2
    if humidity > 70: score += 0.3
    elif humidity > 60: score += 0.2
    if temperature > 30: score += 0.3
    elif temperature > 25: score += 0.2
    return round(min(score, 1.0), 2)
