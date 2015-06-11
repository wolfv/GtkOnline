import sys
import signal
import requests
import os

from gi.repository import Gtk, Gdk
from bs4 import BeautifulSoup

def get_fileobject(src):
	if src.startswith('http'):
		return requests.get(src)
	else:
		return open(src, 'r')

if __name__ == '__main__':
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	filename = sys.argv[1]

	root_path = os.path.dirname(filename)
	print('root path: ', root_path)
	f = get_fileobject(filename)

	builder = Gtk.Builder()

	soup = BeautifulSoup(f)

	scripts = []
	for script in soup.find_all('script'):
		print("adding script ", script.get('src'))

		scripts.append(get_fileobject(os.path.join(root_path, script.get('src'))))
		script.extract() # remove script tag

	styles = []
	for style in soup.find_all('style'):
		print("adding style ", style.get('src'))
		styles.append(get_fileobject(os.path.join(root_path, style.get('src'))))
		style.extract() # remove style tag


	print(str(soup.find('interface')))
	builder.add_from_string(str(soup.find('interface')))
	# builder.connect_signals(Handler())

	window = Gtk.Window()
	window.set_title('Gtk Browser')
	window.add(builder.get_object('root'))
	window.show_all()

	for style in styles:
		style_provider = Gtk.CssProvider()
		style_provider.load_from_data(bytes(style.read(), 'utf-8'))
		style.close()
		builder.get_object('root').get_style_context()\
			.add_provider_for_screen(
				builder.get_object('root').get_screen(), 
				style_provider, 
				Gtk.STYLE_PROVIDER_PRIORITY_USER)

	for script in scripts:
		exec(script.read(), {'builder': builder})

	Gtk.main()