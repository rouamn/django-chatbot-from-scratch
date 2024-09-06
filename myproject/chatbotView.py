from .chat import get_response , bot_name

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_message = data['message']
        bot_response = get_response(user_message)
        return JsonResponse({'response': bot_response})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)