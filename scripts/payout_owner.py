import fnb_api
from datetime import datetime

def payout_owner():
    if datetime.today().weekday() == 0:  # Every Monday
        revenue = get_weekly_revenue()
        fnb_api.transfer(revenue * 0.7, "OWNER_FNB_ACCOUNT")  # 70% profit
        fnb_api.transfer(revenue * 0.3, "OPERATIONS_ACCOUNT")  # 30% reinvest

def get_weekly_revenue():
    return 5000  # Mock: R5000 weekly (AI will track real numbers)
