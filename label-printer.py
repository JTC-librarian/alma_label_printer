import urllib.request
import re
import xml.etree.ElementTree as ET
import time
import win32printing
import win32print
### Settings ###
font = {"faceName":"Microsoft Sans Serif", "height":12, "weight":700}
linegap = 1 # Sets spacing between the lines; 1 seems to work well
printer_name = "ptouch"
### Variables ###
api_base = "https://api-eu.hosted.exlibrisgroup.com" # Check this
api_key = "aSuitableApiKey" # Put your API key here
### Headers ###
headers = {}
authorization_header = "apikey " + api_key
headers["Authorization"] = authorization_header
### HTTP Method Functions ###
def getUrl(url):
    req = urllib.request.Request(url=url, data=None, headers=headers, method='GET')
    try:
        get = urllib.request.urlopen(req)
        text = get.read()
        text_string = text.decode('utf8')
        return text_string
    except Exception as e:
        print(str(e))
        error_text = e.read()
        error_text_string = error_text.decode('utf8')
        return error_text_string
### Main Functions ###
def get_item_data(barcode):
    errorfile = open('get_item_label.error', 'a+', encoding='utf8', errors='ignore')
    api_query = "/almaws/v1/items?view=label&item_barcode=" + barcode
    url = api_base + api_query
    result = getUrl(url)
    return result
def get_item_callnum(item_data):
    root = ET.fromstring(item_data)
    hol = root.find('holding_data')
    callnum = hol.find('call_number').text
    return callnum
def get_callnum_dict(callnum):
    ## Step 1. Split number and cutter.
    try:
        pattern = re.match(r'(.*?) (.*)', callnum)
        number = pattern.group(1)
        cutter = pattern.group(2)
    except:
        number = label
        cutter = ""
    ## Step 2. Split main number and decimal.
    try:
        pattern = re.match(r'(.*?)\.(.*)', number)
        main = pattern.group(1) + "."
        decimal = pattern.group(2)
    except:
        main = number
        decimal = ""
    callnum_dict = {'main':main, 'decimal':decimal, 'cutter':cutter}
    return callnum_dict
def get_decimal_list(decimal):
    count = 0
    new_decimal = ""
    for digit in decimal:
        new_decimal = new_decimal + digit
        count = count + 1
        if count % 3 == 0:
            new_decimal = new_decimal + "."
    decimal_list = new_decimal.split(".")
    return decimal_list
def parse_callnum(callnum):
    callnum_dict = get_callnum_dict(callnum)
    decimal_list = get_decimal_list(callnum_dict['decimal'])
    full_list = []
    full_list.append(callnum_dict['main'])
    for dec in decimal_list:
        full_list.append(dec)
    full_list.append(callnum_dict['cutter'])
    for item in full_list:
        if item == "":
            full_list.remove(item) 
    return full_list
def print_label(parsed_callnum):
    with win32printing.Printer(printer_name=printer_name, linegap=linegap) as printer:
        for item in parsed_callnum:
            printer.text(item, font_config=font)
def run_whole_process():
    try:
        barcode = input("Type or scan the barcode: ")
        item_data = get_item_data(barcode)
        callnum = get_item_callnum(item_data)
        parsed_callnum = parse_callnum(callnum)
        print_label(parsed_callnum)
        print("\n")
        for item in parsed_callnum:
            print(item)
        print("\n")
        print("\n")
        return True
    except:
        print("\n")
        print("Problem getting call number or printing.")
        print("See above for error message.")
        print("Please try again.")
        print("\n")
        print("\n")
        return True
### Main Script ###
ready = True
while ready:
    ready = False
    ready = run_whole_process()




