# csv操作 - 方式一：文件操作原始方式
# 写
# with open("csv_data/01.csv", "w", encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n") # 写入表头
#     f.write("张三,18,男,'football,Java'\n") # 写入数据
#     f.write("李四,20,女,Python\n")
#     f.write("王五,22,男,C++\n")

# 读
# with open("csv_data/01.csv", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip()) # strip()去掉换行符

# csv操作 - 方式二：使用csv模块(推荐)
import csv

# 写
with open("csv_data/02.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
    writer.writeheader() # 写入表头
    writer.writerow({"姓名": "张三", "年龄": 18, "性别": "男", "爱好": "football,Java"}) # 写入数据
    writer.writerow({"姓名": "李四", "年龄": 20, "性别": "女", "爱好": "Python"})
    writer.writerow({"姓名": "王五", "年龄": 22, "性别": "男", "爱好": "C++"})

# 读
with open("csv_data/02.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row) # 输出字典