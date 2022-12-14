import requests
import http.client
import urllib.request

host_name = '0.0.0.0'  # loopback DTM server address
host_port = '8089'
host_address = '0.0.0.0:8089'


xml = """<?xml version = "1.0" encoding = "UTF-8"?>
<Order>
  <Id>78912</Id>
  <Customer>Jason Sweet</Customer>
</Order>"""

headers = {'Content-Type': 'application/xml'}
# example1: post request
r = requests.post(host_address, data=xml, headers=headers)
print(r.text)
# end of example1: post request

# example2: post request
#sendCDTA = http.client.HTTPConnection(host_name, host_port)
#sendCDTA.request('POST', host_address, xml, headers)
# end of example2: post request

