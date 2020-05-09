students = [['a', 123], ['b', 211], ['c', 100], ['d', 101]]

def second_highest(students):
    grades = [s[1] for s in students] # 只把成績拿出來
    grades = sorted(grades, reverse = True)
    second = grades[1] # grades[0]是最高，grades[1]是第二高
    
    second_high_students = [s[0] for s in students if s[1] == second]
    for student in second_high_students:
        print(student)
second_highest(students)