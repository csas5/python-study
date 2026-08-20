import student
import sqlite3

# data → 字典列表
# student_dict → 一个字典
# student → 一个 Student 对象
# students → Student对象列表


#数据库
def find_students_by_name(name):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM students WHERE name = ?",(name,))
    results = cursor.fetchall()  #这时候 id 已经在结果里面了  注意，id需要用到索引比如studnet[0][0]对应的就是id
    conn.close()
    return results





def init_db():  #建立学生表
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

def init_classes_table():  #建立班级表
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()     #这里的text是字符串，integer整数，real小数，id用主键
    cursor.execute("""CREATE TABLE IF NOT EXISTS classes(
    id INTEGER PRIMARY KEY,                                     
    class_name TEXT,
    teacher TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_student(name, age, score,class_id):  #这一版可以将classname改成classID了
    conn = sqlite3.connect("students.db")   #如果 students.db 不存在，SQLite 会自动创建。 这里的connect相当于打开连接
    cursor = conn.cursor()   #创建执行 SQL 的 cursor
    cursor.execute("INSERT INTO students(name,age,score,class_id) VALUES(?,?,?,?)",(name,age,score,class_id))
    conn.commit()
    conn.close()

def get_students():  #把数据库里的所有学生查出来并返回。
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM students")
    students = cursor.fetchall()  #取出全部结果
    conn.close()
    return students #这个函数的职责要求把查询结果交出去，所以这里需要 return students。

def delete_student(student_id):          #name改成id
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?",(student_id,))  #"SQL语句",(name,)别忘了逗号  不需要多扩一层括号
    result = cursor.rowcount  # # 这次 DELETE 影响了几条数据
    conn.commit()
    conn.close()
    if result == 1:
        return True
    else:
        return False 
    
def update_score(new_score,student_id):
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET score = ? WHERE id = ?",(new_score,student_id))    #不是form 而是直接update students  而且set后面要有列的值
    result = cursor.rowcount
    conn.commit()                                                   #只有单元素 tuple时，逗号才是必须的 么有逗号只能算字符串
    conn.close()
    if result == 1:
        return True
    else:
        return False

def get_students_by_score_desc():
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY score DESC")
    students = cursor.fetchall()
    conn.close()
    return students

def get_top_students(limit):   #这一版固定查成绩前三名。加入参数可以自定义前n名
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY score DESC LIMIT ?",(limit,))
    students = cursor.fetchall()
    conn.close()
    return students


def search_students_by_name(keyword):
    result ="%"+keyword+"%"  #字符串拼接
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?",(result,))
    students = cursor.fetchall()
    conn.close()
    return students
    
def count_students():
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    result = cursor.fetchone()   #这里需要返回真正的数量需要索引
    conn.close()
    return result[0]     

def get_average_score():
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(score) FROM students")
    result = cursor.fetchone()
    conn.close()
    return result[0]     #真实边界情况如果 students 表里一条学生都没有，AVG(score) 的结果会是 None
#也就是result[0]里面可能存着None


def get_max_score():
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(score) FROM students")
    result = cursor.fetchone()
    conn.close()
    return result[0]    #注意边界

def get_min_score():
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(score) FROM students")
    result = cursor.fetchone()
    conn.close()
    return result[0] 


def test_class_name_exists():  #添加class_name到学生表
    has_class_name = False
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(students)")
    columns = cursor.fetchall()
    for column in columns:
        if column[1] == "class_name":
            has_class_name = True
    if not has_class_name:
        cursor.execute("ALTER TABLE students ADD COLUMN class_name TEXT")  #等遍历完了在判断存不存在
        conn.commit()
        has_class_name = True     #因为既然刚刚成功添加了这一列，那么当前真实状态已经是 True否则打印依旧false
    conn.close()


def add_class_id_column():    #calss_id是integer整数 这个函数监测classid在不在学生表，不在添加
    has_class_id = False
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor() 
    cursor.execute("PRAGMA table_info(students)")
    columns = cursor.fetchall()
    for column in columns:
        if column[1] == "class_id":
             has_class_id = True
    if not has_class_id:
        cursor.execute("ALTER TABLE students ADD COLUMN class_id INTEGER")
        conn.commit()   #只是如果 class_id 本来就存在，这一次并没有修改数据库，commit() 就相当于空提交。
    conn.close()

    

def count_students_by_class():  #每班人数
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT class_name, COUNT(*) FROM students GROUP BY class_name")
    results = cursor.fetchall()
    conn.close()
    return results

def get_average_score_by_class():   #每班平均分
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT class_name, AVG(score) FROM students GROUP BY class_name")
    results = cursor.fetchall()
    conn.close()
    return results

def get_classes_by_average_score(min_score):    #筛选平均分达到要求的班级
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("SELECT class_name, AVG(score) FROM students GROUP BY class_name HAVING AVG(score) >= ?",(min_score,))
    results = cursor.fetchall()
    conn.close()
    return results


def add_class(class_name, teacher):  #输入class班级和老师
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSRT INTO classes(class_name, teacher) VALUES(?,?)",(class_name,teacher))
    conn.commit()
    conn.close()

def get_classes():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM classes")
    results = cursor.fetchall()
    conn.close()
    return results    #每一行大概是(1, "class1", "张老师")  result[0] → id -----





def migrate_class_name_to_class_id(): #迁移班级名字到班级id
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, class_name FROM students WHERE class_id IS NULL AND class_name IS NOT NULL")
    students = cursor.fetchall()
    for student in students:
        student_id=student[0]    #这里取得是student_id
        class_name = student[1]
        cursor.execute("SELECT id FROM classes WHERE class_name = ?",(class_name))
        class_result = cursor.fetchone() #这里查询了class表的id所以返回了classid
        if class_result is not None:
            class_id = class_result[0]   #所以这里索引的对象就是id
            cursor.execute("UPDATE students SET class_id = ? WHERE id = ?",(class_id, student_id))
                #WHERE id 需要学生id
    conn.commit()
    conn.close()


migrate_class_name_to_class_id()
