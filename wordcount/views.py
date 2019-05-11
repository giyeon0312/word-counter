from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split()
    word_dictionary={} #빈 사전형 자료 만들어놓기
    for word in words:#words의 값들을 순환하면서
        if word in word_dictionary:#이미 있는 word면 하나 증가
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1#없으면 값을 1로하여 리스트에 삽입
    return render(request,'result.html',{'full':text,'total':len(words),'dictionary':word_dictionary.items()})