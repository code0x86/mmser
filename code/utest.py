# coding: utf-8
#
# 单元测试
#

import unittest

from logic import *

__version__ = "0.1"


class LogicTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list_menu(self):
        r = list_menu()
        self.assertTrue(r)

        r = list_menu(t = "favorite")

        self.assertTrue(r)

    def test_fav(self):
        value = 3
        before = len(list_menu(t = "favorite", all_item=True))
        # 添加
        fav(value, True)
        # 删除
        fav(value, False)
        end = len(list_menu(t = "favorite", all_item=True))

        self.assertTrue(before == end)

    def test_find(self):
        andcond = {"id": 28}
        r = find(andcond = andcond)

        self.assertTrue(len(r))        

    def test_update(self):
        # 根据 title 查询，无结果
        title = {"title": "hifm"}
        _id = {"id": 28}
        value = {"desc": "this is cri hitfm fm887."}
        r = set_fm(_id, value)
        result = find(andcond = _id)

        self.assertEqual(result[0][2], value["desc"])


if __name__ == "__main__":
    unittest.main()
