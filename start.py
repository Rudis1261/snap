#!/usr/bin/env python
#import time
import subprocess, time

print "Starting Snap"
print "Starting individual processes of PhantomJS to handle each breakpoint"

# List of test URLs
urlToCheck = [
    'http://example.com',
    'http://www.google.co.za'
]

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

def generateShot(url, size):
    global startTime, screenShotPath
    print "Queued Screenshot FOR:", url, ", SIZE:", size
    namedUrl = url.replace("http://", "")
    namedUrl = namedUrl.replace("https://", "")
    namedUrl = namedUrl.replace("/", "--")
    outputName = screenShotPath+"/"+str(startTime)+"/"+str(size)+"/"+namedUrl+".png"
    
    process = subprocess.Popen([
        'phantomjs', 
        'render.js', 
        str(url),
        str(size),
        outputName
    ])

    return process

def shotQueue(currentBp=None, currentUrl=None):
    global breakPoints, urlToCheck
    start = breakPoints[0];
    end = breakPoints[-1];
    
    # First iteration
    if currentBp is None and currentUrl is None:
        currentBp = start
        currentUrl = urlToCheck[0]
        urlToCheck = urlToCheck[1:]

    # Prevent out of bound recursion. Exit when done
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

shotQueue()
