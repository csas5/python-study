import sqlite3
conn = sqlite3.connect("students.db")   #如果 students.db 不存在，SQLite 会自动创建。 这里的connect相当于打开连接
cursor = conn.cursor()
#在 Python 中执行 SQL，要使用：cursor.execute("SELECT * FROM students")
cursor.execute("""         
CREATE TABLE students (
    id INTEGER PRIMARY KEY,   
    name TEXT,
    age INTEGER,
    score REAL
)
""")  #引号的内容这一段是 SQL，Python 不认识它，必须把它作为字符串交给：
conn.close()  #程序操作完数据库后，关闭数据库连接。