def calculate_grade():
    try:
        
        physics = float(input("Enter Physics mark: "))
        math = float(input("Enter Math mark: "))
        kiswahili = float(input("Enter Kiswahili mark: "))


        if physics < 0 or math < 0 or kiswahili < 0:
            return "Error: Marks cannot be negative."

        # Calculate the average
        average = (physics + math + kiswahili) / 3


        if average > 100:
            return "Error: Average exceeds 100, which is not possible."

                if average >= 80:
            grade = 'A'
        elif average >= 70:
            grade = 'B'
        elif average >= 60:
            grade = 'C'
        elif average >= 50:
            grade = 'D'
        else:
            grade = 'F'

        return f"Average: {average:.2f}, Grade: {grade}"

    except ValueError:

        return "Error: Please enter valid numbers for the marks."

result = calculate_grade()
print(result)
