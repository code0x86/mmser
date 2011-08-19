# coding: utf-8
#
# 执行command
#

from sys import argv
from cmd import Cmd

from logic import *


class Command(Cmd):
    """
        命令操作行
    """
    intro = "Welcome to my fm tool." \
        "\n" \
        "常用命令:\n"\
        "    ?        显示帮助"
    prompt = "> "

    def default(self, line):
        if not line: return

        if line in ("quit", "exit", "q"):
            self.do_EOF(None)
        else:
            print "unknown"
    
    def do_list(self, line):
        r = list_menu()
        self._format(r)

    def do_find(self, line):
        s = line.decode("utf-8").encode("utf-8")
        query = {"title": s}
        r = find(orcond=query)
        self._format(r)

    def do_EOF(self, line):
        exit(0)

    def run(self):
        self.cmdloop()

    def _format(self, r):
        for x in r:
            print str(x[0]), x[1], x[3]


__all__ = ["Command"]
