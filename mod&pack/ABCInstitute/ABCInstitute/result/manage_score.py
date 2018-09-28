def get_average_score(marks1, marks2, marks3):
    average = (marks1 + marks2 + marks3) / 3
    print("Average is: ", average)
    
def get_grade(average):
    if average > 60:
        grade = "A"
    else:
        grade = "B"
    return grade

