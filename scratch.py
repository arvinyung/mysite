#   -*- coding:utf-8 -*-

'''
    @   功能：     根据身高，体重计算BMI指数
    @   author：  无语
    @   create：  2020-03-03
'''

print ('''根据身高，体重计算BMI指数''')

#=================程序开始==================#
#输入身高和体重
hight=float(input("请输入您的身高(米m)："))
weight=float(input("请输入您的体重（千克kg）："))


bmi=weight/(hight*hight)

print("您的BMI指数喂："+str(bmi))

#判断身材是否合理
if  bmi<18.5:
    print("您的体重过轻 ～@～")
if  bmi>=18.5 and bmi<24.9:
    print("正常范围，请保持 （-_-）")
if  bmi>24.9 and bmi<29.9:
    print("您的体重过重 ～@～ ")
if  bmi>29.9:
    print("肥胖 ～@～")

#=================程序结束==================#

