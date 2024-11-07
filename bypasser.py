import requests, pystyle, os
from pystyle import *
from os import system
system("cls && title LYNO AD BYPASSER Powered by bypass.vip")
banner = """
█    ▀▄    ▄  ▄   ████▄     █ ▄▄  █▄▄▄▄ ████▄ ██▄     ▄   ▄█▄      ▄▄▄▄▀ ▄█ ████▄    ▄   
█      █  █    █  █   █     █   █ █  ▄▀ █   █ █  █     █  █▀ ▀▄ ▀▀▀ █    ██ █   █     █  
█       ▀█ ██   █ █   █     █▀▀▀  █▀▀▌  █   █ █   █ █   █ █   ▀     █    ██ █   █ ██   █ 
███▄    █  █ █  █ ▀████     █     █  █  ▀████ █  █  █   █ █▄  ▄▀   █     ▐█ ▀████ █ █  █ 
    ▀ ▄▀   █  █ █            █      █         ███▀  █▄ ▄█ ▀███▀   ▀       ▐       █  █ █ 
           █   ██             ▀    ▀                 ▀▀▀                          █   ██ 
                         BY lasnuh, Ad bypass powered by bypass.vip                                                                
"""
Write.Print(banner, Colors.blue_to_green, interval=0.0000)
link = Write.Input("\n [LYNO]: Please enter the URL you want to bypass: ",Colors.blue_to_green,interval=0.0000)
##########################BYPASS MOMENTS##########################
try:
    url = f"https://api.bypass.vip/bypass?url={link}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload) 
    bypassed_link = response.json().get("result")
    status = response.json().get("status")
    Write.Print(f"\n[LYNO]: STATUS : {status}\tBypassed Link: {bypassed_link}",Colors.blue_to_green,interval=0.1)
    Write.Print(f"\n[LYNO]: Press enter to exit", Colors.blue_to_green, interval=0.0000)
    input()
    quit()
except requests.exceptions.RequestException as e:
    Write.Print(f"\n[LYNO]: An error occurred: {e}",Colors.blue_to_green,interval=0.0000)
