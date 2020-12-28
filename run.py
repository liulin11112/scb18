
from python_1222.lesson07 import read_case,api_fun,write_result

#断言：响应结果与预期结果判断
def execute_fun(filename,sheetname):
    cases = read_case(filename,sheetname)
    for case in cases:
        case_id = case['case_id']       #获取用例编号
        url = case['url']
        data = eval(case['data'])
        expect = eval(case['expect'])
        # print(case_id,expect)
        expect_msg = expect['msg']

        real_result = api_fun(url = url,data = data)
        real_msg = real_result['msg']
        # print(real_result)
        print('期望结果为：{}'.format(expect_msg))
        print('实际结果为：{}'.format(real_msg))

        if expect_msg==real_msg:
            print("第{}条用例执行通过".format(case_id))
            final_re = 'Passed'
        else:
            print("第{}条用例执行不通过".format(case_id))
            final_re = 'Failed'
        write_result(filename,sheetname,case_id+1,8,final_re)          #写入结果到测试用例Excel
        print('*'*30)
        
#改成Jenkins目录下的xlsx文件
execute_fun('D:\\study\\git\\scb18\\test_data\\test_case_api.xlsx', 'login')