import json
import student
import os
import logging
import sqlite3
#原先为data.py现在改成数据库  职责为真正操作数据库
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
    try:
        with open("students.json","w") as file:
            file.write(data)
            logging.info("保存学生数据成功") 
    except OSError:
        logging.error("学生数据保存失败")     #优化点：logging.exception()这样以后不仅知道“保存失败”，还能看到具体异常和 traceback。

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

#数据库
def init_db():
    conn = sqlite3.connect("students.db")   #如果 students.db 不存在，SQLite 会自动创建。 这里的connect相当于打开连接
    cursor = conn.cursor()
    cursor.execute("""              
    CREATE TABLE IF NOT EXISTS students(                      
    id INTEGER PRIMARY KEY,   
    name TEXT,
    age INTEGER,
    score REAL
 )
 """)   #执行 CREATE TABLE IF NOT EXISTS接着表结构
    conn.commit()
    conn.close()

def add_student(name, age, score):
    conn = sqlite3.connect("students.db")   #如果 students.db 不存在，SQLite 会自动创建。 这里的connect相当于打开连接
    cursor = conn.cursor()   #创建执行 SQL 的 cursor
    cursor.execute("INSERT INTO students(name,age,score) VALUES(?,?,?)",(name,age,score))
    conn.commit()
    conn.close()

def get_students():  #把数据库里的所有学生查出来并返回。
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM students")
    students = cursor.fetchall()  #取出全部结果
    conn.close()
    return students #这个函数的职责要求把查询结果交出去，所以这里需要 return students。

def delete_student(name):
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name = ?",(name,))  #"SQL语句",(name,)别忘了逗号  不需要多扩一层括号
    conn.commit()
    conn.close()
    
def update_score(name, new_score):
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("UPDATE students set score = ? WHERE name = ?",(new_score,name,))    #不是form 而是直接update students  而且set后面要有列的值
    conn.commit()                                                   #只有单元素 tuple时，逗号才是必须的 么有逗号只能算字符串
    conn.close()
