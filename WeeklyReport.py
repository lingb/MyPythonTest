import os, sys, getopt, getpass, time, logging
import jira.client
from jira.client import JIRA

# 參數	 說明
# level	 日誌之安全等級 (0, 10, 20, 40, 50)
# format	 控制輸出訊息的格式化字串
# filename	 用來儲存輸出訊息的日誌檔案名稱
# filemode	 開啟日誌檔案之模式, 如 'a' (預設), 'w' 等
# datefmt	 輸出日期時間 asctime 之格式字串, 與 time.strftime()
# style	 格式化字串的標示字元, 有三種 : % (預設), {, 或 $
# handlers	 加入至根日誌之處理器, 不可與 stream, filename 同時存在
# stream	 標準輸出之串流

logging.basicConfig(level=logging.DEBUG,
filename='WeeklyReportLog.txt',
datefmt='%Y%m%dT%H%M%S',
format='%(asctime)s - %(levelname)s : %(message)s')
#  格式化字串	 說明
#  %(asctime)s	 日期時間, 格式為 YYYY-MM-DD HH:mm:SS,ms (毫秒)
#  %(message)s	 使用者自訂訊息
#  %(levelname)s	 日誌安全等級
#  %(levelno)s	 日誌安全等級之數值
#  %(name)s	 使用者名稱 (帳號) 
#  %(lineno)d	 日誌輸出函數呼叫於程式中所在之列數
#  %(filename)s	 日誌輸出函數之模組的檔名
#  %(module)s	 日誌輸出函數之模組名稱
#  %(pathname)s	 日誌輸出函數之模組之完整路徑
#  %(funcName)s	 日誌輸出函數之名稱
#  %(threrad)d	 執行緒 ID
#  %(threradName)s	 執行緒名稱
#  %(process)d	 程序 ID
#  %(created)f	 以 UNIX 標準表示之現在時間 (浮點數)

jira_user = ""
jira_passwd = ""
assignee = "currentuser()"
week = 1

try:
    opts, args = getopt.getopt(sys.argv[1:], "hu:a:w:", ["jirauser=", "assignee=", "week="])
except getopt.GetoptError:
    logging.debug(os.path.basename(__file__) + ' -u <jirauser> -a <assignee> -w <week>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        logging.debug(os.path.basename(__file__) + ' -u <jirauser> -a <assignee> -w <week>')
        sys.exit()
    elif opt in ("-u", "--jirauser"):
        jira_user = arg
    elif opt in ("-a", "--assignee"):
        assignee = arg
    elif opt in ("-w", "--week"):
        week = int(arg)

if jira_user == "":
    logging.debug("You should specify the user name with option -u to login into JIRA server.")
    sys.exit(3)
logging.debug("using JIRA user %s, Getting %s weekly report for week %d " % (jira_user, assignee, week))
jira_passwd = getpass.getpass("Please input passsword for JIRA user:")

options = {'server': 'http://jira.adlinktech.com:8080', 'verify':False}
jira = JIRA(options, basic_auth=(jira_user, jira_passwd))
issues_in_project = jira.search_issues('status was "In Progress" during (startOfYear("+51w"), startOfYear("+52w")) AND assignee in (membersOf(SEC-SPD), jean.wang)', maxResults = 1000)

i = 0
for issue in issues_in_project:
    logging.debug(issue.raw)
    for field_name in issue.raw['fields']:
        logging.debug("Field:%s, Value:%s" % (field_name, issue.raw['fields'][field_name]))
    logging.debug("key: %s" % issue.key)
    logging.debug("project key: %s" % issue.fields.project.key)
    logging.debug("issue type: %s" % issue.fields.issuetype.name)
    logging.debug("reporter: %s" % issue.fields.reporter.displayName)
    logging.debug("assignee: %s" % issue.fields.assignee)
    logging.debug("summary: %s" % issue.fields.summary)
    for comment in jira.comments(issue.key):
        logging.debug(comment)
        break
    i = i + 1
    if i >= 1:
        break
    # log_entry_count = len(issue.fields.comments)
    # for i in range(log_entry_count):
    #     logging.debug(issue.key, issue.fields.worklog.worklogs[i].timeSpent, issue.fields.worklog.worklogs[i].updated, issue.fields.worklog.worklogs[i].updateAuthor)    # log_entry_count = len(value.fields.worklog.worklogs)
    # for i in range(log_entry_count):
    #     logging.debug(issue.key, issue.fields.worklog.worklogs[i].timeSpent, issue.fields.worklog.worklogs[i].updated, issue.fields.worklog.worklogs[i].updateAuthor)