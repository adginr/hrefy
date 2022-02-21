from datetime import datetime, timedelta


def get_expires_dt(days: int):
    """Return datetime after today + days"""
    return datetime.now() + timedelta(days)
