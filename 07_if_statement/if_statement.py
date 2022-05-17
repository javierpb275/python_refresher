
def check_day_of_week(day_of_week):
    if day_of_week == "monday":
        print("Have a great start to your week")
    elif day_of_week == "tuesday":
        print("It's Tuesday!")
    else:
        print("Full speed ahead!")
    print("This always runs")


day_of_week = input("What day of the week is it today").lower()

check_day_of_week(day_of_week)


