import json
import time
import re

filename = "..\\data\\" + '601998.txt'

pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
sk_number = pattern.findall(filename)


with open(filename, 'r') as load_f:
    load_dict = json.load(load_f)

sql_content = ""
for x in range(len(load_dict)):
    if load_dict[x] == "1":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content = "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "2":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "3":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "4":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "5":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "6":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "7":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "8":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "9":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)
    if load_dict[x] == "10":
        create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        valus = '{{"sk_time":"{t}","sk_name":"{k}","sk_amount":"{y}","sk_percentage":"{p}","sk_attribute":"{b}"}}'.format(
            t=load_dict[0], p=load_dict[x + 3], b=load_dict[x + 4], y= load_dict[x + 2], k=load_dict[x + 1])
        sql_content += "insert into focus_stock (create_time, sk_symbol, partner_info) values ('{0}',{1},'{2}');\n".format(
            create_time, sk_number[0], valus)

print(sql_content)

