# webcrawl-opencorpdata

Simple web spider to compile information of Singapore companies based on a list of Unique Entity Numbers (UENs).The following information are extracted from from an online database (www.opencorpdata.com):
-UEN
-Entity Name
-Company's Street Address
-Company's Nature of Business

Web spider built using Scrapy on Python 3.6.3

to run: 
```scrapy runspider UENWebCrawler.py -o "Name of CSV File".csv```
