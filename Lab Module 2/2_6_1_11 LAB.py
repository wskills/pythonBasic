hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
end_hour = str((hour+((mins+dura)//60))%24)
end_mins = str((mins+dura)%60)
print("Event will end at: " + end_hour + ":" + end_mins)