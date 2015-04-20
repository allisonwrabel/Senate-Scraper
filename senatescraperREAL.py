import urllib2
import csv
from BeautifulSoup import BeautifulSoup


url = "http://www.senate.mo.gov/14info/BTS_Web/Daily.aspx?SessionType=R&ActionDate=3/26/2014"
html = urllib2.urlopen(url).read()


soup = BeautifulSoup(html)
senate_table = soup.find("div") 
rows = senate_table.findAll('dl')
#print rows


output_table = [] 
for dl in rows: 


    output_dts = []
    for dt in dl.findAll('dt'):
        output_dts.append(dt.text.replace('&nbsp;', ''))
    
    output_dds = []
    for dd in dl.findAll('dd'):
        output_dds.append(dd.text)
        
    output_table.append(output_dts)
    output_table.append(output_dds) 

print output_table


handle = open("outsenate.csv", "w") 
writer = csv.writer(handle)
writer.writerows(output_table)



