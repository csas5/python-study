# def add_student(students,name,age,score):     #因为一次只更新一个学生所以这里用add_student()意思更好
#     student={                                   #add_students() 不再负责“制作学生字典”，而是负责创建 Student 对象并把对象加入列表
#         "name":name,
#         "age":age,
#         "score":score
#     }
#     students.append(student)
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
class Student:   #我要创建一个叫 Student 的类。   studnets是列表 student是一个对象
    def __init__(self,name,age,score):    #name是创建学生时传进来的一个临时数据。  self.name是把这个数据保存到“当前 Student 对象”里面
         self.name=name                  #这里不要反了name 是传进来的临时数据。self.name 是保存到当前对象的数据。
         self.age=age
         self.score=score
    def show_info(self):
        print("名字为：%s " % self.name)
        print("年龄为：%s " % self.age)
        print("成绩为: %s" % self.score)    #这就是一个真正的类 + 对象 + 属性 + 方法了
    def update_score(self, new_score):
        self.score=new_score            #注意外面的是临时参数，保存的数据都是有self前缀的。赋值是应该用self.score=new_score
