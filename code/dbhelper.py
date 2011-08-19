# coding: utf-8
# 
# sqlite 操作类
#

from sqlite3 import connect

__version__ = "0.1"

DBPATH = "db"


class DBHelper(object):
    """sqlite 帮助类

    用法:
         with DBHelper(tablename) as db:
             db.insert(...)
             db.update(...)
    """
    def __init__(self, table):
        self.conn = connect(DBPATH)
        self.table = table
        
    def __enter__(self):
        return self

    def __exit__(self, t, value, tb):
        self.conn.close()

    def insert(self, value):
        """添加
        
        参数: 
              value     字典{"field": "name"}
        """
        s = "(?)" if len(value) == 1 else str(("?",) * len(value.values())).replace("'", "")
        f = "({0})".format(value.keys()[0]) if len(value) == 1 else tuple(value.keys())
        sql = "insert into {0} {1} values {2}".format(self.table, f, s)
        try:
            c = self.conn.cursor()
            r = c.execute(sql, tuple(value.values()))
            self.conn.commit()
        except Exception as ex:
            raise Exception(ex)
            return False

        return r

    def update(self, key, value):
        """修改

        参数:
              _id       要更新记录id
              value     字典{"title": "hitfm", ["desc": "cri", "url": "mms://live.hitfm.cn/fm887"]}

        """
        fields = ",".join(map(lambda x: "{0}=?".format(x), value.keys()))
        condition = ",".join(map(lambda x: "{0}=?".format(x), key.keys()))
        if key:
            sql = "update {0} set {1} where {2}".format(self.table, fields, condition)
        else:
            sql = "update {0} set {1}".format(self.table, fields)
        v = value.values()
        v.extend(key.values())
        r = self.conn.execute(sql, tuple(v))
        self.conn.commit()

        return r

    def find(self, andcond, orcond, page_index=1, page_size=10, all_item=False):
        """查找

        参数:
              andcond:      and 条件
              orcond:       or 条件
              page_index    索引
              page_size     页数
              all_item      是否所有记录
        """
        page_index -= 1
        fields = ""
        value = ()
        if andcond:
            syn = " and " if len(andcond) > 1 else ""
            fields = syn.join(map(lambda x: "{0}=?".format(x), andcond.keys()))
            value = tuple(andcond.values())
        if orcond:
            syn = " or " if len(orcond) > 1 else ""
            fields += syn.join(map(lambda x: "{0}=?".format(x), orcond.keys()))
            value += tuple(orcond.values())
        if fields:
            sql = "select * from {0} where {1} limit {2}, {3}".format(self.table, fields, page_size * page_index, page_size)
        else:
            sql = "select * from {0} limit {1}, {2}".format(self.table, page_size * page_index, page_size)

        r = self.conn.execute(sql, tuple(value))
        r = list(r)

        return r

    def delete(self, condition):
        """删除
        """
        s = "".join(map(lambda x: "{0}=?".format(x), condition.keys()))
        sql = "delete from {0} where {1}".format(self.table, s)

        r = self.conn.execute(sql, tuple(condition.values()))
        self.conn.commit()

        return r


__all__ = ["DBHelper"]
