import datetime
today = datetime.datetime.today()
print(today)
with open("inclass.txt", 'r') as fields:
    lines = fields.readlines()
    for line in lines:
        record = line.split(",")
        fName = record[0]
        lName = record[1]
        bDay = datetime.datetime.strptime(record[2], '%m-%d-%Y')
        dDay = record[3]
        context = "was"
        if dDay == "":
            context = "has been"
            a = today-bDay
        else:
            dDay = datetime.datetime.strptime(record[3], '%m-%d-%Y')
            a = dDay-bDay
        #if dDay = "", then context = "was" else context = "is"
        company = record[4]
        product = record[5]
        netWorth = record[6]
        a = today-bDay
        days = a.days
        print(fName, lName, context, "alive", days, "days")
