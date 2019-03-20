import re
import urllib.request,urllib.parse,urllib.error
from googlesearch import search
from bs4 import BeautifulSoup
import search1 as h
import link1
x=True
if x==True:
    csv=open('final.csv','w')
    csv.write('hotel name,phone,email,link'+'\n')
    csv.close()
    k=open('jayanth.doc','w')
    d=input("enter your required search")
    print('i am seaching for google results')
    for url in search(d, tld='es', lang='es', stop=10):
    #print(url)
        k.write(url+'\n')
    k.close()
    k=open('jayanth.doc','r')
    print("Now i am opening each and every link")
    for i in k:
        link1.open1(i)
        print('successfully compleated ')
    k.close()
else:
    import sensex
        
