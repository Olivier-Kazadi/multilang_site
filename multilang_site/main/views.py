from django.shortcuts import render
from .models import Article
import openai
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

openai.api_key = settings.OPENAI_API_KEY

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})


@csrf_exempt
def chatbot(request):
    answer = None
    if request.method == 'POST':
        question = request.POST.get('question')
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokes=50
        )
        answer = response.choices[0].message['content'].strip()
        return render(request, 'main/chatbot.html', {'question': question, 'answer': answer})
    return render(request, 'main/chatbot.html')