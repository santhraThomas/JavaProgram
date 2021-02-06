with open("openfolder.txt", 'r') as fields:
    totGpa = 0.00
    counter = 0
    for line in fields:
        fields = line.split(" ",3)
        fname = fields[0]
        lname = fields[1]
        gpa = fields[2]
        classNum = fields[3]
        print("First name : ", fname, "Last Name : ", lname, "GPA: ", gpa,"Class Number : ", classNum)
        counter += 1
        if gpa == 'A':
            totGpa += 4
        elif gpa == 'B':
            totGpa += 3
        elif gpa == 'C':
            totGpa += 2
        elif gpa == 'D':
            totGpa += 1
        elif gpa == 'E':
            totGpa += 0
    print("\n------------")
    print("Total students scored: ",counter)
    print("Average score of students: ", (totGpa / counter))
    print("------------")
#fields.close()
