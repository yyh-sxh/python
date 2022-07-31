import pymysql
#创建连接对象
#host：服务器的主机地址
#port：端口号
#user：用户名
#password：密码
#database：操作的数据库
#charset：编码
content = pymysql.connect(host='localhost',port=3306,user='root',password='',database='python',charset='utf8')

#获取游标，目的就是执行sql语句
cursor = content.cursor()

def list():

    #sql语句
    sql = "select * from students"
    #防sql注入
    # sql = "select * from students where name = %s"
    try:

        #执行sql
        cursor.execute(sql)
        # 执行防注入
        # cursor.execute(sql,('张飞',))
        #获取查询结果
        #单条数据
        # row = cursor.fetchone()
        # print(row)

        #多条数据
        result = cursor.fetchall()
        # print(result)

        for item in result:
            print(item)
    except Exception as e:
        pass


def save():
    # sql = "INSERT INTO students(name,age,sex,country) VALUES ('张辽',30,'男','魏国')"
    #防注入
    sql = "INSERT INTO students(name,age,sex,country) VALUES (%s, %s, %s, %s)"
    try:
        # 执行sql
        # cursor.execute(sql)
        #防注入
        #数组形式传参
        lst = ['张颌',27,'男','魏国']
        cursor.execute(sql,lst)
        content.commit()

    except Exception as e:
        content.rollback()
        print('新增报错')

def update():
    sql = 'UPDATE students set name = "于禁" WHERE id = 17'

    try:
        cursor.execute(sql)
        content.commit() #提交到数据库
    except Exception as e:
        content.rollback() #回滚

def delete():
    sql = 'DELETE FROM students WHERE id = 17'
    try:
        cursor.execute(sql)
        content.commit()
    except Exception as e:
        content.rollback()

if __name__ == '__main__':

    # save()
    # update()
    # delete()
    list()
    # 关闭游标
    cursor.close()
    # 关闭连接
    content.close()