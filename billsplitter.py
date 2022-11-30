bill = input("what's total bill?: ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
bill_convert = float( bill)
tip_convert = int(tip)/100
split_convert = int(split)

split= input("How many people to split the bill?") 
finaltip= (bill_convert / split_convert) * tip_convert
ffinal= (bill_convert / split_convert) + finaltip
final= round(ffinal, 2)
print( "Each person should pay:" + str(final) )
