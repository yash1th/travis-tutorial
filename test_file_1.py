import requests
import praw
r = requests.get('https://google.com')
print(r.status_code)

def code():
	return r.status_code
