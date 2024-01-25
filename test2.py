import requests
from urllib.parse import unquote
import re
import json
import argparse
from datetime import date


parser = argparse.ArgumentParser(description='Crawl Data CLI')
parser.add_argument('--date', type=str, help='Input a date with format yyyy/mm/dd')
args = parser.parse_args()

date = args.date

def findIDbyDate(date):
    data = json.load(open('output.json'))
    return data[formatDate(date)]

def formatDate(datez):
    date = datez.replace("/", "")
    return date


findIDbyDate(date)


# dates = []
# ids = []

# def getDateInFileName(filename):
#     numeric_part = re.search(r'\d+', filename).group()
#     return numeric_part

# # url = 'https://links.sgx.com/1.0.0/derivatives-historical/5601/WEBPXTICK_DT.zip'  # Replace with the actual URL of the resource

# # response = requests.get(url)
# def sendGetReq(fromz, toz):
#     for i in range(fromz, toz):
#         print(i)
#         ids.append(i)
#         url = 'https://links.sgx.com/1.0.0/derivatives-historical/' + str(i) + '/TC.txt'
#         response = requests.head(url)
#         dates.append(getFileName(response))

# def getFileName(response):
#     if 'Content-Disposition' in response.headers:
#         content_disposition = response.headers['Content-Disposition']
#         filename_start = content_disposition.find("filename=")
#         if filename_start != -1:
#             filename_start += len("filename=")
#             filename_end = content_disposition.find(";", filename_start)
#             if filename_end == -1:
#                 filename_end = None
#             filename = content_disposition[filename_start:filename_end].strip('"')
#             filename = unquote(filename)
#             return getDateInFileName(filename)
            # return filename
        
# sendGetReq()

# data = json.load(open('output.json'))
# print(data['20130205'])