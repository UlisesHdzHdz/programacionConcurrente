"""
   Crear 3 subprocesos dentro de un proceso:
*. Registrar 5000 datos en la base de datos
*. Iterar un servicio 50 veces
*. Descargar 5 videos
"""
import requests
import threading
import psycopg2
import time
import pytube

try:
    conexion = psycopg2.connect(database='DBDATOS', user='postgres', password='root')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
except Exception as err:
    print('Error al conecta a la base de datos')
# subprocesos 1
def thread1(task1):
    get_service(task1[0])

def get_service(url):
    init_time = time.time()
    r = requests.get(url)
    photos = r.json()
    for photo in photos:
        write_db(photo["title"])
    end_time = time.time() - init_time
    print(f"Hilo 1 terminado en {end_time} ms")

def write_db(title):
    try:
        cursor1.execute("insert into photos (title) values ('"+title+"')")
        
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()
# subprocesos 2
def thread2(task2):
    init_time = time.time()
    for _ in range(0,50):
        thread2_2 = threading.Thread(target=get_service2, args=[task2])
        thread2_2.start()
    end_time = time.time() - init_time
    print(f"Hilo 2 terminado en {end_time} ms")

def get_service2(task2):
    response = requests.get(task2[0])
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
# subprocesos 3
def thread3(urls,path):
    init_time = time.time()
    for url in urls:
        thread3_2 = threading.Thread(target=get_service3, args=[url,path])
        thread3_2.start()
    end_time = time.time() - init_time
    print(f"Hilo 3 terminado en {end_time} ms")

def get_service3(url,path):
    print(f"Descargando video: {url}")
    try:
        pytube.YouTube(url).streams.first().download(path)
        titleyt = pytube.YouTube(url).title
        print(f"Video descargado: {titleyt}\nURL: {url}\n")
    except Exception as err:
        print('Error en la descarga: ', err)

if __name__ == "__main__":
    user = "Ulises"
    task1 = ["https://jsonplaceholder.typicode.com/photos"]
    task2 = ["https://randomuser.me/api"]
    urls_videos =[
            'https://www.youtube.com/watch?v=sQY6Umchw2M',
            'https://www.youtube.com/watch?v=Sog5AgxPwu0',
            'https://www.youtube.com/watch?v=25GG9LAUHsA',
            'https://www.youtube.com/watch?v=PF1XE7yEmgY',
            'https://www.youtube.com/watch?v=yNXfOOL8824']
    path = "C:/Users/Ulises/Desktop/ProgramacionConcurrente191244"
    
    thread1 = threading.Thread(target=thread1, args=[task1])
    thread2 = threading.Thread(target=thread2, args=[task2])
    thread3 = threading.Thread(target=thread3, args=[urls_videos, path])
    thread1.start()
    thread2.start()
    thread3.start()