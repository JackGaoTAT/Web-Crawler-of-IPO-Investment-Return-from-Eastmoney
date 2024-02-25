import requests
import json
import csv

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"
}
with open("新股收益率数据.csv","a",encoding = "utf-8-sig", newline="") as csva:
    writer = csv.writer(csva)
    writer.writerow(["股票简称",
        "股票代码",
        "上市日期",
        "发行价",
        "最新价",
        "发行中签率",
        "总发行数",
        "首日涨幅",])
    for i in range(1,70):
        param = {
'callback': 'jQuery112305089425983075067_1690425404979',
'sortColumns': 'LISTING_DATE,SECURITY_CODE',
'sortTypes': '-1,-1',
'pageSize': '50',
'pageNumber': f'{i}',
'reportName': 'RPTA_APP_IPOAPPLY',
'quoteColumns': 'f2~01~SECURITY_CODE,f14~01~SECURITY_CODE',
'quoteType': '0',
'columns': 'ALL',
'source': 'WEB',
'client': 'WEB',
'filter':'((APPLY_DATE>\'2010-01-01\')(|@APPLY_DATE="NULL"))((LISTING_DATE>\'2010-01-01\')(|@LISTING_DATE="NULL"))(TRADE_MARKET_CODE!="069001017")'
}

        url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
        res = requests.get(url, params=param, headers=headers)
        data = res.text
        obj = data.replace('jQuery112305089425983075067_1690425404979(','')
        obj = obj[:-2]
        obj_file_name = 'obj_file' + str(i) + '.txt'
        with open(obj_file_name, 'w', encoding='utf-8') as f:
            f.write(obj)
        file_name = 'page' + str(i) + '.json'
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(obj)
        dic = json.loads(obj)
        final = dic["result"]["data"]
        #print(f"股票简称：{股票简称}\t股票代码：{股票代码}\t中签率：{发行中签率}")
        for each in final:
            股票简称 = each["f14"]
            股票代码 = each["SECURITY_CODE"]
            上市日期 = each["LISTING_DATE"]
            发行价 = each["ISSUE_PRICE"]
            最新价 = each["TNEW_PRICE"]
            发行中签率 = each['ONLINE_ISSUE_LWR']
            总发行数 = each ["ISSUE_NUM"]
            首日涨幅 = each["CHANGE_RATE"]
            writer.writerow([each["f14"],each["SECURITY_CODE"],each["LISTING_DATE"],each["ISSUE_PRICE"],each["TNEW_PRICE"],each['ONLINE_ISSUE_LWR'],each ["ISSUE_NUM"],each["CHANGE_RATE"]])