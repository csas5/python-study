# file=open("test.txt","w")     #打开 test.txt不存在就创建使用写入模式
# file.write("hello python")    #写入内容
# file.close()                  #保存并释放资源。
# file=open("test.txt","r")     #打开文件进入写入模式
# content= file.read()          #创建变量并将file.read()中的值赋值给变量
# file.close()                  #保存并释放资源。
# print(content)                #打印变量的内容

students=[
    {
        "name":"jack",
        "age":23,
        "score":90
    }
]

import json    #使用json需要先声明！！！    这是一个json保存函数
def save_students(students):
    data=json.dumps(students)            #()括号内放数据，外头用变量赋值
    file=open("students.json","w")       #注意w小写 and 什么数据就用什么名
    file.write(data)  
    file.close()

def load_students():
    file=open("students.json","r")    #读取保存好的学生数据。
    content=file.read()               #读取文件内容
    file.close()                      #关闭文件
    data=json.loads(content)          #JSON字符串转换
    return data                       #返回数据

save_students(students)               #使用save函数
del students                          #删除studnet这个列表
students=load_students()              #读取studnet.json的数据
print(students)                       #打印students里的内容