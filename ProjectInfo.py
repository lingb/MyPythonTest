import urllib.request
import re
from lxml import html
import requests
import sys
from argparse import ArgumentParser

def printline(contents, start, count):
    i = start
    while i < start + count:
        sys.stdout.write(re.sub(r'[\r\n]+', '', contents[i]))
        sys.stdout.write(' | ')
        i = i + 1
    sys.stdout.write('\n')
    sys.stdout.flush()

def FindProjectInfo(TitleSkip, URL, ProjectName):
    InfoCount = 8
    IndexOfProjectName = 1
    page = requests.get(URL)
    tree = html.fromstring(page.content)
    contents = tree.xpath('//span[@lang="EN-US"]/text()')
    i = TitleSkip
    while i + IndexOfProjectName < len(contents):
        # print(ProjectName, contents[i + IndexOfProjectName])
        match = re.search(ProjectName, contents[i + IndexOfProjectName])
        if match != None:
            printline(contents, TitleSkip, InfoCount)
            printline(contents, i - IndexOfProjectName, InfoCount)
        i = i + 1

parser = ArgumentParser(description="Get project information from web sites")
parser.add_argument("ProjectName", help="Keyword of the project you want to get information")
# parser.add_argument("-f", "--folder", dest="")
args = parser.parse_args()
TargetProjectName = args.ProjectName
print(type(TargetProjectName), len(TargetProjectName))
FindProjectInfo(1, 'http://w3.adlinktech.com/APMO/2017%20Approved%20ODM%20DEF%20Gate.htm', TargetProjectName)
FindProjectInfo(2, 'http://w3.adlinktech.com/APMO/2017%20Approved%20STD%20DEF%20Gate.htm', TargetProjectName)
