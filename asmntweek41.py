def calculate_grade(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Error, please enter numeric input between 0 and 100."

try:
    score = int(input("Enter score: "))
    result = calculate_grade(score)
    
    print(result) 
except ValueError:
    print("Error, please enter numeric input between 0 and 100.")



