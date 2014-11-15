import time
import requests
import grequests
import pickle

with open("backpages","rb") as f:
	urls = pickle.load(f)

content = []
before = time.time()
for url in urls[:30]:
	content.append(requests.get(url))
after = time.time()

urlz = (grequests.get(u) for u in urls[:30])
before_async = time.time()
grequests.map(urlz)
after_async = time.time()

print after - before," time lapse synchronously"
print after_async - before_async," time after async"
