
age = input("What is your current age? ")


max_years = 90
days = ( max_years * 365 ) 
weeks = ( max_years * 52 ) 
months = ( max_years * 12 ) 

udays = ( int(age) * 365 ) 
uweeks = ( int(age) * 52 ) 
umonths = ( int(age) * 12 ) 

user_days = days - udays
user_weeks = weeks - uweeks
user_months = months -  umonths

user_weeks_int = int(user_weeks) 

print (f"You have {user_days} days, {user_weeks_int} weeks, and {user_months} months left.")


