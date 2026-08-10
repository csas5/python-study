import student   #添加 删除 查看
import data      #save and load
import os

def main():
    if os.path.exists("students.json"):
        students = data.load_students()
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
            try:          
                age = int(input("please input a age:"))
            except:
                print("请重新输入")
                continue                      #输入异常会直接崩溃 and 如果异常必须continue
            if age<0 or age>100:
                print("error")
                continue
            try:
                score = float(input("please input a score:"))
            except:
                print("请重新输入")
                continue
            if score<0 or score>100:       #小优化把=0删去了
                print("error")
                continue
            student.add_student(students,name,age,score)
            data.save_students(students)                       #添加后不保存遇到突发情况数据直接消失
        elif choice == "2":
            student.show_students(students)
        elif choice == "3":
            try:
                name = input("please input a name:")       #这里try except没意义因为本身他输入的就是字符串
            except:
                print("请重新输入")
            result=student.delete_student(students,name)           #这里需要给出参数
            if result:
                print("删除成功")
            else:
                print("删除失败")
            data.save_students(students)
        elif choice == "4":
            data.save_students(students)
        elif choice =="5":
            if os.path.exists("students.json"):    #students.json 是数据文件，判断它是否存在是不是应该由 data.py 负责？这里是可以优化的点，其实应该是越权了
                students=data.load_students()      #判断文件是否存在可以写在函数中  读取的数据没有更新students 如果赋值给data变量那么还是旧数据的打印 这里选取students变量即可正确读取
                print("文件存在")
            else:
                print("文件不存在")       #这里return [] 程序直接退出这里直接用continue即可
                continue
            print(students)
        elif choice == "6":
            data.save_students(students)
            break

main()
#print(student)    <module 'student' from 'F:\\AI-Developer-Road\\python-study\\student_system\\student.py'> student 本身是一个 module（模块）对象。