import requests
import timeit
import subprocess
import smtplib, ssl
from logins import *

start = timeit.default_timer()

s = requests.session()

base_headers = {
  'authority': 'www.toasttab.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'x-requested-with': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.toasttab.com/advancedproperties/bulkeditor',
  'accept-language': 'en-US,en;q=0.9'
}

stock = open('stock.txt', 'w')
stock.truncate()

def login():
    
    url = "http://www.toasttab.com/login"

    headers = {
      'Connection': 'keep-alive',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Language': 'en-US,en;q=0.9'
    }

    response = s.request("GET", url, headers=headers, data={})

    url = "https://www.toasttab.com/login"

    headers = {
    'authority': 'www.toasttab.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'accept-language': 'en-US,en;q=0.9'
    }

    response = s.request("GET", url, headers=headers, data={})

    state = response.url.split("state=")[1]

    url = "https://auth.toasttab.com/authorize?force_mfa=false&client_id=" + client_id + "&redirect_uri=https://www.toasttab.com/authentication/callback&response_type=code&scope=openid%20profile&audience=https://toast-users-api/&state=" + state

    headers = {
      'Connection': 'keep-alive',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Sec-Fetch-Site': 'none',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-User': '?1',
      'Sec-Fetch-Dest': 'document',
      'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
      'sec-ch-ua-mobile': '?0',
      'Accept-Language': 'en-US,en;q=0.9'
    }

    response = s.request("GET", url, headers=headers, data={})

    url = "https://auth.toasttab.com/u/login?state=" + state

    headers = {
          'Connection': 'keep-alive',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'Sec-Fetch-Site': 'none',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-User': '?1',
          'Sec-Fetch-Dest': 'document',
          'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
          'sec-ch-ua-mobile': '?0',
          'Accept-Language': 'en-US,en;q=0.9'
    }

    response = s.request("GET", url, headers=headers, data={})

    url = "https://auth.toasttab.com/u/login?state=" + state

    payload='state=' + state + '&username=' + username + '&password=' + password + '&action=default'
    headers = {
      'Connection': 'keep-alive',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
      'sec-ch-ua-mobile': '?0',
      'Upgrade-Insecure-Requests': '1',
      'Origin': 'https://auth.toasttab.com',
      'Content-Type': 'application/x-www-form-urlencoded',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-User': '?1',
      'Sec-Fetch-Dest': 'document',
      'Referer': 'https://auth.toasttab.com/u/login?state=g6Fo2SBzaVdtdjRvYk4wc2ktWlo0OGh2U3Fya196X2FQS2IzSKN0aWTZIHkzOVV6ZHJ2TXJNN0w3Y1hGMkVPQW9Ob2xXa3RhMVl5o2NpZNkgcFZJdGJCWldrcHd1OEg5RGRtMG9QY1NmYWd4cmtydEI',
      'Accept-Language': 'en-US,en;q=0.9'
    }

    response = s.request("POST", url, headers=headers, data=payload)


def small_whole_pies():

    stock.write("SMALLS:")

    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232292334&parentId=100000005232292030&archiveMode=true"

    response = s.request("GET", url, headers=base_headers, data={})

    json_response  = response.json()

    for pizza in json_response["children"][1:]:
        if pizza.get('inventory'):
            stock.write("\n" + pizza['name'])


def small_whole_toppings():
                        
    small_whole_ids_doc = open("small_whole_ids.txt", "r")
    small_whole_ids = small_whole_ids_doc.readlines()
    small_whole_ids_doc.close()

    for x in range(len(small_whole_ids)):
        if(small_whole_ids[x].lstrip()):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + small_whole_ids[x].lstrip().rstrip() + "&parentId=100000005232292405&archiveMode=true"
                        
            response = s.request("GET", url, headers=base_headers, data={})

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])

def small_left_toppings():
                
    small_left_ids_doc = open("small_left_ids.txt", "r")
    small_left_ids = small_left_ids_doc.readlines()
    small_left_ids_doc.close()

    for x in range(len(small_left_ids)):
        if(small_left_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + small_left_ids[x].lstrip().rstrip() + "&parentId=100000005232292695&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={}, timeout=5)

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])

def small_right_toppings():
                
    small_right_ids_doc = open("small_right_ids.txt", "r")
    small_right_ids = small_right_ids_doc.readlines()
    small_right_ids_doc.close()

    for x in range(len(small_right_ids)):
        if(small_right_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + small_right_ids[x].lstrip().rstrip() + "&parentId=100000005232293195&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={}, timeout=5)

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])

def medium_whole_pies():

    stock.write("\n" + "MEDIUMS:")

    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232297878&parentId=100000005232292030&archiveMode=true"

    response = s.request("GET", url, headers=base_headers, data={})

    json_response  = response.json()

    for pizza in json_response["children"][1:]:
        if pizza.get('inventory'):
            stock.write("\n" + pizza['name'])  

def medium_whole_toppings():

    medium_whole_ids_doc = open("medium_whole_ids.txt", "r")
    medium_whole_ids = medium_whole_ids_doc.readlines()
    medium_whole_ids_doc.close()

    for x in range(len(medium_whole_ids)):
        if(medium_whole_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + medium_whole_ids[x].lstrip().rstrip() + "&parentId=100000005232297895&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={})

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])
                        
