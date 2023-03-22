from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['text']
    text_list = text.split()
    word_dict = {}
    print('프린트',text, text_list)
    for word in text_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    print('word_dict',word_dict)
    words = sorted(word_dict.items(),key=lambda x:x[1], reverse=True)

    return render(request, "result.html", {'words':words})