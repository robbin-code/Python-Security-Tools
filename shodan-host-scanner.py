import shodan

SHODAN_API_KEY = "SHODAN API HERE"
api = shodan.Shodan(SHODAN_API_KEY)


user_input = raw_input('[*] Enter a device to scan (Example: Windows, Linux, etc..): ')

if user_input == "":
	print "[*] Enter some device name ( example: windows, linux, cisco, etc...)"
	import sys
	sys.exit()
	
try:
        #grab user input
        results = api.search(user_input) 

        #results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip_str']
                print result['data']
                print 'OS: %s' % result['os']
                print ''
except shodan.APIError, e:
        print 'Error: %s' % e
        
print '[*] Finish Results for ' + user_input.capitalize() + '\n'
