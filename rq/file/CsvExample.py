import csv



########################################  reader ##################################
file = "../dataparse/re/doubanTop250.csv"
# 使用 reader 方式进行读取   utf-8-sig
with open(file, mode='r', encoding="utf-8") as f:
    reader = csv.reader(f)
    # 如果有表投
    # headers = next(reader)
    for row in reader:
        print("rank: {}, name: {}, year: {}, socre: {}, person_nums: {}".format(row[0], row[1],
                                                                                row[2], row[3], row[4]))

# 使用 readerDict 的方式进行数据的读取
# 这种方式的话必须要有一个表头， 不然会将你的第一行数据默认当做表头
with open(file, mode='r', encoding="utf-8") as f:
    dictReader = csv.DictReader(f)
    for it in dictReader:
        print(it)

########################################  writer ########################################
# 定义表头
header_list = ["uid", "name"]
data =[
    { 8427009,"zyh"},
    { 123,"sx"}
]

writerfile = "csvExample.csv"
with open(writerfile, mode='w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    # 一次只能写入一行数据
    writer.writerow(header_list)
    # 写入多条数据
    writer.writerows(data)

# 以dict的方式进行写入 也是最常用的一种方式
dict_data= [
    {"uid": 8427009, "name": "zyh"},
    {"uid": 123, "name": "sx"}
]
with open(writerfile, mode='w', encoding="utf-8", newline="") as f:
    dictWriter = csv.DictWriter(f, header_list)
    dictWriter.writeheader()
    dictWriter.writerows(dict_data)
