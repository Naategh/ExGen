# ExGen
This repository contains a python script that creates exploit templates for XSSI, JSONP Hijacking, Clickjacking and CORS vulnerabilities.
Also, It can help you to determine an endpoint is vulnerable or not.

## Examples
```
$ python ExGen.py -e cors -u http://target.com/vulnerable/endpoint

Your exploit saved as target.com-cors-vulnerable-endpoint.html
You can open it in your browser via file:///path/target.com-cors-vulnerable-endpoint.html
```
