def takeInput():
    termsNum = int(input("How many Semesters have you finished in FCI ?\n"))
    numOfSub = 0
    if termsNum > 6:
        tmp = termsNum - 6
        termsNum -= tmp
        numOfSub = (termsNum*6) + (tmp*5)
    else:
        numOfSub = termsNum*6
    curGPA = float(input("Enter your current GPA : "))
    #print(numOfSub)
    return curGPA * float(numOfSub), numOfSub

def update(v, sub):
    numOfSub = int(input("How many subjects do you have:\n "))
    records = []
    s=""
    print("Enter your grades in capitals: ")
    for i in range(0, numOfSub):
        s = input()
        records.append(s)
    for i in records:
        if i == "A+":
            v += 4.00
        elif i == "A":
            v += 3.70
        elif i == "B+":
            v += 3.5
        elif i == "B":
            v += 3.00
        elif i == "C+":
            v += 2.70
        elif i == "C":
            v += 2.50
        elif i == "D+":
            v += 2.20
        elif i == 'D':
            v += 2.00
    return v / (sub+numOfSub)

if __name__ == '__main__':
    v, sub = takeInput()
    #print(v)
    #print(sub)
    l = update(v, sub)
    print("Your Updated GPA is "+'%.2f'%l)

