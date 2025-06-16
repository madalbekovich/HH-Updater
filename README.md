![image](https://github.com/user-attachments/assets/a7c64913-e4d8-4699-87e3-a1b219c9a5a0)s

1. Склонируйте проект
```
git clone https://github.com/madalbekovich/HH-Updater.git
```
```
cd HH-Updater
```
```
cd workflow
```
2. Установите зависимости
```
pip install -r requirements.txt
```
3. Настройте параметры
Перед запуском подготовьте следующие данные:

  ID резюме: его можно найти в вашем профиле hh.ru.  
  Токен авторизации: создайте токен в личном кабинете hh.ru.  
  Ключевые слова: например, "Python разработчик".  

  Запуск
Запустите скрипт с помощью команды:
```
python3 hh_update.py
```

Следуйте инструкциям на экране:

Введите ID вашего резюме.
Укажите текст сообщения работодателям.
Вставьте ваш токен авторизации.
Введите ключевые слова поиска вакансий.


## Как получить токен от hh?  

### Шаг 1: Установите NetCapture на Android  
1. Скачайте приложение [NetCapture](https://play.google.com/store/apps/details?id=com.minhui.networkcapture) из Google Play.  
2. Запустите приложение и начните захват сетевого трафика.  
3. Авторизуйтесь в своём профиле hh.ru через мобильное приложение или браузер на телефоне.  
4. Найдите запросы к `api.hh.ru` и извлеките ваш токен из заголовка `Authorization`.  

### Шаг 2: Для Linux/Windows/MacOS используйте HTTPToolkit  
1. Установите [HTTPToolkit](https://httptoolkit.com/) для вашей системы.  
2. Настройте перехват HTTPS-трафика, следуя официальной [инструкции](https://httptoolkit.com/docs/setup/).  
3. Войдите в hh.ru через браузер или приложение, используя HTTPToolkit для перехвата трафика.  
4. Найдите запросы, отправляемые на `api.hh.ru`, и скопируйте токен из заголовка `Authorization`.
5. ПРИМЕР ТОКЕНА: USERL8J7GSLGK20749L55C36T14PNLT2N5976JUGG7J2NFULDAfR10wUNM3D3HNL

Если у вас есть пожелания или замечания, напишите [сюда](tg: https://t.me/vedeikikb)!

