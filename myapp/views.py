from django.shortcuts import render

# Create your views here.
import os
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from openai import api_key, Model
import openai


# model_engine = Model("davinci")

@csrf_exempt
def transcribe_audio(request):
    print(request)
    if request.method == 'POST':
        # Get the audio file from the request
        print(request)

        audio = request.FILES['audio']
        print(audio)
        # Save the audio file to the 'audio' directory
        filename = 'audio/' + audio.name

        # saveListToFile(list, filename)
        with open(filename, 'wb+') as destination:
            for chunk in audio.chunks():
                destination.write(chunk)

        openai.api_key = "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"
        audio_file= open(filename, "rb")
        transcript = openai.Audio.translate("whisper-1", audio_file)
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
        return JsonResponse({'text': transcript})
