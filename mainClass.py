from posixpath import curdir
from pytube import YouTube
from PIL import Image
import cv2, os, glob, pyautogui

class mainClass:
# Fazer o download do vídeo através de sua URL do YouTube
# Salvar o vídeo na pasta selecionada

    def youtubeDownloader(video_url, videos_path):
        yt = YouTube(video_url) # Esse método seleciona o URL do vídeo em questão
        yt = yt.streams.get_highest_resolution() # Esse método busca os resultados correspondentes e seleciona aquele que possuir a maelhor resolução
        my_video = yt.download(videos_path) # Realizamos o download especificando a pasta de destino
        return my_video

# Converter o vídeo para uma seleção de frames

    def frameCreator(video):
        vidcap = cv2.VideoCapture(video) # Captura os frames do vídeo
        success, image = vidcap.read() # Seleciona um frame
        count = 0
        while success:
            cv2.imwrite('frame%d.jpg' % count, image) # Transformamos os frames em .JPEG    
            success, image = vidcap.read() # Seleciona o próximo frame
            print('Lendo um novo frame: ', success)
            count += 1

        # Salvar os frames na pasta selecionada

        file_path = os.path.realpath(__file__) # Vamos buscar a pasta deste arquivo .py
        current_dir = os.path.dirname(file_path)
        destination_dir = input('Insira o caminho para a pasta onde serão salvos os frames: ')

        for frames in os.listdir(current_dir):
            if frames.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Verificamos se os arquivos na pasta atual são uma imagem (.JPEG)
                os.replace(current_dir + '\\' + frames, destination_dir + '\\' + frames) # Enviamos os arquivos para a pasta selecionada

        return destination_dir

# Transformar os frames num gif

    def gifCreator(destination_dir):
        gif_name = input('Insira o nome do gif: ') + '.gif'

        frames = [Image.open(image) for image in glob.glob(f"{destination_dir}/*.JPG")]
        frames[0].save(gif_name, format="GIF", append_images=frames[1:], save_all=True, optimize=False, duration=75, loop=0)

        # Mover o gif para a pasta de destino

        file_path = os.path.realpath(__file__) # Vamos buscar a pasta deste arquivo .py
        current_dir = os.path.dirname(file_path)
        gif_directory = input('Insira o caminho para a pasta onde serão salvos os gifs: ')

        os.replace(current_dir + '\\' + gif_name, gif_directory + '\\' + gif_name) # Enviamos o gif para a pasta selecionada
        
        return frames[0]

    if __name__ == '__main__':
        # Caso estejamos rodando o código diretamente nessa classe, iremos utilizar o seguinte algoritmo
        url = input('Insira a url do vídeo que gostaria de converter em um .GIF: ')
        path = input('Insira o caminho para a pasta onde deseja guardar os vídeos: ')

        video = youtubeDownloader(url, path) # Atribuímos o vídeo à uma variável

        directory = frameCreator(video)

        gifCreator(directory) # Criamos o gif

