# def add_student(students,name,age,score):     #因为一次只更新一个学生所以这里用add_student()意思更好
#     student={                                   #add_students() 不再负责“制作学生字典”，而是负责创建 Student 对象并把对象加入列表
#         "name":name,
#         "age":age,
#         "score":score
#     }
#     students.append(student)
import database
import student
import logging
#职责为输入 + 业务流程
def add_student(students,name,age,score):
    student=Student(name,age,score)   #创建一个对象并赋值给某个变量
    students.append(student)  #添加学生对象到学生列表
   

# def show_students(students):                     #这里是读取词典但是现在列表里的对象要迭代函数了
#     for student in students:
#         print("姓名: %s" % student["name"])
#         print("年龄: %s" % student["age"])
#         print("成绩: %s" % student["score"])

def show_students(students): 
    for student in students:
        student.show_info()         #这里查看的的是一个对象




# def delete_student(students,name):
#     for student in students:           #遍历     这里的逻辑是先遍历整个词典找到姓名匹配的词典然后删除 
#         if student["name"] == name:    #name找到目标词典
#             students.remove(student)   #消除词典          #不需要break
#             return True                #加入bool来判断真假
#     return False                         #直接中断  
def delete_student(students,name):
    for student in students:     #从列表中一个一个取出 Student 对象。
        if student.name == name: #通过对象属性获取姓名。
            students.remove(student)  #从学生列表中删除这个对象。
            return True 
    return False

def update_student_score(students, name, new_score):     #z注意需要三个参数
    for student in students:
        if student.name == name:
            student.update_score(new_score)    #更符合 OOP 思想的写法
            return True
    return False


#Student 管理一个学生，管理函数管理一群学生。
class Student:   #我要创建一个叫 Student 的类。   studnets是列表 student是一个对象   这里类名后面的括号，是用来写继承的父类，不是用来接收创建对象时的参数。
    def __init__(self,name,age,score):    #name是创建学生时传进来的一个临时数据。  self.name是把这个数据保存到“当前 Student 对象”里面
         self.name=name                  #这里不要反了name 是传进来的临时数据。self.name 是保存到当前对象的数据。
         self.age=age
         self.score=score
    def show_info(self):             #show_info() 也必须有 self  所以 Python 必须知道这个方法属于哪个对象。
        print("名字为：%s " % self.name)
        print("年龄为：%s " % self.age)
        print("成绩为: %s" % self.score)    #这就是一个真正的类 + 对象 + 属性 + 方法了
    def update_score(self, new_score):
        self.score=new_score            #注意外面的是临时参数，保存的数据都是有self前缀的。赋值是应该用self.score=new_score


#什么时候创建 manager.py？  student.py里面出现：大量业务逻辑。 把管理业务搬出去写成manager.py
#什么时候创建 utils.py？ 当你发现：很多地方重复：比如：input_name()......就写utils.py
#Student 是类，student 是对象，self 到底指向谁。

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

# def add_student_flow(students):
#     name = input_name()
#     age = input_age() 
#     score= input_score()
#     student.add_student(students,name,age,score)
#     logging.info("学生信息添加成功：%s " % name)
#     database.save_students(students)

# def delete_student_flow(students):
#     name = input("please input a name:")       
#     result=student.delete_student(students,name)         
#     if result:
#         print("删除成功")
#     else:
#         print("删除失败")
#     database.save_students(students)

# def update_score_flow(students):     #update_score_flow() 的职责是：完成“一次修改成绩操作” 所以执行完直接回到main菜单
#         name = input("please input a name:")
#         New_score=input_score()
#         result=student.update_student_score(students, name, New_score)
#         if result:
#                 print("成绩修改成功！")
#                 database.save_students(students)
#         else:
#             print("未找到该学生")




#以下数据库函数
def add_students_flow():   #不需要传name·····这个 Flow 的职责本来就是“自己负责输入，然后调用数据库”
    name = input_name()
    age = input_age() 
    score= input_score()
    database.add_student(name, age, score)

def show_students_flow():
    students= database.get_students()  #因为要for遍历所以写成students更好
    for student in students:           
        print("name = %s" %  student[1])                 #这里靠索引来打印name，age，score例如：student[0]=id
        print("age = %s" % student[2]) 
        print("score = %s" % student[3]) 

def delete_students_flow():
    name = input_name()          
    database.delete_student(name)

def update_score_flow():
    name = input_name() 
    new_score = input_score()
    database.update_score(name,new_score)





    


