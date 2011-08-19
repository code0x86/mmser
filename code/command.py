# coding: utf-8
#
# 执行command
#
import codecs
from sys import argv
from cmd import Cmd

from logic import *

__version__ = "0.1"

class Command(Cmd):
    """
        命令操作行
    """
    intro = "Welcome to my fm tool." \
        "\n" \
        "常用命令:\n"\
        "    ? (help)     显示帮助\n"\
        "    list         显示FM列表\n"\
        "    find name    查找\n"\
        "    fav fmid     收藏\n"\
        "    unfav fmid   取消收藏\n"\
        "    set fmid     设置默认播放\n"\
        "    info fmid    得到详细"
    prompt = "> "

    def default(self, line):
        if not line: return

        if line in ("quit", "exit", "q"):
            exit(0)
        else:
            print "unknown"
    
    def do_list(self, line):
        r = list_menu()
        self._format(r)

    def do_find(self, line):
        s = unicode(line, "utf-8")
        query = {"title": s}
        r = find(orcond=query)
        self._format(r)

    def do_fav(self, line):
        _id = self._convert(line)
        if _id: fav(_id, True)
        
    def do_unfav(self, line):
        _id = self._convert(line)
        if _id: fav(_id)

    def do_set(self, line):
        _id = self._convert(line)
        if _id:
            set_fm({}, {"isdefault": 0})
            set_fm({"id": _id}, {"isdefault": 1})

    def do_info(self, line):
        _id = self._convert(line)
        if _id:
            r = find(andcond={"id": _id})
            if r:
                r = r[0]
                print "id:       ", str(r[0])
                print "标题:     ", r[1]
                print "简介:     ", r[2]
                print "url:      ", r[3]
                print "加入时间: ", r[5]
            else:
                print "不存在此记录，请确认."
            
    def _format(self, r):
        for x in r:
            if x[6] == 1: print "*",
            else: print " ",
            print str(x[0]), x[1], x[3]

        print "('*' 为默认.)" 

    def _convert(self, line):
        _id = line.split(" ")
        if _id:
            try:
                _id = int(_id[0])
                return _id
            except Exception as ex:
                print "输入的ID错误."
                return None
                
    def run(self):
        self.cmdloop()
            

__all__ = ["Command"]
