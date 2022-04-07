import os
import json


if __name__ == '__main__':
    # jh = JiraHelper()
    # endpoint = 'https://trigentnav.atlassian.net/jira/software/c/projects/BLU/issues/?jql=project =' \
    #            ' "BLU" AND assignee=61e7dc3c93885f0069689568 '
    # res = jh.make_jira_request(endpoint, "GET")
    # print(res)
    os.makedirs ('result', exist_ok=True)
    data = {
        "state": "karnataka",
        "capital": "Bengaluru"
    }
    with open('result/' + 'output.json', 'w') as email_file:
        json.dump(data, email_file)
