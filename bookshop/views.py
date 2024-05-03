#this is me
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
#    return HttpResponse('''<h1>hello</h1><a href="https://www.youtube.com/watch?v=ES-bdt0KUZg&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=9">click this</a>''')
#def about(request):
 #   return HttpResponse("About swayanshu")
def index(request):
    
    return render(request,'index.html')
def ex1(request):
    s='''<h1> NAVIGATION BAR <a href="https://www.amazon.in/?tag=msndeskabkin-21&ref=pd_sl_5szpgfto9j_e&adgrpid=1320515071595367&hvadid=82532451009254&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=156178&hvtargid=kwd-82533067351416:loc-90&hydadcr=14452_2154372">AMAZON</a><br><a href="https://www.flipkart.com/?ef_id=4ed6ea9b03651ceef62e8e8725ed847f:G:s&s_kwcid=AL!739!10!76484920232329!76485137405439&semcmpid=sem_F1167BY7_Brand_adcenter">FLIPKART</a> Flipkart<br>'''
    return HttpResponse(s)
def analyze(request):
    djtext=request.POST.get('text','default')
    remove=request.POST.get('remove','default')
    fullcaps=request.POST.get('fullcaps','default')
    extraspaceremover=request.POST.get('extraspaceremover','default')
    newlineremover=request.POST.get('newlineremover','default')
    
    print(djtext)
    print(remove)
    print(fullcaps)
   
    analyzed=""
    if remove=="on":
        punctuations=''',./()[]:'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
       
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'converted to uppercase','analyzed_text':analyzed}
        djtext=analyzed
       
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n"and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed

    # Analyze the text

      
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
    if (remove!="on",extraspaceremover!="on",newlineremover!="on",fullcaps!="on"):
        print("error")
  
    return render(request, 'analyze.html', params)
 
    
#def capfirst(request):
 #   return HttpResponse("capitalize first")
#def newlineremove(request):
#    return HttpResponse("removing new line<a href='/'> back</a><input type='text'>")
#def spaceremove(request):
 #   return HttpResponse("space remover <a href='/'> back</a>")
#def charcount(request):
 #   return HttpResponse("char count")

from django.http import HttpResponse
from django.shortcuts import render
import pickle

import os

def write_file():

                f= open("book shop.dat","wb")

                ch='y'

                while ch =='y':

                                l={}

                                booknumber=int(input("bno"))

                                bookname=input("enter name")

                                price=int(input("enter price"))

                                qty=int(input("enter quantity"))

                                t=(booknumber,bookname,price,qty)

                                pickle .dump(t,f)

                                k=input("Do you want to continue further ?y/n:")

                f.close()

 

def read_file():

    file=open("book shop.dat","rb")

    try:

        while True:

            l1={}

            l1=pickle.load(file)

            print(l1)

    except EOFError:

        pass

    file.close() 

 

def sort_file():

    file=open("book shop.dat","rb")

    l1=[]

    try:

        while True:

            rec={}

            rec=pickle.load(file)

            l1.append(rec)

    except EOFError:

        pass

    file.close()

    print(l1)

    for i in range(0,len(l1)):

        for j in range(0,len(l1)-i-1):

            if l1[j]['price']>l1[j+1]['price']:

                l1[j],l1[j+1]=l1[j+1],l1[j]

    print(l1)

    file=open("book shop.dat","wb")

    for i in l1:

        pickle.dump(i,file)

    file.close()

def search_file():

    rec={}

    f = open('book shop.dat','rb')

    flag = False

    r=int(input("Enter booknumber to be searched"))

    while True:

        try:

            rec = pickle.load(f)

            if rec['booknumber'] == r:

                print('Book number:',rec['booknumber'])

                print('Name:',rec['bookname'])

                print('quantity:',rec['qty'])

                print('price:',rec['price'])

                flag = True

        except EOFError:

            break

    if flag == False:

        print('No Records found')

    f.close()


 

def update_file():

    f=open('book shop.dat','rb+')

    flag=False

    p=0

    rec={}

    r=int(input("book number to search"))

    m=int(input("enter price to update"))

    try:

        while True:

            p=f.tell()                           

            print("position",p)

            rec=pickle.load(f)

            if r== rec['book number']:

                rec['price']=m

                f.seek(p)

                pickle.dump(rec,f)

    except EOFError:

           pass

    f.close()

                                   
def del_file():

    f=open('book shop.dat','rb')

    f1=open('temp.dat','wb')

    flag=False

    p=0

    rec={}

    r=int(input("enter book number to search"))

    try:

        while True:

            rec=pickle.load(f)

            if r== rec['booknumber']:

                flag=True

            else:

                pickle.dump(rec,f1)

    except EOFError:

           pass

    f.close()

    f1.close()

    if flag==True:

        print("Record deleted")

    else:

        print("Record not found")

    os.remove("book shop.dat")

    os.rename("temp.dat","book shop.dat")

 


 

def sor1_file():

    file=open("book shop.dat","rb")

    l1=[]

    try:

        while True:

            rec={}

            rec=pickle.load(file)

            l1.append(rec)

    except EOFError:

        pass

    file.close()

    print(l1)

    for i in range(0,len(l1)):

        for j in range(0,len(l1)-i-1):

            if l1[j]['booknumber']>l1[j+1]['booknumber']:

                l1[j],l1[j+1]=l1[j+1],l1[j]

    print(l1)

    file=open("book shop.dat","wb")

    for i in l1:

        pickle.dump(i,file)

    file.close()

 

def updat1_file():

    f=open('book shop.dat','rb+')

    flag=False

    p=0

    rec={}

    r=int(input("enter book  number to search"))

    m=int(input("enter quantity to purchased"))

    try:

        while True:

            p=f.tell()                           

            print("position",p)

            rec=pickle.load(f)

            if r== rec['booknumber']:

                rec['qty']=rec['qty']+m

                f.seek(p)

                pickle.dump(rec,f)

    except EOFError:

           pass

    f.close()

 

 

def updat2_file():

    f=open('book shop.dat','rb+')

    flag=False

    x=0

    p=0

    rec={}

    r=int(input("enter book number to search"))

    m=int(input("enter quantity to sold"))

    try:

        while True:

            p=f.tell()                           

            print("position",p)

            rec=pickle.load(f)

            if r== rec['itemno']:

                rec['qty']=rec['qty']-m

                x=x+m*rec['price']

                print("total price",x)

                f.seek(p)

                pickle.dump(rec,f)

    except EOFError:

           pass

    f.close()

 


 

#main prog

ch= 0

while ch!=10:

    print("File Handling ")

    print("1. Create file")

    print("2. Show file")

    print("3. Search file")

    print("4. Update file for price ")

    print("5. Sort file to sort by price")

    print("6.Delete record")

    print("7.sor1 record for sort by book number ")

    print("8.updat1record for buying book")

    print("9.update2record for selling book ")

    print("10. Exit")

    ch=int(input("Enter Choice(1-10)"))

    if ch==1:

          write_file()

    elif ch==2:

          read_file()

    elif ch==3:

          search_file()

    elif ch==4:

          update_file()

    elif ch==5:

          sort_file()

    elif ch==6:

          del_file()

    elif ch==7:

          sor1_file()

    elif ch==8:

          updat1_file()

    elif ch==9:

          updat2_file()

 

    elif ch==10:

          print("Quitting")

else:

          print("Invalid Choice") 