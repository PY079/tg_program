import webbrowser, os
from os import environ, getcwd

getUser = lambda: environ['USERNAME']
user = getUser()

os.system('cls')
y = input('\n\n    Ввести запрос --> y/n ')
os.system('cls')
webbrowser.register('Yandex', None, webbrowser.BackgroundBrowser('C:/Users/'+user+'/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'))
if y == 'y':
    call = input('\n\n  Введите запрос --> ')
    webbrowser.get('Yandex').open_new_tab('https://yandex.ru/search/?text='+call)
    os.system('cls')


if y == 'n':
    webbrowser.open_new_tab('https://yandex.ru/efir?%3Futm_source=bno&stream_active=category&stream_category=film')