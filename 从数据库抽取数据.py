#!/usr/bin/python3  
   
import pymysql  
  
# 打开数据库连接  
db = pymysql.connect("localhost","root","strongs","testdb" )  
  
# 使用cursor()方法获取操作游标   
cursor = db.cursor()  
  
# SQL 查询语句  
sql = "select * from employee \  
       where age > '%d'" % (18)  
try:  
   # 执行SQL语句  
   cursor.execute(sql)  
   # 获取所有记录列表  
   results = cursor.fetchall()  
   for row in results:  
      first_name = row[0]  
      last_name = row[1]  
      age = row[2]  
      sex = row[3]  
      income = row[4]  
       # 打印结果  
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \  
             (first_name, last_name, age, sex, income ))  
except:  
   print ("Error: unable to fetch data")  
  
# 关闭数据库连接  
db.close()  

#pip install PyMySQL  