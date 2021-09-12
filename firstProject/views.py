from django.http import HttpResponse, request
from django.shortcuts import render




# CSRF-Cross Site Request Forgery

def index(request):
    params={}
    return render(request,'index.html',context=params)

def performOperation(request):
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    lowercase=request.POST.get('lowercase','off')
    uppercase=request.POST.get('uppercase','off')
    removespace=request.POST.get('removespace','off')
    charcount=request.POST.get('charcount','off')
    removenewline=request.POST.get('removenewline','off')
    params={}
    result=""
    text=request.POST.get('text','default')
    if(len(text)==0):
        return HttpResponse("<h1> Error!! Text Area is Empty</h1>")

    str=""
    if(removepunc=="on"):
        puncList='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for ch in text:
            if(ch not in puncList):
                result+=ch
        text=result
        str+="Remove Punctuations "
        params={'purpose':str,'analyzed_text':result}
    if(capitalize=="on"):
        result=text.capitalize()
        text=result
        str+="Capitalize "
        params={'purpose':str,'analyzed_text':text}
    if(lowercase=="on"):
        result=text.lower()
        text=result
        str+="To Lower Case "
        params={'purpose':str,'analyzed_text':text}
    if(uppercase=="on"):
        result=text.upper()
        text=result
        str+="To Upper Case "
        params={'purpose':str,'analyzed_text':text}
    
    if(removenewline=='on'):
        str+="Remove Newline "
        result=""
        for char in text:
            if(char!='\n' and char!='\r'):
                result+=char
        text=result
        params={'purpose':str,'analyzed_text':text}

    if(removespace=='on'):
        str+="Remove Space "
        result=""
        result+=text[0]
        for char in range(1,len(text)):
            if(text[char]==' ' and text[char-1]==' '):
                continue
            else:
                result+=text[char]
        text=result
        params={'purpose':str,'analyzed_text':text}
    if(charcount=="on"):
        str+=f"And The Char Count is {len(text)}"
        params={'purpose':str,'analyzed_text':text}

    if(len(params)==0):
        return HttpResponse("<h1> Error!! No Option Selected</h1>")
    else:
        return render(request,'operation.html',context=params)
            

