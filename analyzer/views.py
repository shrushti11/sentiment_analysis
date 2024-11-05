from django.shortcuts import render
from textblob import TextBlob

def home(request):
    sentiment_result = None
    if request.method == 'POST':
        text = request.POST['text']
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        sentiment_result = {
            "text": text,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "sentiment": "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        }
    return render(request, 'sentiment.html', {'result': sentiment_result})