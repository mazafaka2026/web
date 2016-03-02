import urlparse
slovar=''
def application(env, start_response):
	env=url
	status='200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body=slovar
	start_response(status, headers)
	return[body]
	

url = "http://example.com/?a=1&a=2&c=123&d=6"
print url
query = urlparse.urlparse(url).query
#print query

params = urlparse.parse_qs(query)
#print params

for arg in params:
	if (len(params[arg])) > 1: 
		while True:
			if (len(params[arg])) <= 0:
				break
			else:
				slovar=(slovar)+((str(arg)+'='+str(params[arg][0]))) +'''
'''
				#print slovar
				del(params[arg][0])
	else:
		slovar=(slovar)+(((str(arg)+'='+str(params[arg][0]))))+'''
'''
		#print slovar
print slovar