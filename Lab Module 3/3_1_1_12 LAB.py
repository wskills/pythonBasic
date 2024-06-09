year = int(input("Enter a year: "))

gregorian_calendar = 1582

if year >= gregorian_calendar:
    if (year%4) != 0:
        print("Common year")
    elif (year%100) != 0 :
        print("Leap year")
    elif (year%400) != 0:
        print("Common year")
    else:
        print("Leap year")
else:
    print("Not within the Gregorian calendar period")