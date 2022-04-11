import os
import requests
import logging
from requests.exceptions import HTTPError, ConnectionError, RequestException, ConnectTimeout


class JiraHelper(object):
    logging.getLogger().setLevel(logging.INFO)
    req_session = requests.Session()
    CALCULATION_RESOURCES_PATH = 'src/report_puller/resources/calculation'

    def __init__(self):
        self.jira_url = 'https://trigentnav.atlassian.net'
        self.jira_usname = "Radha S C"
        self.jira_password = "TriDO@123"

    def make_jira_request(self, endpoint, request_type, payload=None):
        """
        Make REST call to Jira
        Report Puller needs to run all the way through program execution so that metrics can be captured
        for all teams. As a result, error handling will be captured by the setup_logging_to_file() method in
        logging_descriptor.py. setup_logging_to_file() will be invoked in the main method of Report Puller.
        :param (str) endpoint: Jira REST V2 API endpoint.
        https://developer.atlassian.com/cloud/jira/platform/rest/v2/
        :param (str) request_type: The HTTP request method
        :param (dict) payload: Payload body in dictionary, default is None
        :return: (dictionary):  Response body
        """
        # url = self.jira_url + endpoint
        url = endpoint
        headers = {'content-type': 'application/json'}
        auth = (self.jira_usname, self.jira_password)
        resp = None

        try:
            resp = self.req_session.request(method=request_type.upper(), url=url,
                                            json=payload, headers=headers, auth=auth)
            resp.raise_for_status()
        except (HTTPError, ConnectionError, RequestException, ConnectTimeout) as err:
            print(err)

        if resp and resp.status_code == 200:
            return resp.json()
        else:
            return None
