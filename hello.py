import urlparse
slovar=''
def app (environ, start_response):
	url=environ
	print url
	#query = urlparse.urlparse(url).query
	#url_fix=query.split("&")
	#for slovar in url_fix:
	#	print 'fix_url---'+ slovar
	
	#status='200 OK'
	#headers = [
	#	('Content-Type', 'text/plain')
	#]
	#body=slovar
	#print 'body.....'+body
	#start_response(status, headers)
	#return[body]
	

#url = "http://example.com/?a=1&a=2&c=123&d=6&a=10"
#print url
#query = urlparse.urlparse(url).query
#url2=query.split("&")


#params = urlparse.parse_qs(query)
#print params

#for arg in url2:
#	print arg