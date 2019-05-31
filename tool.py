#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
import nmap 
#This banner will display every time when the user execute this python script. this banner will help the user to select his/her desire tool.

def logo():
    print('''

    {1} Whois lookup
    {2} Traceroute
    {3} DNS Lookup
    {4} Reverse DNS Lookup
    {5} GeoIP Lookup
    {6} online Port Scan
    {7} local port Scan 
    {8} HTTP Header Check
    {9} URL Extractor
    {10} Exit
''')

logo()

def check_status():
    print("\t [#] Checking the availability of API server...")
    request = requests.get("https://hackertarget.com")
    http = request.status_code
    if http == 200:
        print("\t [#] API Server is Online")
    else:
        print("\t [!] Oops Error occured, Server offline,Ensure your connected to the internet and try again ")
        exit()


def quit():
    alpha = input("Are You Sure?[yes/no] - ").lower()
    if alpha == "yes":
        exit()
    if alpha == "no":
        logo()
        choice()


def choice():
    try:
        selection = input("Tool:- ")
        if selection == '1':
            dig = str(input("Do You Wish to Dig Your Own Information[yes/no] - ").lower())
            if dig == "yes":
                check_status()
                result = requests.get("https://api.hackertarget.com/whois/?q=" +
                                      my_ip).content.decode("UTF-8")
                print(result)
                exit()
            if dig == "no":
                new = input("Enter IP or Domain for lookup:- ")
                check_status()
                result2 = requests.get(
                    "https://api.hackertarget.com/whois/?q=" + new).content.decode("UTF-8")
                print(result2)
                exit()
            else:
                digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
                if digg == "yes":
                    quit()
                if digg == "no":
                    logo()
                    choice()
                else:
                    exit()

        elif selection == '2':
            dig = str(input("Do You Wish to Dig Your Own Information[yes/no] - ").lower())
            if dig == "yes":
                check_status()
                result = requests.get("https://api.hackertarget.com/mtr/?q=" +
                                      my_ip).content.decode("UTF-8")
                print(result)
                exit()
            if dig == "no":
                new = input("Enter IP or Domain for lookup:- ")
                check_status()
                result2 = requests.get("https://api.hackertarget.com/mtr/?q=" + new)
                print(result2)
                exit()
            else:
                digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
            if digg == "yes":
                quit()
            if digg == "no":
                logo()
                choice()
            else:
                exit()

        elif selection == '3':
            dig = str(input("Enter Domain - "))
            check_status()
            result = requests.get(
                "https://api.hackertarget.com/dnslookup/?q=" + dig).content.decode("UTF-8")
            print(result)
            exit()

        elif selection == '4':
            dig = str(input("IP Address / IP Range / Domain Name - "))
            check_status()
            result = requests.get(
                "https://api.hackertarget.com/reversedns/?q=" + dig).content.decode("UTF-8")
            print(result)
            exit()

        elif selection == '5':
            dig = str(input("Do You Wish to Dig Your Own Information[yes/no] - ").lower())
            if dig == "yes":
                check_status()
                result = requests.get("https://api.hackertarget.com/geoip/?q=" +
                                      my_ip).content.decode("UTF-8")
                print(result)
                exit()
            if dig == "no":
                new = input("Enter ip address:- ")
                check_status()
                result2 = requests.get(
                    "https://api.hackertarget.com/geoip/?q=" + new).content.decode("UTF-8")
                print(result2)
                exit()
            else:
                digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
                if digg == "yes":
                    quit()
                if digg == "no":
                    logo()
                    choice()
                else:
                    exit()

        elif selection == '6':
            dig = str(input("Do You Wish to Dig Your Own Information[yes/no] - ").lower())
            if dig == "yes":
                check_status()
                result = requests.get("https://api.hackertarget.com/nmap/?q=" +
                                      my_ip).content.decode("UTF-8")
                print(result)
                exit()
            if dig == "no":
                new = input("Enter ip address:- ")
                check_status()
                result2 = requests.get(
                    "https://api.hackertarget.com/nmap/?q=" + new).content.decode("UTF-8")
                print(result2)
                exit()
            else:
                digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
                if digg == "yes":
                    quit()
                if digg == "no":
                    logo()
                    choice()
                else:
                    exit()

        elif selection == '8':
            dig = str(input("Enter web address:- "))
            check_status()
            result = requests.get(
                "https://api.hackertarget.com/httpheaders/?q=" + dig).content.decode("UTF-8")
            print(result)
            exit()

        elif selection == '9':
            website = str(input("Enter web address:-"))
            website = website.replace("http://", "")
            website = website.replace("https://", "")
            website = ("https://" + website)
            check_status()
            result = requests.get("https://api.hackertarget.com/pagelinks/?q=" +
                                  website).content.decode("UTF-8")
            print(result)
            exit()

        elif selection == '10':
            quit()

        else:
            digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
            if digg == "yes":
                quit()
            if digg == "no":
                logo()
                choice()
            else:
                exit()

    except(KeyboardInterrupt):
        print("Programme Interrupted")
    except requests.exceptions.ConnectionError:
        print('Your Internet is Offline')
        exit


choice()

'''
- References -
https://hackertarget.com/ip-tools/
'''
