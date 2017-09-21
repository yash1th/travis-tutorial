import requests
import praw
def get_status_code(test_url):
    r = requests.get(test_url)
    return r.status_code

if __name__ == '__main__':
    get_status_code(sys.argv[1])	
