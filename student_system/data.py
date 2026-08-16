import json
from student import Student
import os

# def save_students(students):
#     data=json.dumps(students)            #()括号内放数据，外头用变量赋值
#     file=open("students.json","w")       #注意w小写 and 什么数据就用什么名   以后学习异常处理后，可以改：with open("students.json","w") as file: 效果涵盖了自动关闭
#     file.write(data)                    #这里可以优化成with open
#     file.close()

# def load_students():

#     try:                                #异常处理的运用优化  try：下面代码可能出现错误，如果出现错误，不让程序直接崩溃。
#         file=open("students.json","r")  #打开文件读取模式
#         content=file.read()             #将file文件里的students.json内容赋值给content
#         file.close()                    #关闭文件

#         data=json.loads(content)         #用json解压content的内容赋值给data
            
#         return data                      #返回data

#     except:
#         return []             #这是裸异常捕获  可以吃掉所有错误甚至你的代码拼写错误也可以

# def load_students():

#     try:                                             #try：下面代码可能出现错误，如果出现错误，不让程序直接崩溃。

#         with open("students.json","r") as file:      #as file  给打开的文件起一个变量名字：
#             content=file.read() 

#         data=json.loads(content)

#         return data


    # except FileNotFoundError:                      #处理文件错误

    #     return []


    # except json.JSONDecodeError:                   #处理JSON格式错误。

    #     return []

def student_to_dict(student):     #Student对象 → 字典
    student_dict={
        "name": student.name,
        "age": student.age,
        "score": student.score
        }
    return student_dict

def save_students(students):
    student_dicts=[]                              #创建一个列表
    for student in students:                        #遍历对象
        student_dict=student_to_dict(student)      #使用转化词典函数去赋值给某个变量
        student_dicts.append(student_dict)          #添加函数
    data=json.dumps(student_dicts)                  #json.save的固定流程
    with open("students.json","w") as file:
        file.write(data)

def dict_to_student(student_dict):
    name = student_dict["name"]
    age = student_dict["age"]
    score = student_dict["score"]

    student = Student(name, age, score)   #这里未定义Student是因为要导入类  创建一个对象赋值个某个对象

    return student

# data → 字典列表
# student_dict → 一个字典
# student → 一个 Student 对象
# students → Student对象列表

def load_students():
    if not os.path.exists("students.json"):
        return []
    with open("students.json","r") as file:   
            content=file.read()
            data=json.loads(content)
    students=[] 
    for student_dict in data:
        number=dict_to_student(student_dict)
        students.append(number)
    return students

