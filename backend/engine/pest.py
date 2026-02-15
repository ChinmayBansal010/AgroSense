
def pest_risk(temp, humidity):
    if humidity > 70 and temp > 25: return "High pest risk"
    if humidity > 60: return "Moderate pest risk"
    return "Low pest risk"
