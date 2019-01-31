# -*- coding:UTF-8 -*-
# -*- coding:UTF-8 -*-
import requests
import json
def response_text():
    url="http://www.tiaofangzi.com/cservice/order/queryOrderMaster"
    request_data= {"sortValue":"20","orderKey":"6641891075164216111","submitTimeFrom":"20190101","submitTimeTo":"20190113","pageNo":1,"pageSize":20}
    headers = {
       "Origin": "http://www.tiaofangzi.com",
       "Accept": "*/*",
       "Accept-Encoding": "gzip, deflate",
       "Accept-Language": "zh-CN,zh;q=0.9",
       "Content-Type": "application/json",
       "Cookie": "access_token=e57b1e62-2530-4593-b3a6-a82bde993c36",
       "Proxy-Connection": "keep-alive",
       "Referer": "http://www.tiaofangzi.com/"
    }
    param = json.dumps(request_data)

    response=requests.post(url,data=param,headers=headers)


