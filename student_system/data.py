import json


def save_students(students):
    data=json.dumps(students)            #()括号内放数据，外头用变量赋值
    file=open("students.json","w")       #注意w小写 and 什么数据就用什么名   以后学习异常处理后，可以改：with open("students.json","w") as file: 效果涵盖了自动关闭
    file.write(data)  
    file.close()

def load_students():

    try:                                #异常处理的运用优化
        file=open("students.json","r")  #打开文件读取模式
        content=file.read()             #将file文件里的students.json内容赋值给content
        file.close()                    #关闭文件

        data=json.loads(content)         #用json解压content的内容赋值给data
            
        return data                      #返回data

    except:
        return []