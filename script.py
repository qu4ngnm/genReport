import requests
from urllib.parse import unquote
import re
import json


dates = []
ids = []
filenames = []
fileTypes = ['WEBPXTICK_DT.zip', 'TickData_structure.dat', 'TC.txt', 'TC_structure.dat']


def getDateInFileName(filename):
    numeric_part = re.search(r'\d+', filename).group()
    return numeric_part

def sendGetReq():
    for i in range(5599, 5601):
        ids.append(i)
        for filetype in fileTypes:
            url = 'https://links.sgx.com/1.0.0/derivatives-historical/' + str(i) + '/' + filetype
            response = requests.get(url)
            filenames.append(getFileName(response))

def getFileName(response):
    if 'Content-Disposition' in response.headers:
        content_disposition = response.headers['Content-Disposition']
        filename_start = content_disposition.find("filename=")
        if filename_start != -1:
            filename_start += len("filename=")
            filename_end = content_disposition.find(";", filename_start)
            if filename_end == -1:
                filename_end = None
            filename = content_disposition[filename_start:filename_end].strip('"')
            filename = unquote(filename)
            # return getDateInFileName(filename)
            return filename
        
def DownloadFile(url, path):
    try:
        res = requests.get(url)
        with open(path, 'wb') as file:
            file.write(res.content)
    except requests.exceptions.RequestException as e:
        print(f"Download failed. Error: {e}")



sendGetReq()
print(ids)
print(filenames)
json_string = json.dumps(ids, indent=2)
print(json_string)


