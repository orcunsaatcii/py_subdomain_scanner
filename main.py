import requests
import threading


domain = input("Enter your domain ")
subdomains = set()


class ThreadClass(threading.Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                subdomains.add(self.url)
        except requests.exceptions.ConnectionError:
            pass


with open("subdomains.txt", mode="r") as sb_domain:
    threads = []
    for sb in sb_domain:
        sb = sb.strip()
        url = "https://" + sb + "." + domain
        t = ThreadClass(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


for s in subdomains:
    print("Subdomain -------> ", s)




