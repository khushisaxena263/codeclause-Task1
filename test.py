import pyshorteners
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short("https://www.amazon.in/dp/B09ZBFD6TJ/ref=QAHzEditorial_en_IN_2?pf_rd_r=05JZND6XZVMPEZ0NRS2J&pf_rd_p=e3ef03f9-b77d-4e9c-ad40-a07ba17e0506&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-10&pf_rd_t=&pf_rd_i=1389401031&ie=UTF8&ref_=CLP_MH9_BSMidrange_2&th=1")
print(x)