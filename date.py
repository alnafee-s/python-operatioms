#wirte a python code to print current date in different format

from datetime import date
current_date=date.today()
formatted_date=current_date.strftime("%m-%d-%y")
print("current date is",current_date)
print("formated date is",formatted_date)




