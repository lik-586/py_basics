from lxml import html

# 读取 HTML 文件
with open("example.html", "r", encoding="utf-8") as f:
    html_text = f.read()

    # 解析html的文本，将其转换为一个文档对象
    doc = html.fromstring(html_text)

    # 解析表头 - xpath语法
    th_list = doc.xpath("//table/thead/tr/th/text()")

    # 解析表格数据 - xpath语法
    # 获取第一行数据
    td_list = doc.xpath("//table/tbody/tr[1]/td/text()")

    # 获取所有行数据
    tr_list = doc.xpath("//table/tbody/tr")
    for tr in tr_list:
        td_list = tr.xpath("./td/text()")