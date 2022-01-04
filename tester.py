import os
from unittest import TestCase
from mainClass import mainClass

url = input('Insira a url do vídeo: ')
my_path = input('Insira a url da pasta: ')
my_video = mainClass.youtubeDownloader(url, my_path)

class tester(TestCase):
    def ytDownTest(path, video):
        for frames in os.listdir(path):
            if(os.path.abspath(frames) == video):
                # Vamos checar se o caminho absoluto de f é equivalente ao retorno da função 'youtubeDownloader'
                TestCase.assertTrue(frames.lower().endswith(('.mp4'))) # Vamos checar se o arquivo é um .mp4

tester.ytDownTest(my_path, my_video)
