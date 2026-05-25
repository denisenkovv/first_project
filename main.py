import os 
from dotenv import load_dotenv

#Загрузка переменных из файла .env
load_dotenv()

#Читаем переменную AUTHOR
author = os.getenv('PASSWORD')

print(f"Имя автора: {author}")