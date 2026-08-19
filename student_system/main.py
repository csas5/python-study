import student   #添加 删除 查看
import database      #save and load
import os
import logging   #引入日志
#main.py 负责用户交互和程序流程控制。
#student.add_student()负责创建 Student 对象并放入 students 列表。  所以我们再增加一个函数：add_student_flow()可以负责：完成一次“添加学生”的完整用户操作流程。
#迁移了函数记住加前缀不然会显示未定义

            


    




def main():
    database.init_db()
    while True:                                                                     
        print("==================\n")
        print("    学生管理系统   ")
        print("==================\n")
        choice=input("please choice a number:")
        if choice == "1":       
            student.add_students_flow()                       #新封装的函数添加工作流
        elif choice == "2":
            student.show_students_flow()
        elif choice == "3":
            student.delete_students_flow()
        elif choice == "4":
            student.update_score_flow()
        elif choice == "5":
            # database.save_students(students)   #因为是数据库版本保存自动进行所以5的保存功能可以优化
            break
main()
#print(student)    <module 'student' from 'F:\\AI-Developer-Road\\python-study\\student_system\\student.py'> student 本身是一个 module（模块）对象。
# save_students()还没改 with open
# import os 已经不用，可以删除
# 菜单5覆盖students设计可以优化