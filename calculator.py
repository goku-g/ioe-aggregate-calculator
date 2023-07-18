def calculate_percentage(fm, om):
    percent = []
    for i in range(len(fm)):
        per = (om[i]/fm[i]) * 100
        percent.append(per)
    
    return percent

def calculate_aggregate(percent):
    sum = 0
    for i in range(len(percent)):
        if i <= 3:
            sum += percent[i] * 0.1
            
        else:
            sum += percent[i] * 0.15
            
    return sum

def with_marks():
    full_marks = []
    obtained_marks = []
    for sem in range(8):
        print(f"Enter Your {sem+1} Semesters Marks")
        fm = float(input("Full Marks:\t"))
        om = float(input("Obtained Marks:\t"))

        full_marks.append(fm)
        obtained_marks.append(om)

    percentages = calculate_percentage(full_marks, obtained_marks)

    return percentages

def with_percent():
    percentages = []
    for sem in range(8):
        per = float(input(f"Enter Your {sem+1} Semester's Percentage:\t"))
        percentages.append(per)

    return percentages


def main():
    print("If you want to calculate from full marks and obtained marks then type 'M',")
    print("If you want to calculate from percentages then type 'P' and to quit type 'Q'")
    var = input("Input:\t")

    if(var.upper() == 'M'):
        percentages = with_marks()

    elif(var.upper() == 'P'):
        percentages = with_percent()
    
    else:
        exit()

    aggrigate = calculate_aggregate(percentages)

    print(f"\nYour Aggrigate Percentage is {aggrigate}%!!")

if __name__ == '__main__':
    main()