
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    # return HttpResponse('Hello')
   

def analize(request):
    dj_text=(request.POST.get('dj_text','default'))
    removepunc=(request.POST.get('removepunc','off'))
    removenewline=(request.POST.get('removenewline','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    spaceremove=(request.POST.get('spaceremove','off'))
    charcount=(request.POST.get('charcount','off'))
    # check which button is on
    if removepunc=='on':
        analized=''
        punctuation='''/?,.;:'")(*#$%^&//.{.;'})[],;'''
        for char in dj_text:
            if char not in punctuation:
                analized=analized + char
        
        param={'purpose':'Remove Punctuation from text','analize_text':analized}
        dj_text=analized
        # return render(request,'analize.html',param)

    if(charcount=='on'):
        
        count=0
        for i in dj_text:
            if i.isalpha():
                count=count+1
        param={'purpose':'Count number of character','analize_text':count}
        
    if(fullcaps=='on'):
        analized=''
        for i in dj_text:
            analized=analized+i.upper()
        param={'purpose':'Upper case','analize_text':analized}
        dj_text=analized
        # return render(request,'analize.html',param)  

    if(spaceremove=='on'):
        analized=''
        for index,i in enumerate (dj_text):
            
            if not (dj_text[index]==' 'and dj_text[index + 1] == ' ') :
                an=an+i  
        param={'purpose':'Extra space remove','analize_text':analized}
        dj_text=analized
        # return render(request,'analize.html',param)    
    if(removenewline=='on' ):
        analized=''
        for char in dj_text:
            if  char!='\n' and char!='\r' :
                analized = analized + char
            else:
                print('no')
        print('Analyze :',analized)
        param={'purpose':'Remove new line','analize_text':analized}
    
        # return render(request,'analize.html',param)
        #     
    if(removepunc!='on' and removenewline!='on'and spaceremove!='on'and fullcaps!='on' and charcount!='on'):
        return HttpResponse('Please select any one operation and try Again !')
    
    return render(request,'analize.html',param)  





    