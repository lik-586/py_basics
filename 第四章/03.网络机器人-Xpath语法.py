from lxml import html

# 读取 HTML 文件
with open("example.html", "r", encoding="utf-8") as f:
    html_text = f.read()

    # 解析html的文本，将其转换为一个文档对象
    doc = html.fromstring(html_text)

    # 解析表头 - xpath语法
    # /table/thead/tr/th/text() ：表示从根节点开始匹配
    # //table/thead/tr/th/text() ：表示从任意位置开始匹配
    # th_list = doc.xpath("/html/body/div/div/table/thead/tr/th/text()")
    # th_list = doc.xpath("//table/thead/tr/th/text()")
    th_list = doc.xpath("//thead/tr/th/text()")
    print(th_list)

    # tr[1] : 表示匹配第1个tr标签
    td_list = doc.xpath("//tbody/tr[1]/td/text()")
    print(td_list)

    # last() : 表示匹配最后一个tr标签
    td_list = doc.xpath("//tbody/tr[last()]/td/text()")
    print(td_list)

    # p[@class] : 表示匹配所有具有class属性的p标签
    p_list = doc.xpath("//p[@class]/text()")
    print(p_list)

    # p[@class='xn'] : 表示匹配所有class属性值为xn的p标签
    p_list = doc.xpath("//p[@class='xn']/text()")
    print(p_list)

    # * : 表示匹配任意标签
    th_list = doc.xpath("//thead/tr/*/text()")
    print(th_list)

    # @src : 表示匹配src属性
    # @* : 表示匹配所有属性
    #a_list = doc.xpath("//td/img/@src")
    a_list = doc.xpath("//td/img/@*")
    print(a_list)