def medium_left_toppings():
                
    medium_left_ids_doc = open("medium_left_ids.txt", "r")
    medium_left_ids = medium_left_ids_doc.readlines()
    medium_left_ids_doc.close()

    for x in range(len(medium_left_ids)):
        if(medium_left_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + medium_left_ids[x].lstrip().rstrip() + "&parentId=100000005232298501&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={}, timeout=5)

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])

def medium_right_toppings():
                
    medium_right_ids_doc = open("medium_right_ids.txt", "r")
    medium_right_ids = medium_right_ids_doc.readlines()
    medium_right_ids_doc.close()

    medium_right_parent_id = "100000005232298835"

    for x in range(len(medium_right_ids)):
        if(medium_right_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + medium_right_ids[x].lstrip().rstrip() + "&parentId=100000005232298835&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={}, timeout=5)

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])

def large_whole_pies():

    stock.write("\n" + "LARGES:")

    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232302668&parentId=100000005232292030&archiveMode=true"

    response = s.request("GET", url, headers=base_headers, data={})

    json_response  = response.json()

    for pizza in json_response["children"][1:]:
        if pizza.get('inventory'):
            stock.write("\n" + pizza['name'])


def large_whole_toppings():

    large_whole_ids_doc = open("large_whole_ids.txt", "r")
    large_whole_ids = large_whole_ids_doc.readlines()
    large_whole_ids_doc.close()

    for x in range(len(large_whole_ids)):
        if(large_whole_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + large_whole_ids[x].lstrip().rstrip() + "&parentId=100000005232302672&archiveMode=true"
                                
            response = s.request("GET", url, headers=base_headers, data={})

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])

def large_left_toppings():
                
    large_left_ids_doc = open("large_left_ids.txt", "r")
    large_left_ids = large_left_ids_doc.readlines()
    large_left_ids_doc.close()

    for x in range(len(large_left_ids)):
        if(large_left_ids[x].lstrip() != ""):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + large_left_ids[x].lstrip().rstrip() + "&parentId=100000005232303347&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={}, timeout=5)

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])


def large_right_toppings():
                
    large_right_ids_doc = open("large_right_ids.txt", "r")
    large_right_ids = large_right_ids_doc.readlines()
    large_right_ids_doc.close()

    for x in range(len(large_right_ids)):
        if(large_right_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + large_right_ids[x].lstrip().rstrip() + "&parentId=100000005232303746&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={}, timeout=5)

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])
                
def left_half():

    stock.write("\n" + "HALF SPECIALTIES:")

    left_half_doc = open("left_half_ids.txt", "r")
    left_half_ids = left_half_doc.readlines()
    left_half_doc.close()

    for x in range(len(left_half_ids)):
        if(left_half_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + left_half_ids[x].lstrip().rstrip() + "&parentId=100000007232953180&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={})
            
            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])

def right_half():

    right_half_doc = open("right_half_ids.txt", "r")
    right_half_ids = right_half_doc.readlines()
    right_half_doc.close()

    for x in range(len(right_half_ids)):
        if(right_half_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + right_half_ids[x].lstrip().rstrip() + "&parentId=100000007233285110&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={})
            
            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])


def calzone_whole():

    stock.write("\n" + "CALZONES:")

    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232307736&parentId=100000005232292030&archiveMode=true"

    response = s.request("GET", url, headers=base_headers, data={})

    json_response  = response.json()

    for pizza in json_response["children"][1:]:
        if pizza.get('inventory'):
            stock.write("\n" + pizza['name'])

def calzone_toppings():

    calzone_toppings_ids_doc = open("calzone_toppings_ids.txt", "r")
    calzone_toppings_ids = calzone_toppings_ids_doc.readlines()
    calzone_toppings_ids_doc.close()

    for x in range(len(calzone_toppings_ids)):
        if(calzone_toppings_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + calzone_toppings_ids[x].lstrip().rstrip() + "&parentId=100000005232307740&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={})
            
            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])

def salad_whole():

    stock.write("\n" + "SALADS:")

    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232308750&parentId=100000005232292030&archiveMode=true"

    response = s.request("GET", url, headers=base_headers, data={})

    json_response  = response.json()

    for pizza in json_response["children"][1:]:
        if 'inventory' in pizza and pizza['inventory'] == '0':
            stock.write("\n" + pizza['name'])

def dressings():

    dressings_ids_doc = open("dressings_ids.txt", "r")
    dressings_ids = dressings_ids_doc.readlines()
    dressings_ids_doc.close()

    for x in range(len(dressings_ids)):
        if(dressings_ids[x].lstrip() != "" ):
            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + dressings_ids[x].lstrip().rstrip() + "&parentId=100000005232308771&archiveMode=true"

            response = s.request("GET", url, headers=base_headers, data={})

            json_response  = response.json()

            if json_response["children"][0]["inventory"] == "0":
                stock.write("\n" + json_response["children"][0]["name"])


    stock.close()

def email():
    stock = open("stock.txt", "r")
    contents = stock.read()
    stock.close()

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email_address = sender_email  # Enter your address
    receiver_email_address = receiver_email  # Enter receiver address
    password = password
    message = contents

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



def main():
    
    login()
    
    small_whole_pies()
    small_whole_toppings()
    small_left_toppings()
    small_right_toppings()

    medium_whole_pies()
    medium_whole_toppings()
    medium_left_toppings()
    medium_right_toppings

    large_whole_pies()
    large_whole_toppings()
    large_left_toppings
    large_right_toppings()

    left_half()
    right_half()

    calzone_whole()
    calzone_toppings()

    salad_whole()
    dressings()


if __name__ == '__main__':
    main()
