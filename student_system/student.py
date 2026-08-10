def add_student(students,name,age,score):     #因为一次只更新一个学生所以这里用add_student()意思更好
    student={
        "name":name,
        "age":age,
        "score":score
    }
    students.append(student)

def show_students(students):
    for student in students:
        print("姓名: %s" % student["name"])
        print("年龄: %s" % student["age"])
        print("成绩: %s" % student["score"])

def delete_student(students,name):
    for student in students:           #遍历
        if student["name"] == name:    #name找到目标词典
            students.remove(student)   #消除词典          #不需要break
            return True                #加入bool来判断真假
    return False                         #直接中断  