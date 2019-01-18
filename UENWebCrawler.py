import scrapy
import csv


class uenSpider(scrapy.Spider):
    name = "uen_spider"
    start_urls = []
    uen_list = []
    base_url = "https://opencorpdata.com/sg/"

    ## extract list of UENs from csv
    with open('uen_numbers.csv', 'r') as rf:
        reader = csv.reader(rf, delimiter = ",")
        for row in reader:
            if(row != "-"):
                uen_list.append(row[0])

    ## generate list of URLs for spider to crawl
    for uensss in uen_list:
        url = base_url + uensss
        start_urls.append(url)

    # name = "uen_spider"
    # start_urls = ['https://opencorpdata.com/sg/200718096M']

    def parse(self, response):

        ## iterate through table to retrieve UEN, Company Name,
        ## Address of Company and Company Description
        SET_SELECTOR = 'tr'

        uen = ""
        nature = ""

        for item in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'td ::text'

            if item.css(NAME_SELECTOR).extract_first() == "Unique Entity Number (UEN)":
                uen = item.css(NAME_SELECTOR)[1].extract()

            if item.css(NAME_SELECTOR).extract_first() == "Entity Name":
                en_name = item.css(NAME_SELECTOR)[1].extract()

            if item.css(NAME_SELECTOR).extract_first() == "Street Address":
                address_array = []
                for addr in item.css(NAME_SELECTOR):
                    address_array.append(addr.extract())
                address_array1 = address_array[1:len(address_array)]
                address = " ".join(address_array1)

            if item.css(NAME_SELECTOR).extract_first() == "Primary SSIC Description":
                nature = item.css(NAME_SELECTOR)[1].extract()

        ## clean data scrapped by removing '\t's and '\n's
        len_uen = len(uen)
        len_nature = len(nature)
        len_address = len(address)
        len_name = len(en_name)
        uen_new = uen[3:len_uen-2]

        nature_new = nature[3:len_nature-2]
        address_new = address[3: len_address-2]
        name_new = en_name[3:len_name-2]


        yield {
            "uen": uen_new,
            "address1": address_new,
            "entity name": name_new,
            "nature": nature_new
        }
