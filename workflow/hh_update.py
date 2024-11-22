import requests
from colorama import Fore, Style
import os
import math
import time 
ascii_art = f"""       

                   {Fore.RED}ooooo   ooooo ooooo   ooooo                                   .o8                .                      
                   `888'   `888' `888'   `888'                                  "888              .o8                      
                    888     888   888     888       oooo  oooo  oo.ooooo.   .oooo888   .oooo.   .o888oo  .ooooo.  oooo d8b 
                    888ooooo888   888ooooo888       `888  `888   888' `88b d88' `888  `P  )88b    888   d88' `88b `888""8P 
                    888     888   888     888       {Fore.GREEN + Style.BRIGHT} 888   888   888   888 888   888   .oP"888    888   888ooo888  888     
                    888     888   888     888        888   888   888   888 888   888  d8(  888    888 . 888    .o  888     
                   o888o   o888o o888o   o888o       `V88V"V8P'  888bod8P' `Y8bod88P" `Y888""8o   "888" `Y8bod8P' d888b    
                                                                  888                                                       
                                                                 o888o                     
                                             
                                             
                                             
                                             
                                                        {Fore.BLUE + Style.BRIGHT}Developed by madalbekovich   
                                                        {Fore.MAGENTA + Style.DIM}
                                           
                                        
                                                            ...............      
                                                            ...:::::::::::::...    
                                                        ...::::::::.::::::::...  
                                                        ..:-::::::.....::::::-:...
                                                        .:=-----.... ....:----=:..
                                                        .=+==-:............-====..
                                                        .:+++-....-=...-=....-+++:.
                                                        .:++++-:=++=...-++=::=+++:.
                                                        .+++++++++=...-+++++++++..
                                                        .:++++++**+...-*+++++++:..
                                                        ..:+******+...=******+:...
                                                        ...-+******=+*****+-...  
                                                            ...:=++******+=:...    
                                                            ...............      

                                                                                                          
"""

for char in ascii_art:
    print(char, end='', flush=True)
    time.sleep(0.0010)
    
def load_responded_vacancies(file_path='vacancies_responded.txt'):
    """Загружает список откликанных вакансий из файллф"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            return set(data.strip().split(',')) if data else set()
    return set()

def save_responded_vacancy(vacancy_id, file_path='vacancies_responded.txt'):
    """Добавляет вакансию в список откликанных и сохраняет в файл."""
    with open(file_path, 'a') as file:
        file.write(f'{vacancy_id} - ')


def get_vacancies(AUTH_KEY, FILTER_URL):
    headers = {'Authorization': f'Bearer {AUTH_KEY}'}
    
    response = requests.get(FILTER_URL, headers=headers)
    try:
        if response.status_code == 200:
            print('success request!')
            data = response.json()
            data_list = data.get('items', [])
            vacancies = [resume.get('id') for resume in data_list]
            return vacancies
        else:
            print(f'bad request: {response.status_code}')
    except Exception as e:
        print(f'error with: {e}')
        return []

def click_vacancies(AUTH_KEY, RESUME_ID, MESSAGE=None, FILTER_URL=None):
    POST_URL = 'https://api.hh.ru/negotiations?hhtmSource=vacancy_response&hhtmFrom=main&host=headhunter.kg&locale=RU'
    headers = {'Authorization': f'Bearer {AUTH_KEY}'}
    
    vacancies = get_vacancies(AUTH_KEY=AUTH_KEY, FILTER_URL=DEFAULT_URL)
    responded_vacancies = load_responded_vacancies()
    
    if vacancies:
        for vacancy_id in vacancies:
            if vacancy_id in responded_vacancies:
                print(Fore.RED + f'Пропускаем вакансию {vacancy_id},которую вы уже откликались.')
                continue
            data = {'vacancy_id': vacancy_id, 'resume_id': RESUME_ID, 'message': MESSAGE, 'with_chat_info': True}
            # print(f'Отправляем запрос: {data}')
            
            response = requests.post(POST_URL, data=data, headers=headers)
            try:
                if response.status_code == 201:
                    print(f'Отклик на вакансию: {vacancy_id}')
                    save_responded_vacancy(vacancy_id)
                else:
                    responses_status = response.json()
                    if (responses_status.get('description')) == 'Daily negotiations limit is exceeded':
                        print(Fore.RED + f'Превышен суточный лимит откликов,\n{Fore.YELLOW + Style.BRIGHT}Попробуйте указать другое резюме ㋡')
                        break
                    print(f'Не удалось откликнуться. Ошибка с кодом: {response.status_code}')
            except Exception as e:
                print(f'ERROR: {e}')
    else:
        print('Нет доступных вакансий...')

RESUME_ID = input(Fore.GREEN + Style.BRIGHT + 'ID резюме: ')
MESSAGE = input(Fore.GREEN + Style.BRIGHT + 'Желаемая сообщение работадателям: ')
AUTH_KEY = input(Fore.GREEN + Style.BRIGHT + 'Введите токен авторизации: ')
KEY_STACK = input(Fore.GREEN + Style.BRIGHT + 'Введите ключёвые слова(например: Python разработчик): ')

#TO:DO
# PAGE_COUNT = int(input(Fore.GREEN + Style.BRIGHT + 'Введите кол-во откликов: '))
# round_page = PAGE_COUNT / 100
# per_page = math.ceil(round_page)
# for page in range(per_page):

DEFAULT_URL = f'https://api.hh.ru/vacancies?host=headhunter.kg&page=2&per_page=100&text={KEY_STACK}'
click_vacancies(AUTH_KEY=AUTH_KEY, RESUME_ID=RESUME_ID, MESSAGE=MESSAGE, FILTER_URL=DEFAULT_URL)