from tkinter import *
from tkinter.filedialog import askopenfilename
from moviepy.editor import *

# Cria a janela de interface gráfica
janela = Tk()

# Define o título da janela
janela.title("Conversor de vídeo para áudio")

# Define o tamanho mínimo da janela
janela.minsize(width=400, height=100)

# Função para selecionar o arquivo de vídeo
def selecionar_arquivo():
    arquivo = askopenfilename()
    video = VideoFileClip(arquivo)
    audio = video.audio
    audio.write_audiofile("output.mp3")

# Botão para selecionar o arquivo de vídeo
selecionar_arquivo_btn = Button(janela, text="Selecionar arquivo", command=selecionar_arquivo)
selecionar_arquivo_btn.pack(pady=10)

# Roda a janela
janela.mainloop()

