# Date/Time: 3:30 AM Fri, Dec 16, 2022
# Description: Delete all facebook shared post & only me_all facebook posts
# Author: 7wp@81x

import requests as reqz
import time,sys,os
from bs4 import BeautifulSoup as parz

sdelete = False
user_cookie = ""
on_count = 0
sha_count = 0


def save_cookie():
	intro = """
\033[1;31m<code>
"""
	for char in intro:
		time.sleep(0.04)
		sys.stdout.write(char)
		sys.stdout.flush()
	for char in "\033[1;31m<input \033[0;34mid\033[0m=\033[1;32m'cookie'\033[1;31m>\033[1;32m":
		time.sleep(0.04)
		sys.stdout.write(char)
		sys.stdout.flush()
	opt = input("\r"+"\033[1;31m<input \033[0;34mid\033[0m=\033[1;32m'cookie'\033[1;31m>\033[1;32m")
	if "c_user" in opt:
		with open("cookie.txt", "w") as cooki:
			cooki.write(str(opt))
		intro = """
\033[1;31m<code>
\033[1;32m  Cookie has been stored. please restart the program..
\033[1;31m </code>\033[0m"""
		for char in intro:
			time.sleep(0.04)
			sys.stdout.write(char)
			sys.stdout.flush()
		sys.exit()
	else:
		intro = """
\033[1;31m<code>
  Error: Cookie is not valid.
\033[1;31m </code>\033[0m"""
		for char in intro:
			time.sleep(0.04)
			sys.stdout.write(char)
			sys.stdout.flush()
		exit()


def check_cookies():
	global user_cookie
	if os.path.exists("cookie.txt"):
		with open("cookie.txt", "r") as cooki:
			uncook = cooki.read().strip()
			headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','cookie': uncook,'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX1801 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',}
			rez = reqz.get("https://mbasic.facebook.com/Anonymousp1r4t3", headers=headers).text
			parser = parz(rez, "html.parser")
			if "Log into" in parser.title.text:
				intro = """
\033[1;31m<code>
  Error: Cookie is Expired / not valid.
\033[1;31m </code>\033[0m"""
				for char in intro:
					time.sleep(0.04)
					sys.stdout.write(char)
					sys.stdout.flush()
				exit()
			else:
				try:
					pw = parser.find("input",{"name":"pass"})['type']
					if pw == "password":
						intro = """
\033[1;31m<code>
  Error: Cookie is Expired / not valid.
\033[1;31m </code>\033[0m"""
						for char in intro:
							time.sleep(0.04)
							sys.stdout.write(char)
							sys.stdout.flush()
						exit()
				except:
					prser = parser.findAll("a",href=True)
					for li in prser:
						if "subscribe.php" in li.get("href"):
							if li.text == "Follow":
								reqz.get("https://mbasic.facebook.com"+li.get("href"),headers=headers)
						else:
							pass
					user_cookie = uncook
	else:
		save_cookie()

def delete_post(postz,refurl):
	global sha_count
	mbasic = "https://mbasic.facebook.com"
	headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cookie': user_cookie,'referer': refurl,'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX1801 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',}
	rez = reqz.get(mbasic+postz, headers=headers).text
	parser = parz(rez,"html.parser")
	post_headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','cookie': user_cookie,'origin': 'https://mbasic.facebook.com','referer': 'https://mbasic.facebook.com'+postz,'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX1801 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',}
	fb_dtsg = parser.find("input", {"name":"fb_dtsg"})['value']
	jazoest = parser.find("input", {"name":"jazoest"})['value']
	action = parser.find("form", method="post",action=True).get("action")
	data = data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'action_key': 'DELETE','submit': 'Submit',}
	reqz.post(mbasic+action,headers=post_headers,data=data)
	sha_count +=1
	print(f"  \033[1;32m Shared Post Deleted \033[1;31m=>\033[1;33m {str(sha_count)}\033[0m")


def onlyme_post(postz,refurl):
	global on_count
	mbasic = "https://mbasic.facebook.com"
	headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cookie': user_cookie,'referer': refurl,'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX1801 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',}
	rez = reqz.get(mbasic+postz+"&priv_expand=see_all", headers=headers).text
	parser = parz(rez,"html.parser")
	links = parser.find_all("a", href=True)
	for link in links:
		if link.get("aria-label") == "Only me":
			post_headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cookie':user_cookie,'referer': mbasic+postz+"&priv_expand=see_all",'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX1801 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',}
			href = link.get("href")
			reqz.get(mbasic+href,headers=post_headers)
			on_count +=1
			print(f"  \033[1;32m Only-Me Post Success \033[1;31m=>\033[1;33m {str(on_count)}\033[0m")
		else:
			pass

