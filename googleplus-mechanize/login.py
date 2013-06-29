#!/usr/bin/env python

import mechanize

cj = mechanize.LWPCookieJar()
cj.load("cookies.txt")

br = mechanize.Browser()
br.set_cookiejar(cj)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.810.0 Safari/535.1 cd34/0.9b')]
br.open('https://www.google.com/accounts/ServiceLogin?service=oz&passive=1209600&continue=https://plus.google.com/up/start/')

br.select_form(nr=0)

br.form.find_control("Email").readonly = False
br.form['Email'] = 'email@address.com'
br.form['Passwd'] = 'supersecretpasswordhere'

br.submit()

for l in br.links():
    print l

cj.save("cookies.txt")
