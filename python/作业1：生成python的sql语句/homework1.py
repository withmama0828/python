import pymysql


class SQL:

    def __init__(conn, username, password, dbname):
        conn.provincial = {'长春', '沈阳', '哈尔滨'}
        conn.city = {'吉林', '辽宁', '黑龙江'}
        conn.flag = 0
        conn.username = username
        conn.password = password
        conn.dbname = dbname

    def sqlConn(conn, host="127.0.0.0", port=3306):
      password = 123
      username = 'root'
      dbname = ['database', 'provincial', 'city']
      #cursor = conn.cursor()
      # SQL 查询语句
      sql = "SELECT * FROM user_db"
      try:
          # 执行SQL语句
          conn.execute(sql)
          # 获取所有记录列表
          results = conn.fetchall()
          print(results)
      except:
          print(" ")

      # 关闭数据库连接
      #conn.close()

      # 判断用户名，密码是否正确
      if conn.password == password and conn.username == username:
          for i in range(0, len(dbname)):
              if conn.dbname == dbname[i]:
                  conn.flag = 1

    #args 是 arguments 的缩写，表示位置参数；
    # kwargs 是 keyword arguments 的缩写，表示关键字参数。
    # 是 Python 中可变参数的两种形式，并且 *args 必须放在 **kwargs 的前面，因为位置参数在关键字参数的前面。
    #*args就是就是传递一个可变参数列表给函数实参，这个参数列表的数目未知，甚至长度可以为0
    #**kwargs则是将一个可变的关键字参数的字典传给函数实参，同样参数列表长度可以为0或为其他值
    def select(conn, *args, **kwargs):
        # 判断是否链接数据库
        if not conn.flag:
            print('数据库未连接!')
            exit(-1)

        if args:
            print(args)
            print('')
        if kwargs:
            #print(kwargs)
            methods = kwargs['query'].split(',')
            #print(methods)
            print("生成的sql语句是：")
            print('Select {} from {} where {}={}'.format(kwargs['method'], kwargs['query'], kwargs['method'], [kwargs[m] for m in kwargs['method'].split(',')]))
            #print(conn.City, conn.Provincial)


if __name__ == '__main__':

    sql = SQL('root', 123, 'database')
    sql.sqlConn(port=3306)
    #此处生成sql条件
    sql.select(query='provincial', method='provincial', provincial='长春')
    sql.select(query='provincial，city', method='city', city='辽宁')
