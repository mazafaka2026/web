import urlparse
slovar=''
def app (environ, start_response):
	url=''#environ['QUERY_STRING']
	print url
	query = urlparse.urlparse(url).query
	url_fix=query.split("&")
	for slovar in url_fix:
		print 'fix_url---'+ slovar
	
	status='200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	body=slovar
	print 'body.....'+body
	start_response(status, headers)
	if url == '':
		print 'bed'
	else:
		print 'good'
		print url
		url2=url.split("&")
		for arg in url2:
			print arg
			slovar=arg
		print slovar
		body=slovar
		return[body]
