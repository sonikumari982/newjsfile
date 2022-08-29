# a=(1/2)(2/3)(10/6)
# print(float(a))
# a="soni"
# print(f"good morning {a}")
# days = 365
# print(f"There are {days}in a year")
# ##
# a=max(False,-3,-4)
# b=(a,2,7)
# print(b)
#####################3
# import requests
# b=requests.get("https://www.merakilearn.org/course-content/miscellaneous/3/0")
# print(b)
# a=requests.get("https://web.whatsapp.com/")
# print(a)
# somedata=requests.get("http://saral.navgurukul.org/api/courses")
# print(somedata)
# #####
# import json
# from os import close

# p =  { "name":"John", "age":30, "city":"New York"}
# i=open("newfil1.json","w")
# json.dump(p,i)
# i=close()
#########
# import json
# import requests
# b=requests.get("http://saral.navgurukul.org/api/courses")
# print(b)
# with open("project1.json","w") as d:
#     json.dump(b.json(),d,indent=5)
#     print(b)
#############
# import json
# import requests


# file=requests.get("http://saral.navgurukul.org/api/courses")
# with open("fold11.json","w") as fi:
#     json.dump(file.json(),fi,indent="")
#     print(file)
# opning=open("fold11.json", "r")
# content = opning.read()
# # print(content)
# c={"availableCourses"}
# dic1={}
# dic1.update(c)
# # dic1.update(c)
# print(dic1)
# myid={}
# myname={}
# mytyp={}
# mylogo={}
# myshort_description={}
# for q,i in content.items():
#     for f in i:
#         for j,k in f.items():
#             if "id"==j:
#                 myid[j]=k
#             if "name"==j:
#                 myname[j]=k
#             if "type"==j:
#                 mytyp[j]=k
#             if "logo"==j:
#                 mylogo[j]=k
#             if "short_description"==j:
#                 myshort_description[j]=k
# mydic={}
# mydic.update(myid)
# mydic.update(myname)
# mydic.update(mytyp)
# mydic.update(mylogo)
# mydic.update(myshort_description)
# with open("file12.json","w")as fl:
#     json.dump(mydic,fl,indent="")
#     print(mydic)
#########
# from cmath import nan
# from operator import length_hint


# a=[1,2,3,4,5]
# # b=a.reverse()

# # g=b
# # print(g)
# f=[]
# i=0
# while i<=len(a):
#     f.append(a[i])
#     c=f
#     f.append(c)
#     print(f)
#     i=i+1
# print(f)
##########
from webbrowser import get
import requests
from bs4 import BeautifulSoup
forlink=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
# print(forlink)
b=forlink.content
a=forlink.text
# print(a)
supe=BeautifulSoup(a,"html.parser")
# print(supe)
# c=supe.find("h1").get_text()
b=supe.find("titel").get_text()
# print(c)
print(b)