#设计学生管理系统 V1.0
import json
import os
def add_students(students,name,age,score):
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

def save_students(students):
    data=json.dumps(students)            #()括号内放数据，外头用变量赋值
    file=open("students.json","w")       #注意w小写 and 什么数据就用什么名
    file.write(data)  
    file.close()

def delete_student(students,name):
    for student in students:           #遍历
        if student["name"] == name:    #name找到目标词典
            students.remove(student)   #消除词典
            break                      #直接中断

def load_students():
    file=open("students.json","r")    #读取保存好的学生数据。
    content=file.read()               #读取文件内容
    file.close()                      #关闭文件
    data=json.loads(content)          #JSON字符串转换
    return data                       #返回数据


def main():
    if os.path.exists("students.json"):
        students = load_students()
    else:
        students = []                   #在main函数中，main的局部变量，只有写在所有函数外面的变量才是全局变量   有个缺陷这里的需要加载数据
    while True:                                                                     
        print("==================\n")
        print("    学生管理系统   ")
        print("==================\n")
        choice=input("please choice a number:")
        if choice == "1":       
            name = input("please input a name:")         #先输入在判断合法性       
            if name=="":                
                print("error")
                continue          
            age = int(input("please input a age:"))
            if age<0 or age>100:
                print("error")
                continue
            score = float(input("please input a score:"))
            if score<=0 or score>100:
                print("error")
                continue
            add_students(students,name,age,score)
            save_students(students)                       #添加后不保存遇到突发情况数据直接消失
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            name = input("please input a name:")
            delete_student(students,name)
            save_students(students)
        elif choice == "4":
            save_students(students)
        elif choice =="5":
            if os.path.exists("students.json"):      #判断文件是否存在可以写在函数中
                print("文件存在")
            else:
                print("文件不存在")
                continue
            data=load_students()
            print(data)
        elif choice == "6":
            save_students(students)
            break
#优化点有很多   启动加载   load文件不存在处理   完善提示

main()

            



