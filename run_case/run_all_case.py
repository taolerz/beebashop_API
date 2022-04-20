#encoding=utf-8
import HTMLTestRunner
import unittest,time,os
case_path=r'D:\taoler\autotestfile\beebashop_API\test_case'
#case_path=r'F:\autotestfile\beebashop_API\test_case'    # 用例路径
print (case_path)
report_path = os.path.join(os.getcwd(), 'report')   # 报告存放路径
print (report_path)

def all_case():
    # discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern="test*.py", top_level_dir=case_path)
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern="uiautotest.py", top_level_dir=case_path)

    print (discover)
    return discover

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))   # 1、获取当前时间，这样便于下面的使用。

    report_abspath = os.path.join(report_path, "result_"+now+".html")       # 2、html报告文件路径

    fp = open(report_abspath, "wb")                                           # 3、打开一个文件，将result写入此file中
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'比巴微商城接口自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # 4、调用add_case函数返回值
    runner.run(all_case())
    fp.close()
    print(fp)

