# -*- coding:UTF-8 -*-
import requests
import json


class Tiaofangzi(object):
    global null
    null = ''
    global headers
    headers = {
        "Origin": "http://www.tiaofangzi.com",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json",
        "Cookie": "access_token=d11904fc-063b-45f4-bbc4-c9dc49dd8e18",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://www.tiaofangzi.com/"
    }

    # 获取订单列表
    def tiaofangzi_orderkey(self):
        url = "http://www.tiaofangzi.com/cservice/order/queryOrderMaster"
        request_data = {"sortValue": "100000", "groupName": "1415", "submitTimeFrom": "20190114",
                        "submitTimeTo": "20190114", "pageNo":1 , "pageSize": 2000}
        param = json.dumps(request_data)
        response = requests.post(url, data=param, headers=headers)
        # print response.text
        return json.loads(response.text)['data']['records']


    #获取订单详情
    def get_orderinfo(self, orderkey):
        request_data = {"orderKey": orderkey}
        print type(request_data)
        url = "http://www.tiaofangzi.com/cservice/order/queryOrderDetail"
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            # "Content-Length": "271",
            "Content-Type": "application/json",
            "Cookie": "access_token=d11904fc-063b-45f4-bbc4-c9dc49dd8e18",
            "Host": "www.tiaofangzi.com",
            "Origin": "www.tiaofangzi.com",
            "Proxy-Connection": "keep-alive",
            "Referer": "www.tiaofangzi.com",
            "User-Agent": "Mozilla/5.0 Maclongosh longel Mac OS X 10_13_6 AppleWebKit/537.36 KHTML, like Gecko Chrome/71.0.3578.98 Safari/537.36"
        }
        param = json.dumps(request_data)
        response = requests.post(url, data=param, headers=headers)
        return json.loads(response.text)['data']["records"]
        # return response.text["data"]


if __name__ == '__main__':
    tiaofangzi = Tiaofangzi()



    # x = tiaofangzi.get_orderinfo("6646342727262807992")
    x = tiaofangzi.get_orderinfo("6646363239925942200")
    # u'6646363239925942200'
    print
    # print tiaofangzi.tiaofangzi_orderkey()
