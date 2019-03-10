```
           _             _         __                _  _        
__      __(_) _ __    __| |  ___  / _|  __ _  _   _ | || |_  ___ 
\ \ /\ / /| || '_ \  / _` | / _ \| |_  / _` || | | || || __|/ __|
 \ V  V / | || | | || (_| ||  __/|  _|| (_| || |_| || || |_ \__ \
  \_/\_/  |_||_| |_| \__,_| \___||_|   \__,_| \__,_||_| \__||___/
                                                                 
```
Tool to quickly determine which processes or services are not defaults on Windows

## Installation
Requires Python3 and `pipenv`
```
git clone git@github.com:jroblak/windefaults.git
pipenv install
```

## Usage
```
analyze.py [OPTIONS] [[services|processes]] FILE_PATH

Options:
  --version [2008|2012|2016|2019|10]
                                  The version of Windows you're analyzing
                                  (default: 10)
  --help                          Show this message and exit.
```
`FILE_PATH`: windefaults expects a csv file, with the first column being the name of the process
or service (this is the default `Export-Csv` behavior)

## Example:
```
➜  pipenv run python analyze.py --version="2012" services test/testcases/service-test.csv
The following non-default services were found:
[+] badservice
```
