from datetime import datetime, timedelta

# починил
def date_in_future(value):
    now = datetime.now()
    try:
        integer = int(value)
        value_to_date = timedelta(value)
        new_date = now + value_to_date

        return (new_date.strftime("%d-%m-%Y %H:%M:%S"))
    except:
        return (now.strftime("%d-%m-%Y %H:%M:%S"))
    
# for test
print(date_in_future([]))
print(date_in_future(2))