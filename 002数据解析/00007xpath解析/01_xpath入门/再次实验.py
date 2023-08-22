from lxml import etree
xml = """  
<book>  
    <id></id>  
    <name>遍地野花香</name>  
        <name>遍地野花香1</name>  
    <price>1.23</price>  
    <nick>臭豆腐</nick>  
    <author>  
        <nick id="10086">周大强</nick>  
        <nick id="10010">周芷若</nick>  
        <nick class="joy"></nick>  
        <nick class-="">蔡依林</nick>  
        <div>  
            <nick>惹了</nick>  
        </div>  
    </author>  
    <partner>  
        <nick id="ppc">胖胖胖</nick>  
        <nick id="ppdb">胖胖不胖</nick>  
    </partner>  
</book>  
"""

et = etree.XML(xml)
result = et.xpath("/book//nick")
print(result)
