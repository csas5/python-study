# 程序需要：
# 获取用户输入的出生年份
# 将输入的数据转换成可以计算的数字类型
# 计算年龄
# 输出结果

# bron=input("请输入您的出生年份：")
# age=2026-int(bron)
# print("您的年龄是：",age)

# 制作一个购物计算程序。
# 用户输入：
# 商品价格
# 购买数量
# 程序输出：
# 商品总价

# price=float(input("请输入商品价格："))
# quantity=int(input("请输入购买数量："))
# total=price*quantity
# print("商品总价是：",total)
# 制作一个计算器。
# 程序需要：
# 用户输入：
# 第一个数字
# 第二个数字
# 然后计算：
# 两数相加
# 两数相减
# 两数相乘
# 两数相除

# num1=float(input("请输入第一个数字："))
# num2=float(input("请输入第二个数字："))
# print("两数相加的结果是：",num1+num2)
# print("两数相减的结果是：",num1-num2)
# print("两数相乘的结果是：",num1*num2)
# print("两数相除的结果是：",num1/num2)

# 要求：
# 写一个程序：
# 输入用户年龄。
# 判断：
# age=int(input("请输入您的年龄："))
# if age>=18:
#     print("您已成年，可以进入。")
# else:
#     print("您未成年，禁止进入。")

# student_score=float(input("请输入学生成绩："))
# if student_score>=90:
#     print("成绩优秀")
# elif student_score>=80:
#     print("成绩良好")
# elif student_score>=60:
#     print("成绩及格")
# else : 
#     print("成绩不及格")

# user_name="admin"
# user_password="123456"
# input_name=input("请输入用户名：")
# input_password=input("请输入密码：")
# if input_name==user_name and input_password==user_password:
#     print("登录成功")
# else:
#     print("用户名或密码错误")

# cost=float(input("请输入："))
# if cost>=1000:
#     print("黄金会员")
# elif cost>=500:
#     print("白银会员")
# elif cost>=100:
#     print("普通会员")
# else:
#     print("非会员")

balance=5000
cost=float(input("请输入消费金额："))
if cost<=balance:
    balance=balance-cost
    print("消费成功，当前余额为：",balance)
elif cost>balance:
    print("余额不足，无法消费。")
else:
    cost<=0
    print("消费金额必须大于0。")