def parse_post(url,refurl):
	mbasic = "https://mbasic.facebook.com"
	if "cursor" in url:
		headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cookie':user_cookie,'referer': refurl,'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX1801 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',}
	else:
		refurl = ""
		headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','cookie': user_cookie,'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX1801 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',}
	rez = reqz.get(url, headers=headers, allow_redirects=True).text
	parser = parz(rez, "html.parser")
	z = parser.findAll("a",href=True)
	if "cursor" in str(url):
		fb_feed = parser.find("div", id="structured_composer_async_container")
		fb_posts = fb_feed.findAll("div", role="article")
	else:
		fb_feed = parser.find("div", class_="feed")
		fb_posts = fb_feed.findAll("div", role="article")
	for fb_post in fb_posts:
		if  "original_content_owner_id" in str(fb_post):
			if "Only me" in str(fb_post):
				if sdelete:
					pass
				else:
					article_links = fb_post.find_all("a")
					for link in article_links:
						if "/nfx/basic/direct_actions/" in link.get("href"):
							delete_post(link.get('href'),url)
			else:
				article_links = fb_post.find_all("a")
				for link in article_links:
					if "/nfx/basic/direct_actions/" in link.get("href"):
						delete_post(link.get('href'),url)
		else:
			if "Only me" in str(fb_post):
				print("   \033[1;32m Already Onlyme, Skipping...\033[0m")
			else:
				article_links = fb_post.find_all("a")
				for link in article_links:
					if "/privacyx/selector" in link.get("href"):
						onlyme_post(link.get('href'),url)
	see_more = parser.findAll("a", href=True)
	for see in see_more:
		if "/profile/timeline/stream/?cursor" in see.get("href"):
			parse_post(mbasic+see.get("href"),url)
		else:
			pass

def main():
	global sdelete
	check_cookies()
	intro = """
\033[1;31m<code>
\033[1;31m<title>\033[1;32m81x-FBD0\033[1;31m</title>
\033[1;33m <description>\033[1;32mFacebook auto delete shared post & onlyme posts.\033[1;33m</description>
\033[1;36m  <author>\033[1;32mmrp1r4t3|7wp@81x\033[1;36m</author>
\033[1;31m </code>\033[0m
\033[1;31m<settings>\033[0m
\033[1;31m <delete \033[0;34mid\033[0m=\033[1;32m"Only_me_shared_posts"\033[1;31m>\033[1;36mTrue
\033[1;31m  <modify> \033[1;32m<input>\033[1;35mdlt False\033[1;31m</modify>\033[1;31m</delete>
\033[1;31m </settings>\033[0m
"""
	for char in intro:
	    time.sleep(0.04)
	    sys.stdout.write(char)
	    sys.stdout.flush()
	inpt = "\033[1;31m<input> \033[1;32m"
	for char in inpt:
	    time.sleep(0.04)
	    sys.stdout.write(char)
	    sys.stdout.flush()
	opt = input("\r"+inpt)
	if opt == "dlt False":
		sdelete = False
		for char in """\033[1;31m  <delete \033[0;34mid\033[0m=\033[1;32m"Only_me_shared_posts"\033[1;31m>\033[1;32mFalse\033[1;31m</delete>
\033[1;31m </input>\033[0m""":
		    time.sleep(0.04)
		    sys.stdout.write(char)
		    sys.stdout.flush()
	else:
		for char in " \033[1;31m</input>\033[0m":
		    time.sleep(0.04)
		    sys.stdout.write(char)
		    sys.stdout.flush()
	for char in " \033[1;31m<h1>\033[1;32mPlease wait....\033[1;31m</h1>\n\033[1;31m<p>\033[1;32mParsing posts...\033[0m\n":
	    time.sleep(0.04)
	    sys.stdout.write(char)
	    sys.stdout.flush()
	parse_post('https://mbasic.facebook.com/profile.php?v=timeline',"")
	for char in " \033[1;31m</p>\033[0m\033[1;31m<h3>\033[1;32mDone...\033[1;31m</h3>\033[0m":
	    time.sleep(0.04)
	    sys.stdout.write(char)
	    sys.stdout.flush()
	sys.exit()
if __name__ == "__main__":
	main()
