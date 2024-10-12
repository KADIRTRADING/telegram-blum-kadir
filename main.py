from utils.core import create_sessions, logger
from utils.telegram import Accounts
from utils.starter import start
import asyncio
from itertools import zip_longest
from utils.core import get_all_lines
import os
import argparse
from data import config


async def main():
    print("Tizim yaratuvchisi: https://t.me/kadirtrading\n")

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', type=int, help='Amalga oshirish uchun harakat')
    action = parser.parse_args().action

    if not os.path.exists('sessiyalar'):
        os.mkdir('sessiyalar')
    if not os.path.exists("ma'lumotlar"):
        os.mkdir("ma'lumotlar")

    if not action:
        action = int(input("Bittasini tanlang:\n1. ichki qismni boshlang\n2. Pyrogram sessiya yarating\n\n> "))

    if action == 2:
        await create_sessions()

    if action == 1:
        try:
            accounts = await Accounts().get_accounts()

            if config.PROXY is True:
                proxys = get_all_lines("data/proxy.txt")
            else:
                proxys = ""

            tasks = []
            for thread, (account, proxy) in enumerate(zip_longest(accounts, proxys)):
                if not account:
                    break
                tasks.append(asyncio.create_task(start(account=account, thread=thread, proxy=proxy)))

            await asyncio.gather(*tasks)
        except ValueError as error:
            logger.error("O'ylaymanki, hech qanday sessiyalar yo'q, iltimos, keyingi boshlash uchun ushbu CMD-ga 2 ni kiritib, bittasini qo'shing")
            logger.error('Agar sessiyalar haqiqiy deb hisoblasangiz, quyida xatolik bor, iltimos uni telegram chatimizga yuboring: https://t.me/kadir_trading')
            logger.error(error)

if __name__ == '__main__':
    print("""
    
    ####                  ####                                         ########        ##########                       #####      ###########
    ####              ####                                       ##########        ###########                     #####      #############
    ####           ####                                      #####      ####        #####      #####                 #####      ####              #####
    ####        ####                                     #####         ####        #####          #####             #####      ####                #####
    ####     ####                                    #####            ####        #####             #####          #####      ####                #####
    ####  ####                                   ###############        #####               #####        #####      ####               #####
    ########                                  ################       #####                  #####     #####      ##############
    ########                              #####                    ####       #####                 #####      #####      ##########
    ####   ####                         #####                     ####       #####               #####        #####      ####        ####
    ####      ####                    #####                      ####       #####             #####          #####      ####          ####
    ####        #####              #####                       ####      #####           #####            #####       ####            ####
    ####          #####          #####                        ####      ##############             #####       ####               ####
    ####            #####      #####                         ####      ############                  #####       ####                  ####
                                                         
                   Yaratuvchi: Muhammadqodir Abdusalomov                                          
          
          """)
    asyncio.run(main())
