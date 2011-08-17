# coding: utf-8
#
# 把addr文件中的数据导入数据库中
#

import os.path

import sqlite3

DBPATH = "db"
FNAME = "addr"
TABLENAME = "fm"

def f_read():
    """读取文件

    拼接sql语句

    """
    if not os.path.isfile(FNAME):
        raise IOError("make sure the file exist.")

    with open(FNAME) as f:
        for x in f:
            s = x.split("=")
            sql = "insert into {0}(title, desc, url) values('{1}', '{2}', '{3}');\n".format(TABLENAME, s[0], s[0], s[1].replace("\n", ""))
            exec_sql(sql)

    print "done ..."


def exec_sql(p):
    """执行SQL语句

    """
    if not os.path.isfile(DBPATH):
        raise IOError("make sure the db exist.")    
    with sqlite3.connect(DBPATH) as con:
        con.execute(p)


if __name__ == "__main__":
    sql = f_read()
