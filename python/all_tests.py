#! /usr/bin/env python
#coding=utf-8
import unittest
import time,sys
import HTMLTestRunner
sys.path.append("\test_case")
from code import *

testunit=unittest.TestSuite()


#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))

#取前面时间
now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())

#定义个报告存放路径，支持相对路径。
filename = "F:\\selenium_python\\python\\report\\"+now+'.html'
fp = file(filename, 'wb')

runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')

#执行测试用例
runner.run(testunit)
