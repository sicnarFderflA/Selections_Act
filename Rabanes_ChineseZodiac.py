year = int(input("Enter Year: "))

ans = year % 12 + 1

# print(ans)

if ans == 11:
   sign = ("Horse")
elif ans == 12:
   sign = ("Goat")
elif ans == 1:
   sign = ("Monkey")
elif ans == 2:
   sign = ("Rooster")
elif ans == 3:
   sign = ("Dog")
elif ans == 4:
   sign = ("Pig")
elif ans == 5:
   sign = ("Rat")
elif ans == 6:
   sign = ("Ox")
elif ans == 7:
   sign = ("Tiger")
elif ans == 8:
   sign = ("Rabbit")
elif ans == 9:
   sign = ("Dragon")
else:
   sign = ("Snake")

print("The Chinese Zodiac Sign of the year", year , "is", sign)