import datetime
today=datetime.datetime.today()
with open("inClass.txt", "r") as fName:
    lines = fName.readlines()
    for line in lines:
        record=line.split(",")
        fName = record[0]
        lName = record[1]
        bDay = datetime.datetime.strptime(record[2], "%m-%d-%Y")
        dDay = record[3]
        context = "was"
        if dDay == "":
            context = "has been"
            a=today-bDay
        else:
            dDay = datetime.datetime.strptime(record[3], "%m-%d-%Y")
            a=dDay-bDay
        company = record[4]
        product = record[5]
        netWorth = record[6]
        days = a.days
        print(fName, lName, context, "alive", days, "days")
        # calculate the total days each person has been alive including leap year
