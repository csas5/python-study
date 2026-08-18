import sqlite3
conn = sqlite3.connect("students.db")   #如果 students.db 不存在，SQLite 会自动创建。 这里的connect相当于打开连接
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students")
#在 Python 中执行 SQL，要使用：cursor.execute("SELECT * FROM students")   且这里可以缩略成CREATE TABLE IF NOT EXISTS students避免重复创建时报错。
# cursor.execute("""            
# CREATE TABLE students (
#     id INTEGER PRIMARY KEY,   
#     name TEXT,
#     age INTEGER,
#     score REAL
# )
# """)  #引号的内容这一段是 SQL，Python 不认识它，必须把它作为字符串交给：
# conn.close()  #程序操作完数据库后，关闭数据库连接。
# 
# 本质上和下面是一样的：
# # cursor.execute(
#     "CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, score REAL)"
# )
#  
cursor.execute(
    "INSERT INTO students(name, age, score) VALUES (?, ?, ?)",
    ("xiaoming", 21, 87.5)
)
#cursor.fetchone()只取一条结果
conn.commit()   #只有增加删除更新这类会改变数据库的内容的指令会需要这个
conn.close()

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
print(students)

cursor.execute(
    "SELECT * FROM students WHERE name = ?",
    ("tom",)
)
students = cursor.fetchall()   #取所有
print(students)

cursor.execute(         #更新
    "UPDATE students SET score = 90 WHERE name = ?",
    ("tom",)
)

conn.commit()
conn.close()

cursor.execute(           #删除
    "DELETE FROM students WHERE name = ?",
    ("jack",)
)

conn.commit() 
conn.close()  


# cursor.execute("INSERT INTO students (name,age,score) VALUES(?,?,?)", ('lucy',19,88.5)")  #别忘了逗号
# conn.commit() 
# cursor.execute("SELECT * FROM students")
# students = cursor.fetchall()
# print(students)
