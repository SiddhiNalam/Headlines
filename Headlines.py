import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

page = requests.get("http://indiatoday.intoday.in/technology/category/news/1/895.html")
soup = BeautifulSoup(page.content, 'html.parser')
hd=soup.find_all('h2')
i=0
j=1
abc=[]
while(hd):
	if(hd[i].get_text()=="Most Read"):
		break
	text=str(str(j)+" >" +hd[i].get_text())
	# text=hd[i].get_text()
	abc.append(text)
	j=j+1
	i=i+1


root = Tk()
T = Text(root, height=12, width=100)
T.pack()
T.insert(END, "Today's Headlines\n")
for x in abc:
    T.insert(INSERT, x+'\n')

mainloop()

# for i in abc:
# 	print(i)
# 	print('')