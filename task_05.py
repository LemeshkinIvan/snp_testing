from datetime import datetime, timedelta

def date_in_future(value):
    try:
        integer = int(value)

        now = datetime.now()
        value_to_date = timedelta(value)
        new_date = now + value_to_date

        return (new_date.strftime("%d-%m-%Y %H:%M:%S"))
    except:
        return []
    
# for test
print(date_in_future([]))
print(date_in_future(2))