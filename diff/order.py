# -*- coding:UTF-8 -*-

import json
import math

import requests

from diff.tiaofangzi import Tiaofangzi


class Shanghuzhongxin(object):
    global null
    null = ""
    # 定义的heade跳房子的headersl

    headers = {
        "Origin": "http://www.tiaofangzi.com",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json",
        "Cookie": "access_token=",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://www.tiaofangzi.com/"
    }

    # 获取商户中心订单列表的信息
    def getCenterOrderList(self, currentPage):
        url = "http://vip.shop.hualala.com/api/v1/universal?getOrderSearch"
        request_data = {
            "service": "HTTP_SERVICE_URL_ORDER",
            "method": "/orderSearch",
            "data": {
                "page": currentPage,
                "orderState": "0",
                "orderSource": "0",
                "orderType": "0",
                "startTime": "2019-01-14",
                "endTime": "2019-01-14",
                "payChannel": "0",
                "payType": "0",
                "ticketOpen": "0",
                "groupID": 1415
            },

            "type": "post",
            "groupID": "1415"

        }
        headers = {
            "Origin": "http://vip.shop.hualala.com",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-type": "application/json",
            "traceID": "3814a6e6-50a3-4b45-bf72-39144637b0ce",
            "groupID": "1415",
            "Referer": "http://vip.shop.hualala.com/meta/2/4392",
            "Cookie": "MEIQIA_EXTRA_TRACK_ID=1FWFSGT0bYCDqtRoBZ0ZSYgJ7PF; dynamic_code_session=99c96be2-4d70-40e9-acdc-2d3f1958a853; access_token=4c874156-ce08-4925-bbb2-33069bc028b9; MEIQIA_VISIT_ID=1Fk8W9l5vlmwZFgoZBVNjOLOxws",
            "Proxy-Connection": "keep-alive"
        }
        # headers_json=json.dumps(headers)
        param = json.dumps(request_data)
        response = requests.post(url, data=param, headers=headers)
        return response.text

    # 获取页数
    def pageTotal(self):

        totalsize = json.loads(self.getCenterOrderList(1))["pageResult"]["totalSize"]
        return math.ceil(float(totalsize) / 20)
        # print type(json.loads(self.getCenterOrderList(1)))
        # print type(json.loads(self.getCenterOrderList(1))["pageResult"])

    # 获取订单list
    def totallist(self):
        pass

    # 通过orderkey获取订单详情
    def get_orderinfo(self, orderkey):
        request_data = {"service": "HTTP_SERVICE_URL_ORDER",
                        "method": "/orderDetail",
                        "data": {"orderKey": orderkey},
                        "type": "post",
                        "groupID": "1415"}
        url = "http://vip.shop.hualala.com/api/v1/universal?getOrderDetail"
        headers = {
            "Origin": "http://vip.shop.hualala.com",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-type": "application/json",
            "Cookie": "access_token=d11904fc-063b-45f4-bbc4-c9dc49dd8e18",
            "Referer": "http://www.tiaofangzi.com/",
            "Proxy-Connection": "keep-alive"

        }
        param = json.dumps(request_data)
        response = requests.post(url, data=param, headers=headers)
        return json.loads(response.text)["data"]

    def diffdata(self):

        tiaofangzi = Tiaofangzi()
        tiaofangzi.tiaofangzi_orderkey()
        shanghuzhongxin = Shanghuzhongxin()
        orderList = []
        for x in shanghuzhongxin.getSHZXOrderList():
            for y in tiaofangzi.tiaofangzi_orderkey():
                if "orderKey" in x.keys():
                    if x["orderKey"] == y["orderKey"]:
                        order = {}
                        order["orderKey"] = x["orderKey"]
                        # x1_payChannelAlias=shanghuzhongxin.get_orderinfo(json.dumps(x["orderKey"]))["orderMaster"]["payChannelAlias"]
                        shanghuzhongxinPayType = \
                        shanghuzhongxin.get_orderinfo(json.dumps(x["orderKey"]))["orderMaster"]["payTypeAlias"]

                        record = tiaofangzi.get_orderinfo(json.dumps(x["orderKey"]));

                        if not record:
                            print("continue +1")
                            continue

                        if not record["paymentDetailList"]:
                            continue

                        tiaofangziPayType = record["paymentDetailList"][0]["paymentSubjectName"]
                        if x["shopID"] != y["shopID"]:
                            order["shopID"] = "shagnhuzhohgnxin:" + x["shopID"] + ";tiaofangzi:" + y["shopID"]

                        if shanghuzhongxinPayType != tiaofangziPayType:
                            order["shopOrderKey"] = "shagnhuzhohgnxin:" + x["shopOrderKey"] + ";tiaofangzi:" + y[
                                "shopOrderKey"]
                            print(order["shopOrderKey"])  # print x["shopName"]
                        #
                        # if x["paidTotalAmount"] != y["paidTotalAmount"]:
                        #     print x["paidTotalAmount"]
                        #
                        # if x["originTotalAmount"] != y["originTotalAmount"]:
                        #     print x["originTotalAmount"]
                        #
                        # if x["thirdPartyTransNo"] != y["thirdPartyTransNo"]:
                        #     print x["thirdPartyTransNo"]

                        orderList.append(order)
        return orderList

    def getSHZXOrderList(self):
        contentDictList = []
        shanghuzhongxin = Shanghuzhongxin()
        # 总页数
        pageTotal = shanghuzhongxin.pageTotal()
        currentPage = 1
        while currentPage <= pageTotal:
            content = shanghuzhongxin.getCenterOrderList(currentPage)
            contentdict = json.loads(content)['data']
            contentDictList.extend(contentdict)
            currentPage += 1
        return contentDictList


if __name__ == '__main__':
    shanghuzhongxin = Shanghuzhongxin()
    # shanghuzhongxin.getShzxorderlist()
    # print shanghuzhongxin.pageTotal()
    shanghuzhongxin.diffdata()
    # orderListResult = shanghuzhongxin.diffdata()

    # print orderListResult
