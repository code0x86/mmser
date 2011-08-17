# coding: utf-8
#
# 所有操作逻辑
#

from dbhelper import DBHelper as dbh

__version__ = "0.1"

FMTABLE = "fm"
FAVTABLE = "favorite"


def list_menu(t = "fm", page_index = 1, page_size = 20, all_item=False):
    """显示菜单

    参数:
          t            [fm/favorite]
          page_index   索引
          page_size    条数
          all_item     是否所有的记录
    """
    table = FMTABLE if t == "fm" else FAVTABLE
    with dbh(table) as db:
        r = db.find("", "", page_index = page_index, page_size = page_size, all_item=all_item)

        return r


def set_fm(key, value):
    """设置fm

    参数:
          key           更新条件 e.g. {'title': 'test' [...]}
          value         更新的值 e.g. {'title': 'test_change' [...]}
    """
    with dbh(FMTABLE) as db:
        r = db.update(key, value)
        
        return r


def fav(_id, b):
    """收藏操作
    
    参数:
         _id            fmid
         b              Boolean 添加/删除
    """
    with dbh(FAVTABLE) as db:
        value = {"fmid": _id}
        if b:
            r = db.insert(value)
        else:
            r = db.delete(value)

        return r


def find(t = "fm", andcond=None, orcond=None, page_index = 1, page_size = 20, all_item=False):
    # TODO 模糊查询
    """查找

    参数:
          t            表名，默认fm
          andcond      与查询条件 
          orcond       或查询条件
          page_index   索引
          page_size    条数
          all_item     所有记录
    """
    table = FMTABLE if t == "fm" else FAVTABLE
    with dbh(table) as db:
        r = db.find(andcond, orcond, page_index = page_index, page_size = page_size, all_item=all_item)

        return r
    


__all__ = ["list_menu", "set_fm", "fav", "find"]
