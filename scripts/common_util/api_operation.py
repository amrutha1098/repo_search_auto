from scripts.common_util.constants import *


class API_OPERATIONS:

    def __init__(self):
        self.request_url = api_request_url

    # example request URL: https://api.github.com/search/repositories?q=test&per_page=10&page=1&sort=stars&order=desc
    # input params
    #       str  : q / keyword    
    #       int  : per_page     
    #       int  : page  ( current page in ui )
    def get_repo_details(self, keyword, per_page, page):
        url = self.request_url + 'search/repositories?q=' + str(keyword) + '&per_page=' + str(
            per_page) + '&page=' + str(page) + '&sort=stars&order=desc'
        response = requests.get(url)
        data = response.json()
        return data['total_count']

    # example request URL: https://api.github.com/repos/storybookjs/storybook/commits?per_page=3&page=0
    # input params
    #       str  : git_op ( commits or forks)
    #       str  : repo_name
    #       str  : owner_name
    #       int  : per_page     
    #       int  : page  ( current page in ui )
    def get_commits_details(self, git_op, keyword, per_page, page):
        url = self.request_url + 'repos/' + str(repo_name) + '/' + str(owner_name) + '/' + st(
            git_op) + '?per_page=' + str(per_page) + '&page=' + str(page)
        response = requests.get(url)
        data = response.json()
        return data

    # example request URL: https://api.github.com/users/Rippyblogger
    # input params
    #       str  : name ( commits or forks)
    def get_github_bio_details(self, name):
        url = self.request_url + 'users/' + str(name)
        response = requests.get(url)
        data = response.json()
        return data

    #  function to form the json to verify for ui
