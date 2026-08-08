# Day2：个人信息卡

# c
#思考题为什么如果用户输入的是：22   因为是整数
#为什么 Python 并不知道它是数字？
#想一想：
#input() 得到的数据到底是什么类型？永远返回字符串
#思考题
#a = input("请输入第一个数字：")
#b = input("请输入第二个数字：")
#print(a + b) result=1020  因为“+”是字符串拼接 "Hello" + "Python"="HelloPython" 如果是数字相加应该是 10 + 20 = 30

# 用户输入商品名称。
# 用户输入商品价格。
# 用户输入商品库存数量。
# 最后输出一张商品信息卡。
goods_name = input("请输入商品名称：")
goods_price = input("请输入商品价格：")
goods_stock = input("请输入商品库存数量：")
print("商品信息卡如下：")
print("商品名称：%s" % goods_name)
print("商品价格：%s" % goods_price)     
print("商品库存：%s" % goods_stock)     