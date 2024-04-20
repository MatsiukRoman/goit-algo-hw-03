from datetime import datetime 

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date,"%Y-%m-%d")
        current_datetime = datetime.today()
        days_ahead = abs(current_datetime.date() - input_date.date())
        return days_ahead.days
    except Exception as e:
        return ("Exception: ", e)

print(get_days_from_today("2021-01-09"))
