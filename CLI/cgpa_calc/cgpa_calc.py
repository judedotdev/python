def gpa1_display():
    global total
    global gtotal
    total = 0
    gtotal = 0
    grades = {"a": "5", "A": "5", "b": "4", "B": "4", "c": "3",
              "C": "3", "d": "2", "D": "2", "e": "1", "E": "1", "f": "0", "F": "0"}
    name = input("\n Enter the student name:")
    dept = input("\n Enter the department:")
    year = input("\n Enter the Year of student:")
    sem1 = "FIRST SEMESTER"
    print("This will compute result for your First Semester")
    n = int(input("\n Enter the No. of Courses for First Semester:"))
    marks = []
    for entry in range(n):
        sc = input("\n Enter the subject code:")
        ma = input("\n Enter the grades in (A-F):")
        g = float(input("\n Enter the Credit Unit:"))
        if ma in grades:
            m = float(grades[ma])
            ma = ma.upper()
            entry = (sc, g, m, ma)
            marks.append(entry)
            if ma == "F":
                mn = "0"
            else:
                mn = "1"
    if mn == "0":
        print("\n\tNAME:", name, "\t\tDEPARTMENT:", dept)
        print("\n\tYEAR:", year, "\t\tSEMESTER:", sem1)
        print("\n Subject code          Grade")
        for entry in marks:
            sc, g, m, ma = entry
            print("\n\t", sc, "\t\t", ma)
        print("\n\nGPA=ARREAR")
    else:
        print("\n\tNAME:", name, "\t\tDEPARTMENT:", dept)
        print("\n\tYEAR:", year, "\t\tSEMESTER:", sem1)
        print("\n Subject code          Grade")
        for entry in marks:
            sc, g, m, ma = entry
            print("\n\t", sc, "\t\t", ma)
            total = total+m*g
            gtotal = gtotal+g
        gpa1 = total/gtotal
        print("\n\nGPA=", gpa1)


gpa1_display()


def gpa2_display():
    total2 = 0
    gtotal2 = 0
    grades2 = {"a": "5", "A": "5", "b": "4", "B": "4", "c": "3",
               "C": "3", "d": "2", "D": "2", "e": "1", "E": "1", "f": "0", "F": "0"}
    name2 = input("\n Enter the student name:")
    dept2 = input("\n Enter the department:")
    year2 = input("\n Enter the Year of student:")
    sem2 = "SECOND SEMESTER"
    print("This will compute result for your Second Semester")
    n2 = int(input("\n Enter the No. of Courses for Second Semester:"))
    marks2 = []
    for entry in range(n2):
        sc2 = input("\n Enter the subject code:")
        ma2 = input("\n Enter the grades in (A-F):")
        g2 = float(input("\n Enter the Credit Unit:"))
        if ma2 in grades2:
            m2 = float(grades2[ma2])
            ma2 = ma2.upper()
            entry = (sc2, g2, m2, ma2)
            marks2.append(entry)
            if ma2 == "F":
                mn2 = "0"
            else:
                mn2 = "1"
    if mn2 == "0":
        print("\n\tNAME:", name2, "\t\tDEPARTMENT:", dept2)
        print("\n\tYEAR:", year2, "\t\tSEMESTER:", sem2)
        print("\n Subject code          Grade")
        for entry in marks2:
            sc2, g2, m2, ma2 = entry
            print("\n\t", sc2, "\t\t", ma2)
        print("\n\nGPA=ARREAR")
    else:
        print("\n\tNAME:", name2, "\t\tDEPARTMENT:", dept2)
        print("\n\tYEAR:", year2, "\t\tSEMESTER:", sem2)
        print("\n Subject code          Grade")
        for entry in marks2:
            sc2, g2, m2, ma2 = entry
            print("\n\t", sc2, "\t\t", ma2)
            total2 = total2+m2*g2
            gtotal2 = gtotal2+g2
        gpa2 = total2/gtotal2
        print("\n\nGPA=", gpa2)
        cgpa = (total+total2)/(gtotal+gtotal2)
        print("\n\nCGPA=", cgpa)


gpa2_display()
input("\n Press enter key to exit....")
