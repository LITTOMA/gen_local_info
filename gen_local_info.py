import urllib2,re,os,traceback

def mkdir(path):
	if not os.path.exists(path):
		print 'make dir:', path
		os.makedirs(path)

url = 'http://3dsdb.com/xml.php'
xml = urllib2.urlopen(url).read()

partten = r'<release>[\s|\S]+?</release>'
matches = re.compile(partten).findall(xml)

tidpar = re.compile(r'<titleid>(.+?)</titleid>')
regpar = re.compile(r'<region>(.+?)</region>')
langpar = re.compile(r'<languages>(.+?)</languages>')
for m in matches:
	try:
		tid = tidpar.search(m).group(1)
		region = regpar.search(m).group(1)
		language = langpar.search(m).group(1).split(',')[0]
		mkdir('luma/locales/')
		filepath = 'luma/locales/%s.txt'%tid
		if os.path.exists(filepath):
			print 'File: "%s" exists, skip'%filepath
			continue
		with open('luma/locales/%s.txt'%tid, 'w')as txt:
			txt.write('%s %s'%(region.upper(), language.upper()))
	except:
		traceback.print_exc()
		continue
