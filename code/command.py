# coding: utf-8
#
# 执行command
#
from sys import argv
from cmd import Cmd

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

    def do_EOF(self, line):
        exit(0)

    def run(self):
        self.cmdloop()


__all__ = ["Command"]
