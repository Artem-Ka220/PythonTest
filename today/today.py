today = input("What day?")

if today == "Saturday":
    print("Party!")
elif today == "Sunday":
    condition = input("How's the condition?")
    if condition == "Headache":
        print("Recover, then rest.")
    else:
        print("Rest")
else:
    print("Work, work, work!")  