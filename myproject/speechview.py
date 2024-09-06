# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import speech_recognition

@csrf_exempt
def speech_to_text(request):
    if request.method == 'POST':
        recognizer = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                return JsonResponse({'text': text})
        except speech_recognition.RequestError:
            return JsonResponse({'error': 'Network error'}, status=500)
        except speech_recognition.UnknownValueError:
            return JsonResponse({'error': 'Unable to recognize speech'}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
