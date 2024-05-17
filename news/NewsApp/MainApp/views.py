from django.shortcuts import render, redirect
import requests
from .forms import TopicForm
from NewsApp.settings import NEWS_API_KEY

def index(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            selected_topic = form.cleaned_data['topic']
            return redirect('news_by_topic', topic=selected_topic)  # Redirect to news_by_topic view
        else:
            # Handle case where form is not valid (e.g., display errors)
            context = {'form': form, 'error_message': 'Please select a valid topic.'}
            return render(request, 'index.html', context)

    # Render the form in the template
    form = TopicForm()
    context = {'form': form}
    return render(request, 'index.html', context)


def news_by_topic(request, topic):
    url = f'https://newsapi.org/v2/everything?q={topic}&from=2024-05-16&sortBy=popularity&apiKey={NEWS_API_KEY}'
    crypto_news = requests.get(url).json()

    if crypto_news['status'] == 'error':
        error_message = crypto_news['message']  # Extract error message from API response
        context = {'error_message': error_message}
        return render(request, 'error.html', context)  # Render error template

    articles = []  # Empty list to store processed articles
    if crypto_news['status'] == 'ok' and crypto_news['articles']:
        for article in crypto_news['articles']:
            articles.append({
                'title': article['title'],
                'description': article['description'],
                'image_url': article['urlToImage'],
                'url': article['url'],  # Add article URL for full story
            })

    context = {'articles': articles, 'topic': topic}  # Pass data for rendering
    return render(request, 'news.html', context)
