#days={
   #"1":"Jan-31",
   #"3":"Mar-31",
   #"5":"May-31",
   #"6":"Jun-30",
   #"7":"Jul-31",
   #"8":"Aug-31",
   #"9":"Sep-30",
   #"10":"Oct-31",
   #"11":"Nov-30",
   #"12":"Dec-31"
#}
#year=int(input("Enter the year:"))
#month=input("Enter the month:")
#if ((year%4==0 and (year%400==0 or year%100!=0)) and month=="2"):
 #  print("Feb:29")
#else:
#   print(days[month])#
   
print("////Displaying Calendar////")
import calendar
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
calendar=calendar.month(year,month)
print(calendar)
