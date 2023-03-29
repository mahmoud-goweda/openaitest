from django.shortcuts import render

# Create your views here.
import os
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config

# from openai import api_key, Model
import openai


# model_engine = Model("davinci")

@csrf_exempt
def transcribe_audio(request):
    if request.method == 'POST':

            # Get the audio file from the request
            
        try:
            audio = request.FILES['audio']
        
            # Save the audio file to the 'audio' directory
            filename = 'audio/' + audio.name

            # saveListToFile(list, filename)
            with open(filename, 'wb+') as destination:
                for chunk in audio.chunks():
                    destination.write(chunk)

            openai.api_key = config('api_key_ai') 
            audio_file= open(filename, "rb")
            transcript = openai.Audio.translate("whisper-1", audio_file)
            os.remove(filename)

            # with open(filename, 'wb') as f:
            #     for chunk in audio.chunks():
            #         f.write(chunk)
            
            # # Transcribe the audio using the OpenAI Speech-to-Text API
            # headers = {
            #     'Authorization': f'Bearer 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',
            #     'Content-Type': 'audio/wav'
            # }
            # with open(filename, 'rb') as f:
            #     response = requests.post('https://api.openai.com/v1/engines/davinci/voice/translate', headers=headers, data=f)
            # text = response.json()
            
            # Return a JSON response with the transcription result
            return JsonResponse({'text': transcript});
        except:
            os.remove(filename)
            return JsonResponse({'text': 'error cant upload'});



