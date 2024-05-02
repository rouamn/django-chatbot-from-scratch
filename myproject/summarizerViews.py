import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .summarizer import summarize_text

@csrf_exempt
def summarize(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        text = data['text']
        summary = summarize_text(text)
        return JsonResponse({'summary': summary})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
