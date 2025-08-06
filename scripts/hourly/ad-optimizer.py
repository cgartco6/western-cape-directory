# scripts/hourly/ad-optimizer.py
def adjust_pricing():
    traffic = get_peak_hours()
    for town in traffic:
        new_price = base_price * (1 + (traffic[town]['demand'] / 10))
        update_database_pricing(town, new_price)
