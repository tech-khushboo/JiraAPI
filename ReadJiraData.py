
from atlassian import Jira
import pymongo

client = pymongo.MongoClient('mongodb://khushboo:password123@ds135068.mlab.com:35068/jiradb?retryWrites=false')
db = client['jiradb']
collection = db['task']


jira = Jira(url='http://localhost:8085', username='khushboo2502@gmail.com', password='Jira@123')
JQL = 'project = TEST AND status NOT IN (Closed, Resolved) ORDER BY issuekey'
data = jira.jql(JQL)
print(data['total'])
for tasks in data['issues']:
    print(tasks['id'])
    print(tasks['fields']['summary'])
    mydict = { "id": tasks['id'], "summary": tasks['fields']['summary'] }
    x = collection.insert_one(mydict)
    print(x)