#!/usr/bin/env python
import subprocess, time, sys, urllib, json

print "Starting Snap"
print "Starting individual processes of PhantomJS to handle each breakpoint"

# List of test URLs
urlToCheck = [
    'http://example.com',
    'http://www.google.com',
]

# Allow the url's to be provided via arguments to the call
if len(sys.argv) > 1:
    urlToCheck = []
    sys.argv.pop(0)
    for arg in sys.argv:
        try:
            urllib.urlopen(arg)
        except IOError as e:
            print "ERROR: Invalid URL provided as argument ["+str(arg)+"]", e
            exit(1)
        urlToCheck.append(arg)

# Fallback
if len(urlToCheck) == 0:
    print "ERROR: No urls to test";
    exit(1)

# The BS3 breakpoints I want to see + 320px (regarded as true min screen width)
# It hasn't been tested until it's been tested on an iPhone 4
breakPoints = [
    320,
    480,
    768,
    992,
    1200
]

# Other variables for this to work
startTime = int(time.time())
screenShotPath = "screenshots"

def generateShot(url, width):
    global startTime, screenShotPath
    print "Queued Screenshot FOR:", url, "WIDTH:", width
    namedUrl = url.replace("http://", "")
    namedUrl = namedUrl.replace("https://", "")
    namedUrl = namedUrl.replace("/", "--")
    outputName = screenShotPath+"/"+str(startTime)+"/"+str(width)+"/"+namedUrl+".png"

    # Optional cookie to be set
    cookies = json.dumps({
        'rbViewed' : "%7B%22rbViewed%22%3A%221%22%2C%22lastViewed%22%3A%20%221442385836270%22%2C%20%22threeDaysOrMore%22%3A%20%22false%22%7D"
    })

    # Command and params to be passed through
    command = [
        'phantomjs',
        'render.js',
        str(url),
        str(width),
        outputName,
        cookies,
    ]

    # Fire and Forget
    subprocess.Popen(command)

    # Synchronous Command
    # try:
    #     print " ".join(command)
    #     retcode = subprocess.call(" ".join(command), shell=True)
    #     if retcode < 0:
    #         print >>sys.stderr, "Child was terminated by signal", -retcode
    #     else:
    #         print >>sys.stderr, "Success"
    # except OSError as e:
    #     print >>sys.stderr, "Execution failed:", e

    return True

def shotQueue(currentBp=None, currentUrl=None):
    global breakPoints, urlToCheck
    start = breakPoints[0];
    end = breakPoints[-1];

    # First iteration
    if currentBp is None and currentUrl is None:
        currentBp = start
        currentUrl = urlToCheck[0]
        urlToCheck = urlToCheck[1:]

    # Prevent out of bound recursion. Exit when done - THE END
    elif len(urlToCheck) == 0 and currentBp == end:
        print "Queued, awaiting response"
        exit()

    # Still busy with Break Points for URL
    elif currentBp < end:
        currentBp = breakPoints[breakPoints.index(currentBp)+1]

    # Done with current URL
    elif currentBp == end:
        currentBp = start
        currentUrl = urlToCheck[0]
        urlToCheck = urlToCheck[1:]

    # Generate the Screenshot man
    generateShot(currentUrl, currentBp)

    # Recurse back with the next iteration details
    return shotQueue(currentBp, currentUrl)

# Start it all
shotQueue()
