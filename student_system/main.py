import student   #添加 删除 查看
import data      #save and load
import os
#main.py 负责用户交互和程序流程控制。
#student.add_student()负责创建 Student 对象并放入 students 列表。  所以我们再增加一个函数：add_student_flow()可以负责：完成一次“添加学生”的完整用户操作流程。




def input_score():
    while True:
        try:
            score = float(input("please input score:"))
        except ValueError:
            print("please input again")
            continue
        if score<0 or score>100:   #小优化点可以不要else 因为if执行了continue下面便不会执行
            print("error")
            continue  #直接进入下一轮 while
        return score

def input_age():
    while True:
        try:
            age = int(input("please input age:"))
        except ValueError:
            print("please input again")
            continue
        if age<0 or age>100:   #小优化点可以不要else 因为if执行了continue下面便不会执行
            print("error")
            continue
        return age

def input_name():
    while True:
        name = input("please input a name:")
        if name == "":
            print("please try again")
            continue
        return name

def add_student_flow(students):
    name = input_name()
    age = input_age() 
    score= input_score()
    student.add_student(students,name,age,score)
    data.save_students(students)

def delete_student_flow(students):
    name = input("please input a name:")       
    result=student.delete_student(students,name)         
    if result:
        print("删除成功")
    else:
        print("删除失败")
    data.save_students(students)

def update_score_flow(students):     #update_score_flow() 的职责是：完成“一次修改成绩操作” 所以执行完直接回到main菜单
        name = input("please input a name:")
        New_score=input_score()
        result=student.update_student_score(students, name, New_score)
        if result:
                print("成绩修改成功！")
                data.save_students(students)
        else:
            print("未找到该学生")
            


    




def main():
    # if os.path.exists("students.json"):
    #     students = data.load_students()
    # else:
    #     students = []                   #在main函数中，main的局部变量，只有写在所有函数外面的变量才是全局变量   有个缺陷这里的需要加载数据
    students = data.load_students()
    while True:                                                                     
        print("==================\n")
        print("    学生管理系统   ")
        print("==================\n")
        choice=input("please choice a number:")
        if choice == "1":       
        #     # name = input("please input a name:")         #先输入在判断合法性       
        #     # if name=="":                
        #     #     print("error")
        #     #     continue
        #     name = input_name()
        #     # try:          
        #     #     age = int(input("please input a age:"))         
        #     # except ValueError:                #这里可能出现值错误
        #     #     print("请重新输入")
        #     #     continue                      #输入异常会直接崩溃 and 如果异常必须continue
        #     # if age<0 or age>100:
        #     #     print("error")
        #     #     continue
        #     age = input_age()     #将上方代码组成函数
        #     # try:
        #     #     score = float(input("please input a score:"))
        #     # except ValueError:              #可能出现值错误
        #     #     print("请重新输入")
        #     #     continue
        #     # if score<0 or score>100:       #小优化把=0删去了
        #     #     print("error")
        #     #     continue
        #     score= input_score()
        #     student.add_student(students,name,age,score)
        #     data.save_students(students)
            add_student_flow(students)                       #新封装的函数添加工作流
        elif choice == "2":
            student.show_students(students)
        elif choice == "3":
                # name = input("please input a name:")       #这里try except没意义因为本身他输入的就是字符串
                # result=student.delete_student(students,name)           #这里需要给出参数
                # if result:
                #     print("删除成功")
                # else:
                #     print("删除失败")
                # data.save_students(students)
            delete_student_flow(students)
        elif choice == "4":
            # name = input("please input a name:")
            # # try:
            # #     New_score=float(input("please input a score:"))
            # # except ValueError:
            # #     print("重新输入")
            # #     continue 
            # # if New_score < 0 or New_score > 100:
            # #     print("成绩范围错误")
            # #     continue
            # New_score=input_score()    #重构将上面的几段代码变成一个函数以后有新东西直接改函数就可以牵一发而动全身
            # result=student.update_student_score(students, name, New_score)    #调用 student.py 里面的 update_student_score 函数
            # if result:
            #     print("成绩修改成功！")
            #     data.save_students(students)
            # else:
            #     print("Error")
                # continue
            update_score_flow(students)
        elif choice == "5":
            data.save_students(students)
        elif choice =="6":
            students=data.load_students()  
            # print(students)    #在变成调用对象后，这个打印不起作用
            student.show_students(students)
        elif choice == "7":
            data.save_students(students)
            break

main()
#print(student)    <module 'student' from 'F:\\AI-Developer-Road\\python-study\\student_system\\student.py'> student 本身是一个 module（模块）对象。
# save_students()还没改 with open
# import os 已经不用，可以删除
# 菜单5覆盖students设计可以优化