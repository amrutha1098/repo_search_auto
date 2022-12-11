# repo_search_auto

Automated framework for repository Search [Github](https://github.com/kesavan-rangan/repo-search)

### Installation

```console

pip3 install selenium
pip3 install html-testRunner
pip3 install requests

 **************** or ******************
 
 pip3 install -r requirements.txt
 
```
please follow following instruction to generate proper html report [link](https://stackoverflow.com/questions/71858651/attributeerror-htmltestresult-object-has-no-attribute-count-relevant-tb-lev)

copy the required chrome webdriver to repo_search_automation/input folder [link](https://chromedriver.chromium.org/downloads)
To check which chromedriver to be downloaded open google chrome, click the three dots in the upper-right corner of the window and click on help.

### Run

```console
python3 scripts/test_suites/repo_search.py

```

### Where do we find the report and logs 

```console

report > repo_search_automation/reports/MyReport.html
logs >  repo_search_automation/logs
```
