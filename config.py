from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST', 'localhost')  # ou o IP correto, se necessário
DB_NAME = os.getenv('DB_NAME', 'tarefas')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # Se você tiver uma chave secreta definida no .env
