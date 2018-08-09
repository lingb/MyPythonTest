import calendar
import datetime
import logging
import os
import re
import shutil
import sys
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
box104 = inbox.Folders["104"]
messages = box104.Items
'''message = messages.GetLast()
body_content = message.Body
subject = message.Subject
categories = message.Categories
print(body_content)
print(subject)
print(categories)'''

i = 0
for message in messages:
    matches = re.findall("(?i)ipmi", message.Body)
    if len(matches) > 2:
        names = re.search('】(.+?)\(', message.Subject)
        if names:
            print(names.group(1))
        '''print(message.Subject)
        i=i+1
        if i >= 10:
            break'''
