#!/usr/bin/env python3

import os
import subprocess
import configparser

CONFIG_PATH = '/etc/lmp/lmp.conf'
MEDIA_PATH = '$HOME/media'
MEDIA_PLAYER = 'mpv'
HOME_SYMBOL = '##'
CHAR_CUTOFF = 10
START_MESSAGE = 'Select a file or directory to play'

def get_config():
    global MEDIA_PATH
    global MEDIA_PLAYER
    global HOME_SYMBOL
    global CHAR_CUTOFF
    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_PATH)
    except:
        print('Could not read config file')
    try:
        MEDIA_PATH = config.get('general', 'media_path')
        MEDIA_PLAYER = config.get('general', 'media_player')
        HOME_SYMBOL = config.get('general', 'home_symbol')
        CHAR_CUTOFF = int(config.get('general', 'char_cutoff'))
    except:
        print('Could not get one or more options')
    MEDIA_PATH = os.path.expandvars(MEDIA_PATH)

# Recursive cli selection
def select_media(path, message=START_MESSAGE):
    subprocess.run(['tput', 'reset'])
    previous_path = '/'.join(path.split('/')[:-1])
    if message:
        print(message)
    if os.path.isfile(path):
        print('\033[94m' + 'Playing media...' + '\033[0m')
        media = subprocess.Popen([MEDIA_PLAYER, path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        path = previous_path
        previous_path = '/'.join(path.split('/')[:-1])
        subprocess.run(['tput', 'reset'])
        print(START_MESSAGE)
    list_dir = os.listdir(path)
    list_dir.sort()
    for i, file in enumerate(list_dir):
        print('\033[92m' + f'{i+1}' + '.' + '\033[0m' + f'\t{file}')
    if path != MEDIA_PATH:
        print('\033[92m' + '0.' + '\033[0m' + '\tGo back')
    else:
        print('\033[92m' + '0.' + '\033[0m' +'\tExit')
    
    path_array = path.replace(MEDIA_PATH, HOME_SYMBOL).split('/')
    display_path = []
    for i, dir in enumerate(path_array):
        if not(i == len(path_array)-1) and len(dir) > CHAR_CUTOFF:
            dir = dir[:CHAR_CUTOFF] + '...'
        display_path.append(dir)
    display_path = '/'.join(display_path)

    choice = input(f'\033[95m[{display_path}] > \033[0m')
    try:
        choice = int(choice)
    except ValueError:
        if(choice == 'q'):
            return
        select_media(path, '\033[91m' + 'Invalid input, try again' + '\033[0m')
        return
    except KeyboardInterrupt:
        return
    if choice == 0 and path != MEDIA_PATH:
        select_media(previous_path)
    elif choice == 0:
        return
    elif len(list_dir)+1 > choice:
        select_media(f'{path}/{list_dir[choice-1]}')
    else:
        select_media(path, '\033[91m' + 'Invalid selection, try again' + '\033[0m')

def main():
    global MEDIA_PATH
    get_config()
    select_media(MEDIA_PATH)

if __name__ == '__main__':
    main()
