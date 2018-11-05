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

i = 0
for message in messages:
    matches = re.findall("(?i)ipmi", message.Body)
    if len(matches) >= 2:
        names = re.search('】(.+?)\(', message.Subject)
        if names:
            print(names.group(1))
