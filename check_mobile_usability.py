# From http://www.thetaranights.com/website-mobile-friendly-tester-automation-script-python-codes-for-mobile-friendly-test/
# check mobile usability

from json import loads
import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]    

with open('websitesformobilefriendlytest.txt') as f:
    for line in f:
        google_results = br.open("https://www.googleapis.com/pagespeedonline/v3beta1/mobileReady?url=http://" + str(line)).read()
        json_obj = loads(google_results)
        if json_obj["ruleGroups"]["USABILITY"]["pass"] == True:
            print "Congrats " + str(line)  + " is mobile friendly"
        else:
            print str(line) + " is not mobile friendly"
