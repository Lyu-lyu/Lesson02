
School = [
    {'Grade':'11', 'Result': [3,4,5,2,4,2,5]},
    {'Grade':'10', 'Result': [5,4,5,2,3,4]},
    {'Grade':'9', 'Result': [3,4,5,2,5,5,5,3,5]},
    {'Grade':'8', 'Result': [2,4,5,3,2,2]}
    ]

Student_sum = 0 
School_score = 0
for element in School:
    Cur_class_students = len(element['Result'])
    Student_sum += Cur_class_students
    Cur_class_score = 0
    for Score in element['Result']:
        Cur_class_score += Score
        School_score += Score
    if Cur_class_students == 0:
        Average_class == 0
    else:    
        Average_class = round (Cur_class_score / Cur_class_students, 1)
    print ('Средняя оценка по классу {}: {}.'.format (element['Grade'], Average_class))

Average = round (School_score / Student_sum, 1)
print ('Средняя оценка по школе:', Average)