# pdfsummarizerViews.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .pdfsummarizer import summarize_pdf

@csrf_exempt
def summarize_pdf_view(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        try:
            pdf_file = request.FILES['pdf_file']
            summary = summarize_pdf(pdf_file)
            return JsonResponse({'summary': summary})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
