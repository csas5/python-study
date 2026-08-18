import logging
logging.basicConfig(   #basicConfig() 可以理解成：给 Python 的 logging 系统做“基础配置”的函数。
    level=logging.INFO,
    filename="app.log",  #它告诉 logging：不要只把日志显示在终端，而是把日志写进 app.log 文件。
    encoding="utf-8",   #指定编码  这里我的代码有个bug 如果不指定编码log里面会乱码
    format="%(asctime)s - %(levelname)s - %(message)s"  #时间-等级-内容
)
logging.info("学生信息添加成功")        #括号填入信息解释其原因
logging.warning("students.json不存在")    
logging.error("学生数据保存失败")

#现在数据流变成：
# logging.info()
#        ↓
#    logging系统
#        ↓
#     app.log