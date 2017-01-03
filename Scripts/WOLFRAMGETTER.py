import wolframalpha
import sys

inp = sys.argv[1]
client = wolframalpha.Client('4XUQL2-GYULW3729X')
res = client.query(inp)

for pod in res.pods:
    for sub in pod.subpods:
		for img in sub.img:
			if pod.id == 'Result' or pod.id == 'Plot':
				print img.src
