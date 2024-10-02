gender = input("Enter your gender: ")
hemoglobin = int(input("Enter your hemoglobin: "))
if gender == "female":
    if hemoglobin < 117:
        print("Low hemoglobin")
    elif 117 <= hemoglobin <= 155:
        print("Normal hemoglobin")
    elif hemoglobin > 155:
        print("High hemoglobin")
if gender == "male":
    if hemoglobin < 134:
        print("Low hemoglobin")
    elif 134 <= hemoglobin <= 167:
        print("Normal hemoglobin")
    elif hemoglobin > 167:
        print("High hemoglobin")
