import requests
from colorama import Fore, Style
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
    
    vacancies = get_vacancies(AUTH_KEY=AUTH_KEY, FILTER_URL=FILTER_URL)
    
    if vacancies:
        for vacancy_id in vacancies:
            data = {'vacancy_id': vacancy_id, 'resume_id': RESUME_ID, 'message': MESSAGE, 'with_chat_info': True}
            print(f'Отправляем запрос: {data}')
            
            response = requests.post(POST_URL, data=data, headers=headers)
            try:
                if response.status_code == 201:
                    print(f'Отклик на вакансию: {vacancy_id}')
                else:
                    print(f'Не удалось откликнуться. Ошибка с кодом: {response.status_code}')
                    print(response.text)
            except Exception as e:
                print(f'ERROR: {e}')
    else:
        print('Нет доступных вакансий...')

RESUME_ID = input(Fore.GREEN + Style.BRIGHT + 'ID резюме: ')
MESSAGE = input(Fore.GREEN + Style.BRIGHT + 'Желаемая сообщение работадателям: ')
AUTH_KEY = input(Fore.GREEN + Style.BRIGHT + 'Введите токен авторизации: ')
FILTER_URL = input(Fore.GREEN + Style.BRIGHT + 'Введите URL фильтрации: ')

click_vacancies(AUTH_KEY=AUTH_KEY, RESUME_ID=RESUME_ID, MESSAGE=MESSAGE, FILTER_URL=FILTER_URL)