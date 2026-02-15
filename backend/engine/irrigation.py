
def irrigation(stage, rainfall):
    if rainfall > 5: return "No irrigation today"
    if stage in ["Germination", "Flowering"]: return "Light irrigation recommended"
    return "Irrigation optional"
