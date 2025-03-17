FROM python:3.8-slim

# Instala dependências do sistema (ffmpeg para manipulação de vídeo e bibliotecas para OpenCV)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
 && rm -rf /var/lib/apt/lists/*

# Instala o PyTorch (versão CPU) e torchvision
RUN pip install --no-cache-dir torch==1.8.0+cpu torchvision==0.9.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Instala outras dependências do Python
RUN pip install --no-cache-dir streamlit opencv-python-headless pillow

# Instala o Detectron2 (versão CPU)
RUN pip install --no-cache-dir detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.8/index.html

# Define o diretório de trabalho
WORKDIR /app

# Copia o código da aplicação para dentro do container
COPY . /app

# Comando para iniciar a aplicação com Streamlit
CMD ["streamlit", "run", "app.py"]
