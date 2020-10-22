#!/usr/bin/python3
import requests
import bs4 
import argparse
import sys
from colorama import Fore,init
init(convert=True)

def gitpinnedrepo(username):
	res = requests.get("https://github.com/%s" %(username))
	if res.status_code == 404:
		print(Fore.RED +"No github account with the username",username)
		return ;
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	pinned = soup.find_all("span", class_='repo')
	print(Fore.BLUE + "\n [+] Gitgo scraping pinned_repo Name of user..... \n")
	for pinned_repo in range(len(pinned)):
		print(Fore.GREEN + pinned[pinned_repo].text)
	print("...............................................................")

def gistrepo(username):
	res = requests.get("https://gist.github.com/%s" %(username))
	if res.status_code == 404:
		print(Fore.RED +"No gist account with the username",username)
		return ;
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	gist = soup.find_all("strong", class_='css-truncate-target')
	print(Fore.BLUE + "\n\n [+] Gitgo scraping all gist Name of user..... \n")
	for gist_repo in range(len(gist)):
		print(Fore.GREEN + gist[gist_repo].text)
	print("...............................................................")
		
def getprofile_stats(username):
	res = requests.get("https://github.com/{}".format(username))
	if res.status_code == 404:
		print(Fore.RED +"No github profile with the username",username)
		return ;
	soup = bs4.BeautifulSoup(res.content,"html.parser")
	try:
		name=soup.find('span',{'class':'p-name vcard-fullname d-block overflow-hidden'}).text
	except:
		name='Not Available'
	try:
		username=soup.find('span',{'class':'p-nickname vcard-username d-block'}).text
	except:
		username='Not Available'
	try:
		data=soup.find_all('span',{'class':'text-bold text-gray-dark'})
		stars=data[2].text
		following=data[1].text
		followers=data[0].text
	except:
		data='Not Available'
		stars='Not Available'
		following='Not Available'
		followers='Not Available'
	try:
		location=soup.find('span',{'class':'p-label'}).text
	except:
		location='Not Available'
	try:
		data=soup.find('span',{'class':'Counter'})
		repositories=data.text
	except:
		repositories='Not Available'
	profile_data={'name':name,'username':username,'location':location,'stars':stars,'following':following,'followers':followers,'repositories':repositories}
	print(Fore.BLUE + "\n\n [+] Gitgo scraping profile_data of user \n")
	print(Fore.GREEN)
	print(profile_data)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--gitusername',help='Github username')
	args = parser.parse_args()
	print(Fore.RED + '''
  
WELCOME WELCOME WELCOME !!! 
	
''')

	if args.gitusername:
		gitpinnedrepo(args.gitusername)
		gistrepo(args.gitusername)
		getprofile_stats(args.gitusername)
		exit()
  
  
#   https://www.webnots.com/alt-code-shortcuts-for-block-elements/#:~:text=Hold%20one%20of%20the%20alt,eighths%20block%20symbol%20like%20%E2%96%87.
 