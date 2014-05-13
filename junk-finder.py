'''
External Dependencies:
https://github.com/charlierguo/gmail
http://www.crummy.com/software/BeautifulSoup/
'''

from sys import argv
import gmail
import webbrowser
from datetime import date, timedelta
from email import header
from bs4 import BeautifulSoup as bs
import os

def clean_header(h):
	s = h.encode('utf-8')
	s = header.decode_header(s)[0][0]
	return s


def find_junk(g, days):
	after_date = date.today() - timedelta(days=int(days))
	messages = g.inbox().mail(after=after_date, prefetch=True)
	print "Looking through %i messages for junk." % len(messages)
	junk = []
	for m in messages:
		try:
			soup = bs(m.html)
		except:
			try:
				soup = bs(m.body)
			except:
				print "Couldn't parse email from " + clean_header(m.fr)
		links = soup.find_all('a')
		for l in links:
			try:
				link_text = str(l.contents[0])
				if 'unsubscribe' in link_text.lower():
						junk.append({
							'sender'  	 : clean_header(m.fr),
							'subject' 	 : clean_header(m.subject),
							'ulink'   	 : l.get('href'),
							'ulink_text' : link_text
							})
			except:
				continue
	
	return junk

def write_html(junk):
	#set up the HTML doc and table
	html = '''
<!DOCTYPE HTML>
<html>
	<h1>Junk</h1>
	<table>
		<tr>
			<th>Sender</th>
			<th>Subject</th>
			<th>Unsubscribe Link</th>
		</tr>
	'''

	#add the junk
	for i in junk:
		html = html + '''
		<tr>
			<td>{0}</td>
			<td>{1}</td>
			<td><a href='{2}' target='_blank'>{3}</a></td>
		</tr>
		'''.format(i['sender'], i['subject'], i['ulink'], i['ulink_text'])
	
	#close the table and doc
	html = html + '''
	</table>
</html>
	'''
	return html

def main():
	_, user, pw, days = argv
	g = gmail.login(user, pw)
	if g.logged_in:
		print "Logged in to %s." % user
		junk = find_junk(g, days)
		html = write_html(junk)
		
		filename = "%s--%s.html" % (str(date.today() - timedelta(days=int(days))), str(date.today()))
		f = open(filename, 'w')
		f.write(html)
		f.close()
		try:
			filename = 'file://%s/%s' % (os.path.dirname(os.path.realpath(__file__)), filename)
			webbrowser.open_new_tab(filename)
		except:
			print 'Open %s in your web browser.' % filename

	else:
		print "Could not log in to %s." % user

if __name__ == '__main__':
	main()