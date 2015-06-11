# GtkOnline
A 2 hour hack to replace HTML and JavaScript with Gtk and Python.

At the moment there is no sandbox or any security mechanism at all, so use with care.

Example usage: Download `gtk_browser.py` and execute with `python3 gtk_browser.py <<URL>>`.

URL is a special crafted glade file that includes `<script>` and `<style>` tags.

URL can be local or on the web. You can use the included example by replacing URL with `https://github.com/wolfv/GtkOnline/blob/master/testapp/test.glade`.

### Dependencies

`gtk_browser.py` depends on Gtk3 of course, and also BeautifulSoup. You should be able to install BeautifulSoup4 with `sudo dnf install python3-beautifulsoup4.noarch` on Fedora or on Ubuntu `sudo apt-get install python3-bs4`.

Questions? 

Write me: w.vollprecht@gmail.com 
Twitter: https://twitter.com/wuoulf
