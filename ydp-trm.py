###################################
## YTMSDL VERSION 3 - FOR TERMUX ##
## Now with Python and colors!   ##
## Creator : datbadwolf97        ##
###################################
from yt_dlp import YoutubeDL
from colorama import Fore, Back
import os

while True:
    ydl_mp3 = {
        'outtmpl': '%(title)s.%(ext)s',
        'paths' : {
            'home' : '~/Music',
        },
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    ydl_m4a = {
        'outtmpl': '%(title)s.%(ext)s',
        'paths' : {
            'home' : '~/Music',
        },
        'format': 'm4a/bestaudio/best',
    }

    ydl_wav = {
        'outtmpl' : '%(title)s.%(ext)s',
        'paths' : {
            'home' : '~/Music',
        },
        'format' : 'm4a/bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'prefferedcodec' : 'wav',
        }]
    }
    print(Fore.RED + Back.BLACK + 'Youtube Music Downloader III' + Fore.RESET + Back.RESET)
    print(Fore.BLUE + 'Select a format below.' + Fore.RESET)
    print(Fore.RESET + '1. MP3. \n2. M4A.\n3. WAV.\n4. Exit.')
    inp1 = input(Fore.CYAN + 'Choose an option. : ' + Fore.RESET)
    if inp1 == '1':
        inp2 = input(Fore.RESET + 'Enter the link : ')
        print(Fore.CYAN + 'Downloading MP3.' + Fore.RESET)
        with YoutubeDL(ydl_mp3) as ydl:
                error_code = ydl.download(inp2)
        print('Done.')
        os.system('sleep 1 && clear')
        exit()
    elif inp1 == '2':
        inp3 = input(Fore.RESET + 'Enter the link : ')
        print(Fore.GREEN + 'Downloading M4A.' + Fore.RESET)
        with YoutubeDL(ydl_m4a) as ydl:
            error_code = ydl.download(inp3)
        print('Done.')
        os.system('sleep 1 && clear')
        exit()
    elif inp1 == '3':
        inp4 = input(Fore.RESET + 'Enter the link : ')
        print(Fore.RED + 'Downloading WAV.' + Fore.RESET)
        with YoutubeDL(ydl_wav) as ydl:
            error_code = ydl.download(inp4)
        os.system('sleep 1 && clear')
        exit()
    elif inp1 == '4':
        print(Fore.RESET + 'Exiting...')
        os.system('sleep 1 && clear')
        exit()
    else:
        print(Fore.LIGHTRED_EX + 'Unrecognized option.' + Fore.RESET)
        os.system('sleep 1 && clear')
## Well, that's it for now...
