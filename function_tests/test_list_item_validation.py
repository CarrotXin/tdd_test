#-*- coding:utf-8 -*-
import time

from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith 访问首页，不小心提交了一个空待办事项 
        # 输入框中没输入任何内容，它就按下了回车键

        # 首页刷新了，显示一个错误消息
        # 提示待办事项不能为空

        # 她输入了一些文字，然后再次提交，这次没有问题了

        # 她有点调皮，又提交了一个空待办事项

        # 在清单页面她看到了一个类似的错误信息

        # 输入文字后就没有问题了
        self.fail('write me!')
