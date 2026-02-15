
def harvest(stage, market_signal):
    if stage == "Maturity" and market_signal == "SELL":
        return "Harvest and sell now"
    if stage == "Maturity":
        return "Harvest possible, monitor prices"
    return "Harvest not recommended"
