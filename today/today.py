today = input("What day?")
condition = input("How's the condition?")

if today == "Saturday":
    print("Party!")
elif today == "Sunday":
    if condition == "Headache":
        print("Recover, then rest.")
    else:
        print("Rest")
else:
    print("Work, work, work!")  