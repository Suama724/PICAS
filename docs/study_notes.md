# .XML 文件

其应该具有这种形式:
```xml
<root>
<child1>str content</child1>
<>
</root>
```
```xml
<article mdate="2002-01-03" key="persons/Codd71a">
<author>E. F. Codd</author>
<title>Further Normalization of the Data Base Relational Model.</title>
<journal>IBM Research Report, San Jose, California</journal>
<volume>RJ909</volume>
<month>August</month>
<year>1971</year>
<cdrom>ibmTR/rj909.pdf</cdrom>
<ee>db/labs/ibm/RJ909.html</ee>
</article>
```
其中标签中可以写attr, 它们相当于作为元元tag, 其信息与论文本身(基本)不沾, 只是方便管理检索
处理xml: xml.etree.ElementTree 库

信源: 定义 https://zh.wikipedia.org/wiki/XML
      库 https://blog.csdn.net/qq233325332/article/details/130799948