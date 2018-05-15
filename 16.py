import requests, re, os, base64;
from urlparse import urlparse, parse_qs

def scan(dork, tld, log):
	url = []
	result = open(log,"a")
	page = 0
	print("[+] Scanned Running By Dork : "+dork)
	while page <= 100:
		urll = "http://www.google."+tld+"/search?q="+dork+"&start="+str(page)+"&inurl=https"
		htmll = requests.get(urll).text
		if re.findall('<script src="(.*?)" async defer></script>', htmll):
			print("[-] Captcha Detect! You're Requests Blocked")
			print("[-[ Pleae Trun Off You're Connection For Change New IP Addres")
			pass
		else:
			pass
		link = re.findall(r'<h3 class="r"><a href="(.*?)"',htmll)
		for i in link:
			i=i.strip()
			o = urlparse(i, 'http')
			if i.startswith('/url?'):
				link = parse_qs(o.query)['q'][0]
				url.append(link)
				result.write(str(link+"\n"))
		page+=10
		print("["+str(len(url))+"]  Site Crawled")
	print("["+str(len(url))+"] Success Crawled All")

print("Welcome To A-Dork")
print("Author : Alwan\n\n")
print("""[A-Dork] List  :
	
[1.]Google Dorker""")

tools = raw_input("\nSelect  >>> ")
if tools == "1":
	dork = raw_input("[A-DORK] Input Dork : ")
	if ' ' in dork:
		dork = dork.replace(' ', '+')
	else:
		pass
	dom = "com"
	out = raw_input("[A-DORK] Untuk Menyimpan Hasil Dorking : ")
	scan(dork,dom,out)
	print("[X] A-DORK Num "+tools+" Not Found")
	exit()