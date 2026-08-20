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

def input_class_name():
    while True:
        class_name = input("please input a class_name:")
        if class_name =="":
            print("please try again")
            continue
        return class_name

def input_class_id():
    while True:
        try:
            class_id = int(input("please input a class_id:"))
        except ValueError:
            print("please try again")
            continue
        return class_id
        
        



#以下数据库函数
def add_students_flow():   #不需要传name·····这个 Flow 的职责本来就是“自己负责输入，然后调用数据库”
    name = input_name()
    age = input_age() 
    score= input_score()
    class_id = select_class_id()
    database.add_student(name, age, score,class_id)

def show_students_flow():
    students= database.get_students()  #因为要for遍历所以写成students更好
    for student in students:           
        print("name = %s" %  student[1])                 #这里靠索引来打印name，age，score例如：student[0]=id
        print("age = %s" % student[2]) 
        print("score = %s" % student[3])
        print("class_name = %s" % student[4]) 

def delete_students_flow():
    name = input_name()
    student_id=select_student_id_by_name(name)  #这个函数已经有notfoun所以建议flow直接判断
    if student_id is None:   
        return        
    result=database.delete_student(student_id)
    if result :
        print("DELETE SUCCESSFUL")
    else:
        print("DELETE failed")

def update_score_flow():
    name = input_name()
    student_id=select_student_id_by_name(name)
    if student_id is None:   
            return  
    new_score = input_score()   #如果学生根本不存在，就没必要继续问用户输入新成绩
    result=database.update_score(new_score,student_id)
    if result :
        print("UPDATE SUCCESSFUL")
    else:
        print("UPDATE failed")


def select_student_id_by_name(name):
    results=database.find_students_by_name(name)
    if len(results) == 0:
        print("Not found!")
        return 
    elif len(results) == 1:
        student_id=results[0][0]        #这里的results[0]取的是一整条数据，result[0][0]取得才是id
        return student_id
    elif len(results) >=2:
        for result in results:
            print("id = %s,name = %s,age = %s,score = %s" % (result[0],result[1],result[2],result[3])) #这里0123分别对应id-----
        while True:
            try:        #多候选时，id 输入异常处理
                student_id = int(input("please input a id:"))
            except ValueError:
                print("please try again")
                continue
            for result in results:              #for 检查所有候选
                if student_id == result[0]:    #找到合法id
                    return student_id
            print("please try again")   #for 结束以后才能确定“一个都没匹配”

    
def show_students_by_score_desc_flow():
    students = database.get_students_by_score_desc()
    for student in students:
        print("name= %s , age= %s, score = %s" % (student[1],student[2],student[3]))

def show_top_students_flow():
    while True:
        try:
            limit = int(input("please input limit:"))
        except ValueError:
            print("please try again")    #缺少continue
            continue
        if limit >0:
            students=database.get_top_students(limit)
        else:
            print("please input a number greater than 0")  #提示词优化
            continue
        for student in students:
            print("name= %s , age= %s, score = %s" % (student[1],student[2],student[3]))
            #这里放break会导致打印完一行数据直接结束函数所以return更好但是缩进自己判断  
        return

def search_students_by_name_flow():
    keyword = input("please input a keyword:")
    students = database.search_students_by_name(keyword)
    if len(students)>0:    #但这里的 student 还没有定义需要判断>0
        for student in students:
            print("name= %s , age= %s, score = %s" % (student[1],student[2],student[3]))
    else:
        print("NOT FOUND")
        return
#这里不需要return可以删，因为 for 全部执行完以后，函数本身就自然结束了。
# #区分两个变量：students → 所有搜索结果
# student  → for 循环里当前这一条学生数据

def count_students_flow():
    result = database.count_students()
    print("WE HAVE %s students" % result)

def average_score_flow():
    result=database.get_average_score()
    if result is None:
        print("NOT FOUND students DATA")
        return          #注意流程控制点，这里没有return会继续往下执行
    print("average=%s" % result)

def max_score_flow():
    result=database.get_max_score()
    if result is None:
        print("NOT FOUND MAX score")
        return
    print("MAX score = %s" % result)

def min_score_flow():
    result=database.get_min_score()
    if result is None:
        print("NOT FOUND min score")
        return
    print("min score = %s" % result)



#记住result返回的只有两个元素（“calss1",3)   result[0]代表班级
def count_students_by_class_flow():       
    results=database.count_students_by_class()
    for result in results:
        print("class = %s,students = %s\n" % (result[0],result[1]))

def average_score_by_class_flow():
    results=database.get_average_score_by_class()
    for result in results:
        print("class = %s,average = %s\n" % (result[0],result[1]))

def classes_by_average_score_flow():
    min_score =input_score()
    results = database.get_classes_by_average_score(min_score)
    for result in results:
        print("class = %s,average = %s\n" % (result[0],result[1]))
# result[0] → class_name
# result[1] → 聚合结果


def add_class_flow():
    class_name = input_name()
    teacher = input_name()
    database.add_class(class_name, teacher)

    print("ADD successful")

def show_classes_flow():
    results = database.get_classes()
    for result in results:
        print("id= %s,class_name = %s,teacher = %s" % (result[0],result[1],result[2]))



def select_class_id():  #用户选择班级ID
    results = database.get_classes()
    for result in results:
        print("ID= %s,calss_id= %s,teacher = %s" %(result[0],result[1],result[2]))
    while True:
        # class_id = input_age()   #这个输入函数不太恰当
        class_id = input_class_id()  #这里可以整一个input_class_id()函数
        for result in results:
            if class_id == result[0]:
                return class_id
        print("please try again!")  #这里不需要return打印完直接下一轮循环了


