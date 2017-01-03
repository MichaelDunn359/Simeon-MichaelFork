#!C:/Python27/python
print "Content-type: text/html\n\n"

import wolframalpha
import sys
import cgi
import urllib 

form = cgi.FieldStorage()
equation = form.getvalue('equation')
equation = urllib.unquote(equation)

client = wolframalpha.Client('4XUQL2-GYULW3729X')
res = client.query(equation)

for pod in res.pods:
    for sub in pod.subpods:
		for img in sub.img:
			if pod.id == 'Result' or pod.id == 'Plot':
				print img.src
