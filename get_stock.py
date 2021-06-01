import requests
import pickle
import time
import subprocess
import smtplib, ssl


start_time = time.time()


def main():

    session = requests.session()  # or an existing session

    with open('cookies.txt', 'rb') as f:
        session.cookies.update(pickle.load(f))

    stock = open('stock.txt', 'w')
    stock.truncate()

    def smalls():

        def small_whole_pies():

            stock.write("SMALLS:")

            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232292334&parentId=100000005232292030&archiveMode=true"

            payload={}
            headers = {
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
              'accept-language': 'en-US,en;q=0.9'    }

            response = session.request("GET", url, headers=headers, data=payload)

            json_response  = response.json()

            for pizza in json_response["children"][1:]:
                if 'inventory' in pizza and pizza['inventory'] is not None:
                    stock.write("\n" + pizza['name'])            

        small_whole_pies()

        def small_whole_toppings():
                        
            small_whole_ids_doc = open("small_whole_ids.txt", "r")
            small_whole_ids = small_whole_ids_doc.readlines()

            small_whole_parent_id = "100000005232292405"

            for x in range(len(small_whole_ids)):
                if(small_whole_ids[x].lstrip()):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + small_whole_ids[x].lstrip().rstrip() + "&parentId=" + small_whole_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
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
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        small_whole_toppings()

        def small_left_toppings():
                        
            small_left_ids_doc = open("small_left_ids.txt", "r")
            small_left_ids = small_left_ids_doc.readlines()

            small_left_parent_id = "100000005232292695"

            for x in range(len(small_left_ids)):
                if(small_left_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + small_left_ids[x].lstrip().rstrip() + "&parentId=" + small_left_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
                      'authority': 'www.toasttab.com',
                      'pragma': 'no-cache',
                      'cache-control': 'no-cache',
                      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                      'accept': 'application/json, text/javascript, */*; q=0.01',
                      'x-requested-with': 'XMLHttpRequest',
                      'sec-ch-ua-mobile': '?0',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                      'sec-fetch-site': 'same-origin',
                      'sec-fetch-mode': 'cors',
                      'sec-fetch-dest': 'empty',
                      'referer': 'https://www.toasttab.com/advancedproperties/bulkeditor',
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload, timeout=5)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        small_left_toppings()

        def small_right_toppings():
                        
            small_right_ids_doc = open("small_right_ids.txt", "r")
            small_right_ids = small_right_ids_doc.readlines()

            small_right_parent_id = "100000005232293195"

            for x in range(len(small_right_ids)):
                if(small_right_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + small_right_ids[x].lstrip().rstrip() + "&parentId=" + small_right_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
                      'authority': 'www.toasttab.com',
                      'pragma': 'no-cache',
                      'cache-control': 'no-cache',
                      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                      'accept': 'application/json, text/javascript, */*; q=0.01',
                      'x-requested-with': 'XMLHttpRequest',
                      'sec-ch-ua-mobile': '?0',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                      'sec-fetch-site': 'same-origin',
                      'sec-fetch-mode': 'cors',
                      'sec-fetch-dest': 'empty',
                      'referer': 'https://www.toasttab.com/advancedproperties/bulkeditor',
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload, timeout=5)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        small_right_toppings()
        
    smalls()

    def mediums():

        def medium_whole_pies():

            stock.write("\n" + "MEDIUMS:")

            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232297878&parentId=100000005232292030&archiveMode=true"
    
            payload={}
            headers = {
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
              'accept-language': 'en-US,en;q=0.9'    }

            response = session.request("GET", url, headers=headers, data=payload)

            json_response  = response.json()

            for pizza in json_response["children"][1:]:
                if 'inventory' in pizza and pizza['inventory'] is not None:
                    stock.write("\n" + pizza['name'])            

        medium_whole_pies()

        def medium_whole_toppings():

            medium_whole_ids_doc = open("medium_whole_ids.txt", "r")
            medium_whole_ids = medium_whole_ids_doc.readlines()

            medium_whole_parent_id = "100000005232297895"

            for x in range(len(medium_whole_ids)):
                if(medium_whole_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + medium_whole_ids[x].lstrip().rstrip() + "&parentId=" + medium_whole_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
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
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        medium_whole_toppings()

        def medium_left_toppings():
                        
            medium_left_ids_doc = open("medium_left_ids.txt", "r")
            medium_left_ids = medium_left_ids_doc.readlines()

            medium_left_parent_id = "100000005232298501"

            for x in range(len(medium_left_ids)):
                if(medium_left_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + medium_left_ids[x].lstrip().rstrip() + "&parentId=" + medium_left_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
                      'authority': 'www.toasttab.com',
                      'pragma': 'no-cache',
                      'cache-control': 'no-cache',
                      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                      'accept': 'application/json, text/javascript, */*; q=0.01',
                      'x-requested-with': 'XMLHttpRequest',
                      'sec-ch-ua-mobile': '?0',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                      'sec-fetch-site': 'same-origin',
                      'sec-fetch-mode': 'cors',
                      'sec-fetch-dest': 'empty',
                      'referer': 'https://www.toasttab.com/advancedproperties/bulkeditor',
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload, timeout=5)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        medium_left_toppings()

        def medium_right_toppings():
                        
            medium_right_ids_doc = open("medium_right_ids.txt", "r")
            medium_right_ids = medium_right_ids_doc.readlines()

            medium_right_parent_id = "100000005232298835"

            for x in range(len(medium_right_ids)):
                if(medium_right_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + medium_right_ids[x].lstrip().rstrip() + "&parentId=" + medium_right_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
                      'authority': 'www.toasttab.com',
                      'pragma': 'no-cache',
                      'cache-control': 'no-cache',
                      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                      'accept': 'application/json, text/javascript, */*; q=0.01',
                      'x-requested-with': 'XMLHttpRequest',
                      'sec-ch-ua-mobile': '?0',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                      'sec-fetch-site': 'same-origin',
                      'sec-fetch-mode': 'cors',
                      'sec-fetch-dest': 'empty',
                      'referer': 'https://www.toasttab.com/advancedproperties/bulkeditor',
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload, timeout=5)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        medium_right_toppings()
        
    mediums()

    def larges():

        def large_whole_pies():

            stock.write("\n" + "LARGES:")

            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232302668&parentId=100000005232292030&archiveMode=true"
    
            payload={}
            headers = {
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
              'accept-language': 'en-US,en;q=0.9'    }

            response = session.request("GET", url, headers=headers, data=payload)

            json_response  = response.json()

            for pizza in json_response["children"][1:]:
                if 'inventory' in pizza and pizza['inventory'] is not None:
                    stock.write("\n" + pizza['name'])            

        large_whole_pies()

        def large_whole_toppings():

            large_whole_ids_doc = open("large_whole_ids.txt", "r")
            large_whole_ids = large_whole_ids_doc.readlines()

            large_whole_parent_id = "100000005232302672"

            for x in range(len(large_whole_ids)):
                if(large_whole_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + large_whole_ids[x].lstrip().rstrip() + "&parentId=" + large_whole_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
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
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        large_whole_toppings()

        def large_left_toppings():
                        
            large_left_ids_doc = open("large_left_ids.txt", "r")
            large_left_ids = large_left_ids_doc.readlines()

            large_left_parent_id = "100000005232303347"

            for x in range(len(large_left_ids)):
                if(large_left_ids[x].lstrip() != ""):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + large_left_ids[x].lstrip().rstrip() + "&parentId=" + large_left_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
                      'authority': 'www.toasttab.com',
                      'pragma': 'no-cache',
                      'cache-control': 'no-cache',
                      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                      'accept': 'application/json, text/javascript, */*; q=0.01',
                      'x-requested-with': 'XMLHttpRequest',
                      'sec-ch-ua-mobile': '?0',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                      'sec-fetch-site': 'same-origin',
                      'sec-fetch-mode': 'cors',
                      'sec-fetch-dest': 'empty',
                      'referer': 'https://www.toasttab.com/advancedproperties/bulkeditor',
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload, timeout=5)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        large_left_toppings()

        def large_right_toppings():
                        
            large_right_ids_doc = open("large_right_ids.txt", "r")
            large_right_ids = large_right_ids_doc.readlines()

            large_right_parent_id = "100000005232303746"

            for x in range(len(large_right_ids)):
                if(large_right_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + large_right_ids[x].lstrip().rstrip() + "&parentId=" + large_right_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
                      'authority': 'www.toasttab.com',
                      'pragma': 'no-cache',
                      'cache-control': 'no-cache',
                      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
                      'accept': 'application/json, text/javascript, */*; q=0.01',
                      'x-requested-with': 'XMLHttpRequest',
                      'sec-ch-ua-mobile': '?0',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
                      'sec-fetch-site': 'same-origin',
                      'sec-fetch-mode': 'cors',
                      'sec-fetch-dest': 'empty',
                      'referer': 'https://www.toasttab.com/advancedproperties/bulkeditor',
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload, timeout=5)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        large_right_toppings()
        
    larges()

    def half_specialties():

        stock.write("\n" + "HALF SPECIALTIES:")

        def left_half():

            left_half_doc = open("left_half_ids.txt", "r")
            left_half_ids = left_half_doc.readlines()

            left_half_parent_id = "100000007232953180"

            for x in range(len(left_half_ids)):
                if(left_half_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + left_half_ids[x].lstrip().rstrip() + "&parentId=" + left_half_parent_id + "&archiveMode=true"
                                       
                    payload={}
                    
                    headers = {
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
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload)
                    
                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])

        left_half()

        def right_half():

            right_half_doc = open("right_half_ids.txt", "r")
            right_half_ids = right_half_doc.readlines()

            right_half_parent_id = "100000007233285110"

            for x in range(len(right_half_ids)):
                if(right_half_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + right_half_ids[x].lstrip().rstrip() + "&parentId=" + right_half_parent_id + "&archiveMode=true"
                                           
                    payload={}
                    
                    headers = {
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
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload)
                    
                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])

        right_half()

    half_specialties()

    def calzones():

        def calzone_whole():

            stock.write("\n" + "CALZONES:")

            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232307736&parentId=100000005232292030&archiveMode=true"
    
            payload={}
            headers = {
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
              'accept-language': 'en-US,en;q=0.9'    }

            response = session.request("GET", url, headers=headers, data=payload)

            json_response  = response.json()

            for pizza in json_response["children"][1:]:
                if 'inventory' in pizza and pizza['inventory'] is not None:
                    stock.write("\n" + pizza['name'])            

        calzone_whole()

        def calzone_toppings():

            calzone_toppings_ids_doc = open("calzone_toppings_ids.txt", "r")
            calzone_toppings_ids = calzone_toppings_ids_doc.readlines()

            calzone_topping_parent_id = "100000005232307740"

            for x in range(len(calzone_toppings_ids)):
                if(calzone_toppings_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + calzone_toppings_ids[x].lstrip().rstrip() + "&parentId=" + calzone_topping_parent_id + "&archiveMode=true"
                                           
                    payload={}
                    
                    headers = {
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
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload)
                    
                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        calzone_toppings()
        
    calzones()

    def salads():

        def salad_whole():

            stock.write("\n" + "SALADS:")

            url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuGroup&entityId=100000005232308750&parentId=100000005232292030&archiveMode=true"
    
            payload={}
            headers = {
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
              'accept-language': 'en-US,en;q=0.9'    }

            response = session.request("GET", url, headers=headers, data=payload)

            json_response  = response.json()

            for pizza in json_response["children"][1:]:
                if 'inventory' in pizza and pizza['inventory'] == '0':
                    print(pizza['name'])
                    stock.write("\n" + pizza['name'])            

        salad_whole()

        def dressings():

            dressings_ids_doc = open("dressings_ids.txt", "r")
            dressings_ids = dressings_ids_doc.readlines()

            dressings_parent_id = "100000005232308771"

            for x in range(len(dressings_ids)):
                if(dressings_ids[x].lstrip() != "" ):
                    url = "https://www.toasttab.com/advancedproperties/listchildren?entityType=MenuOption&entityId=" + dressings_ids[x].lstrip().rstrip() + "&parentId=" + dressings_parent_id + "&archiveMode=true"
                                
                    payload={}
                    
                    headers = {
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
                      'accept-language': 'en-US,en;q=0.9'    }

                    response = session.request("GET", url, headers=headers, data=payload)

                    json_response  = response.json()

                    if json_response["children"][0]["inventory"] == "0":
                        print(json_response["children"][0]["name"])
                        print(json_response["children"][0]["inventory"])
                        stock.write("\n" + json_response["children"][0]["name"])
                        
        dressings()

    salads()
        
    stock.close()

    stock = open("stock.txt", "r")
    contents = stock.read()
    stock.close()

    def email():
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "TKTKTK"  # Enter your address
        receiver_email = "TKTKTK"  # Enter receiver address
        password = "TKTKTK"
        message = contents

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    email()

main()

print   ("--- %s seconds ---" % (time.time() - start_time))
