from datetime import date
import random
import bday_messages

today = date.today()
print("--- Birthday Countdown ---")
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))

target_year = today.year
next_birthday = date(target_year, month, day)

if next_birthday < today:
    next_birthday = date(target_year + 1, month, day)

days_away = (next_birthday - today).days

if days_away == 0:
    print("\n🎉 Happy Birthday! It's today! 🎉")
else:
    print(f"\nYour birthday is {days_away} days away!")

random_msg = random.choice(bday_messages.bday_messages)
print(f"Message for you: {random_msg}")
