from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

#텍스트에서 명사만 list로 반환해줌 (중복 고려 x)
def KLT2023_Nlist(text):
    from konlp.kma.klt2023 import klt2023
    klt = klt2023()
    list = klt.nouns(text) 
    return list

def result(request):
    text = request.GET['text']
    # replaced length
    replaced_length = len(text.replace(" ",""))
    # simple ver.
    simple_length = len(text)
    simple_text_list = text.split()
    simple_word_dict = {}
    for word in simple_text_list:
        if word in simple_word_dict:
            simple_word_dict[word] += 1
        else:
            simple_word_dict[word] = 1
    simple_words = sorted(simple_word_dict.items(),key=lambda x:x[1], reverse=True)
    # simple ver 총 단어 개수
    simple_total_count = len(simple_word_dict)
    # KLT2023 ver.
    klt_list = KLT2023_Nlist(text)
    klt_word_dict = {}
    for word in klt_list:
        if word in klt_word_dict:
            klt_word_dict[word] += 1
        else:
            klt_word_dict[word] = 1
    klt_words = sorted(klt_word_dict.items(),key=lambda x:x[1], reverse=True)
    # klt2023 ver 총 단어 개수
    klt_total_count = len(klt_word_dict)

    return render(request, "result.html", {"simple_length":simple_length,'simple_words':simple_words,"simple_total_count":simple_total_count,"replaced_length":replaced_length, "klt_words":klt_words, "klt_total_count":klt_total_count})