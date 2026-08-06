# i=1
# while(i<=5):
#     print(i)
#     i+=1

# i=1
# sum=0
# while(i<=100):
#     sum+=i  #sum=sum+i
#     i+=1    #i=i+1
# print("1到100的和为：",sum)

# i=7
# while(int(input("请输入一个数字："))!=i):
#     print("输入错误，请重新输入！")
# else:
#     print("输入正确，程序结束！")

# i=7
# guess=0   #重点是定义一个变量来存储用户输入的数字  且需要elif判断三个状态
# while(guess!=i):
#     guess=int(input("请输入一个数字："))
#     if guess>i:
#         print("猜big了，请重新输入！")
#     elif guess<i:
#         print("猜small了，请重新输入！")
#     elif guess==i:
#         print("恭喜你，猜对了！")

# user_name="admin"
# user_password="123456"
# count=0
# while(count<3):
#     input_username=input("请输入用户名：")   #这里可能出错的点在于不能同时将用户名和密码用and连接在一起判断，因为用户可能只输入了用户名错了就直接else。
#     input_password=input("请输入密码：")
#     if user_name==input_username and user_password==input_password:
#         print("登录成功！")
#         break
#     else:
#         print("用户名或密码错误，请重新输入！")
#         count+=1
#     if count==3:
#         print("输入错误次数过多，账号已锁定！")

# i=0
# names=[0,0,0]  #实际上是定义了一个长度为3的列表，里面的元素都是0，但代码中如果要定义100个以上的元素就不太适合了，因为列表的长度是固定的，除非使用append()方法来动态添加元素。并且不建议用list而是改用names更好
# while(i<3):
#     names[i]=input("请输入姓名：")   
#     i+=1
# print(names[0],names[2])

# i = 0
# students=[]  #这里的append()方法是用来向列表中添加元素的，注意append()方法是没有返回值的，所以不能直接将其赋值给一个变量，否则会报错。
# while(i<3):
#     student=input("请输入学生姓名：")
#     students.append(student)   #append()方法是用来向列表中添加元素的，注意append()方法是没有返回值的，所以不能直接将其赋值给一个变量，否则会报错。
#     i+=1
# print(students[0],students[2])

# i = 0
# students=[]  
# while(i<3):
#     student=input("请输入学生姓名：")
#     students.append(student)   
#     i+=1
# for student in students:  #这里的for循环是用来遍历列表中的元素的，注意for循环的语法是for 变量 in 列表名:，其中变量是用来存储列表中的每一个元素的。
#     print(student)

# scores=[88,76,95,59,66]
# for score in scores:
#     if score>=60:
#         print(score,"及格")
#     else:
#         print(score,"不及格")

# scores=[88,76,95,59,66]
# total=0
# average=0  #一个小优化点 average=0其实可以删除。
# for score in scores:
#     total+=score
# print("总分为：",total)
# average=float(total/len(scores))  #len直接遍历数组的数量，这样就不用数数了
# print("平均数为 %s" % average)


# scores=[88,76,95,59,66,40,100]
# total=0
# pass_count=0
# fall_count=0
# for score in scores:
#     total+=score   #只负责统计数据
#     if score>=60:
#         pass_count+=1
#     else:
#         fall_count+=1
# print("总分为：",total)
# average=float(total/len(scores))  #float是多余的，在有average出现时
# print("平均数为 %s" % average)
# print("pass:%s and fall:%s" % (pass_count,fall_count))

#Day6最后挑战
# 找出最高分
# 找出最低分
# 输出最高分是多少
# 输出最低分是多少
scores=[88,76,95,59,66,40,100]
max=0
small=scores[0]
for score in scores:
    if max<score:
        max=score
    if small>score:
        small=score
print(max,small) 



