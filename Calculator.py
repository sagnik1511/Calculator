#!/usr/bin/env python
# coding: utf-8

# In[52]:


""" 
author
s_agnik1511  
"""


#   This calculator is made within 15 hours of hardwork.
# this is a simple calculator with 4 basic arithmatic operators which cn produce any value from -10e18 to +10e18




#hope you like it





from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("400x600")

def click1(x):
    s=entry.get()
    entry.delete(0,END)
    b=str(s)+str(x)
    entry.insert(0,b)

def capC():
    entry.delete(0,END)
    e1.delete(0,END)
    entry.config(bg="white")

def ch(c):
    c=chr(c)
    if c=='/' or c=='+' or c=='-' or c=='*':
        return True
    else :
        return False

def CC():
    str1=str(entry.get())
    entry.delete(0,END)
    str2=str(str1[0:len(str1)-1])
    entry.insert(0,str2)
    
def eqq():
    al=str(entry.get())
    entry.delete(0,END)
    e1.delete(0,END)
    try:
        al=str(eval(al))
        entry.config(bg="green")
    except:
        al="Math Error"
        entry.config(bg="red")
        
    e1.insert(0,al)
    
              
entry=Entry(root,width=50)

b1=Button(root,text="0",height=5,width=9,command=lambda: click1(0))
b2=Button(root,text="1",height=5,width=9,command=lambda: click1(1))
b3=Button(root,text="2",height=5,width=9,command=lambda: click1(2))
b4=Button(root,text="3",height=5,width=9,command=lambda: click1(3))
b5=Button(root,text="4",height=5,width=9,command=lambda: click1(4))
b6=Button(root,text="5",height=5,width=9,command=lambda: click1(5))
b7=Button(root,text="6",height=5,width=9,command=lambda: click1(6))
b8=Button(root,text="7",height=5,width=9,command=lambda: click1(7))
b9=Button(root,text="8",height=5,width=9,command=lambda: click1(8))
b10=Button(root,text="9",height=5,width=9,command=lambda: click1(9))
b11=Button(root,text="CE",height=2,width=9,command=capC)
b18=Button(root,text="C",height=2,width=9,command=CC)
b12=Button(root,text="+",height=5,width=14,command=lambda: click1("+"))
b13=Button(root,text="-",height=5,width=14,command=lambda: click1("-"))
b14=Button(root,text="x",height=5,width=14,command=lambda: click1("*"))
b15=Button(root,text="=",height=8,width=48,command=eqq)
b16=Button(root,text="÷",height=5,width=14,command=lambda: click1("/"))
b17=Button(root,text=".",height=5,width=9,command=lambda: click1("."))
e1=Entry(root,width=50)
c1=Canvas(height=400,width=500,bg="green")
#implementing
entry.place(x=50,y=10)
e1.place(x=50,y=35)
b2.place(x=10,y=65)
b3.place(x=90,y=65)
b4.place(x=170,y=65)
b5.place(x=10,y=160)
b6.place(x=90,y=160)
b7.place(x=170,y=160)
b8.place(x=10,y=255)
b9.place(x=90,y=255)
b10.place(x=170,y=255)
b1.place(x=90,y=350)
b16.place(x=250,y=65)
b14.place(x=250,y=160)
b13.place(x=250,y=255)
b12.place(x=250,y=350)
b18.place(x=10,y=397)
b11.place(x=10,y=350)
b17.place(x=10,y=375)
b17.place(x=170,y=350)
b15.place(x=11,y=445)
root.mainloop()


# In[ ]:





# In[ ]:




