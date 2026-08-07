# student={              #不要忘了给字典建立一个名字，之后好索引例如：student["name"]
#     "name" : "jack",   #字典中不是 “name=jack"而是 name：jack
#     "age" : 23,     #键通常需要加引号 而且不要忘了逗号   Python开发中常见格式：冒号后面留一个空格即可。
#     "score" : 60
# }
# print(student["name"],student["score"])

# student={
#     "name":"jack",
#     "age":23,
#     "score":60
# }
# student["score"]=90
# student["city"]="shanghai"
# print(student["city"])

# students = []                                    #示例   students=[]空列表  里面什么都没有。

# i = 0

# while i < 3:                                    #创建一个学生字典
#     name = input("请输入姓名：")
#     age = int(input("请输入年龄："))
#     score = int(input("请输入成绩："))

#     student = {
#         "name": name,
#         "age": age,
#         "score": score
#     }

#     students.append(student)                  #加入列表

#     i += 1                                    #循环加入

# print(students)

# i=0
# total=0
# studentslists=[]
# max_score=0
# max_score_name=0   #初始值应该更像：max_score_name=""
# while(i<3):                                                 #创建空列表循环创建字典append进去
#     studentslist=input("please input name:")
#     studentslists.append(studentslist)
#     i+=1
# studentslists[0]={
#     "name": "jack",
#      "age": 23,
#      "score": 90
# }
# studentslists[1]={
#     "name": "tom",
#     "age": 21,
#     "score": 85
# }
# studentslists[2]={
#     "name": "lucy",
#     "age": 22,
#     "score":95
# }
# for student in studentslists:
#     total+=student["score"]
#     if max_score<student["score"]:
#         max_score=student["score"]
#         max_score_name=student["name"]        #我在这一直思考怎么在for里面找到最高分的名字，随后想到能寻到最高分那么此刻for一定是在最高分的字典里面所以直接让最高分名字=字典名字即可
# print(max_score_name,max_score)
# average=total/len(studentslists)
# print(average)

# students=[]
# i = 0
# while(i<3):
#     name = input("please input name:")
#     age = int(input("please input age:"))
#     score =float(input("please input score:"))
#     student={
#         "name": name,
#         "age": age,
#         "score": score
#     } 
#     students.append(student)
#     i+=1
# for student in students:
#     print("学生：%s 年龄：%s 成绩: %s" % (student["name"], student["age"], student["score"])) #记住多个%s后面的变量要用括号的形式

# def welcome():
#     print("welcome python")  #定义一个函数
# welcome()  #调用函数 使用刚刚创建的功能。
# x=input("please input name:")
# def welcome(x):
#     print("welcome %s" % x)
# welcome(x)

# def add(a,b):     #有几个参数就写几个参数
#     add = a + b   #处理程序  建议变量名为result
#     return add    #返回结果
# print(add(10,20)) 

# scores=[90,80,70]
# def average(scores):
#     total = 0
#     for score in scores:
#         total += score
#     result = total / len(scores)
#     return result
# print(average(scores))

students=[
    {
        "name":"jack",
        "age":23,
        "score":90
    },
    {
        "name":"tom",
        "age":21,
        "score":85
    }
]
def get_average_score(students):
    total = 0
    for student in students:
        total += student["score"]
    get_average_score = total / len(students)   #错误在计算人数这里
    return get_average_score
print(get_average_score(students))

    
