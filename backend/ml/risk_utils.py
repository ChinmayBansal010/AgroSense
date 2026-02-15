
def risk_label(score):
    if score >= 0.7: return "High"
    if score >= 0.4: return "Medium"
    return "Low"
