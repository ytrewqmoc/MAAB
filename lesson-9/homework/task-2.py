import csv

grades_data = {}
subjects_count = {}

with open("grades.csv", 'r') as csvfile:
    content = csv.DictReader(csvfile)
    for row in content:
        subject = row['Subject']
        grade = float(row['Grade'])
        
        if subject not in grades_data:
            grades_data[subject] = 0
            subjects_count[subject] = 0
        
        grades_data[subject] += grade
        subjects_count[subject] += 1

average_grades = {subject: round(grades_data[subject] / subjects_count[subject], 2) for subject in grades_data}

with open("average_grades.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Subject', 'Grade'])  
    for subject, avg in average_grades.items():
        writer.writerow([subject, avg])

print("Process finished")
