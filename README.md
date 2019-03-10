```
           _             _         __                _  _
__      __(_) _ __    __| |  ___  / _|  __ _  _   _ | || |_  ___
\ \ /\ / /| || '_ \  / _` | / _ \| |_  / _` || | | || || __|/ __|
 \ V  V / | || | | || (_| ||  __/|  _|| (_| || |_| || || |_ \__ \
  \_/\_/  |_||_| |_| \__,_| \___||_|   \__,_| \__,_||_| \__||___/

```
Tool to quickly determine which processes or services are not defaults on Windows. Useful for CTFs, and maybe elsewhere as well!

## Installation
Requires Python3 and `pipenv`
```
git clone git@github.com:jroblak/windefaults.git
cd windefaults
pipenv install
```

## Usage
```
analyze.py [OPTIONS] FILE_PATH

Options:
  --item_type [services|processes]
                                  The type of items you're analyzing (default:
                                  services)
  --version [2008|2012|2016|2019|10]
                                  The version of Windows you're analyzing
                                  (default: 10)
  --help                          Show this message and exit.
```
`FILE_PATH`: windefaults expects a csv file, with the first column being the name of the process
or service (this is the default `Export-Csv` behavior)

## Example:
```
➜  pipenv run python analyze.py --version=2012 --item_type=services test/testcases/service-test.csv
The following non-default services were found:
[+] badservice
```
