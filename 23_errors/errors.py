def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


grades = []

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
except ValueError:
    print("grades must be numbers")
else:
    print(f"The average grade is {average}")
finally:
    print("THE END")
