# !/usr/bin/env python
# -*-coding: utf-8-*-
import xlrd
import xlsxwriter

import json


# 生成excel文件11
def generate_excel(rec_data):
    # 打开excel表格
    # workbook = xlwt.Workbook('uft-8','/home/hualala/diff.xlsx')
    # workbook = xlsxwriter.Workbook('/home/hualala/diff.xlsx')
    workbook = xlsxwriter.Workbook('/Users/wangrui/PycharmProjects/untitled11/diff.xlsx')

    worksheet = workbook.add_worksheet()

    bold_format = workbook.add_format({'bold': True})
    bold_format = workbook.add_format({'bold': True})
    money_format = workbook.add_format({'num_format': '$#,##0'})
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

    worksheet.set_column(1, 1, 15)

    worksheet.write('A1', 'orderKey', bold_format)
    worksheet.write('B1', 'shoporderKey', bold_format)
    worksheet.write('C1', 'id_1', bold_format)
    worksheet.write('D1', 'id_1_doc', bold_format)
    worksheet.write('E1', 'id_2_doc', bold_format)
    worksheet.write('F1', 'id_2_doc', bold_format)
    row = 1
    col = 0
    for item in (rec_data):
        # 使用write_string方法，指定数据格式写入数据
        worksheet.write_string(row, col, str(item['orderKey']))

        worksheet.write_string(row, col + 1, item['shoporderKey'])
        # worksheet.write_string(row, col + 2, str(item['id_1']))
        # worksheet.write_string(row, col + 3, item['id_1_doc'])
        # worksheet.write_string(row, col + 4, str(item['id_2']))
        # worksheet.write_string(row, col + 5, item['id_2_doc'])
        row += 1
    workbook.close()


# if __name__ == '__main__':
    # rec_data = [{'sku_id': 2685373,
    #             'id_1': 16161212,
    #             'id_2': 23853166,
    #             'id_2_doc': u'【分享/吐槽大会】宝宝发烧用退热贴真的有效吗？',
    #             'sku_title': u'啾啾 CHUCHU 新宝宝水枕（适用年龄0岁以上）',
    #             'id_1_doc': u'宝宝退热捷径，别忘了这些物理降温宝宝体内致热源刺激体温调节中枢导致产热增加、散热减少的症状即为发热。\n'}]


    # generate_excel(rec_data)
