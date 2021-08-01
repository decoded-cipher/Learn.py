from datetime import date

def findAge(current_date, current_month, current_year, birth_date, birth_month, birth_year):
     
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[birth_month-1]
         
    if (birth_month > current_month):        
        current_year = current_year - 1
        current_month = current_month + 12
         
    # calculate date, month, year
    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year
     
    # print present age
    print("\nHurray! You are", calculated_year, "Years", calculated_month, "Months &", calculated_date, "Days old.")

print('\nWELCOME TO INOVUS AGE CALCULATOR\n')
birth_year = int(input('Enter the Year that you were born : '))
birth_month = int(input('Enter the Month that you were born : '))
birth_date = int(input('Enter the Date that you were born : '))

current_year = date.today().year
current_month = date.today().month
current_date = date.today().day

findAge(current_date, current_month, current_year, birth_date, birth_month, birth_year)
