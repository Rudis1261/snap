# Snap *Linux

#### Another screenshot application. 

I know there are applications out there which already do something like this, but in the past when I have tried using those I found them cumbersome and often riddled with issues. 

## The Goal of this project
* This is my take on this type of thing. 
* Build multiple URLs, at multiple resolutions, at the same time. 
* Then serve the results in a easy to interpret way.

## Prerequisites
You will need to have **python** and **npm** (Node Package Manager) installed before you will be able to use this 

## Installation:
```shell
git clone git@github.com:drpain/snap.git
cd snap
sudo chmod +x install.sh start.py
./install.sh
```

## USAGE:
* Run the script with the URL's you want to test, separated by spaces

```shell
./start.py http://www.google.com http://www.example.com
```

And keep an eye on the screenshots folder for your newly created, crisp images.

### Example output
```shell
rudis1261@TheCracken:~/GitHub/snap$ ./start.py 
Starting Snap
Starting individual processes of PhantomJS to handle each breakpoint
Queued Screenshot FOR: http://example.com SIZE: 320
Queued Screenshot FOR: http://example.com SIZE: 480
Queued Screenshot FOR: http://example.com SIZE: 768
Queued Screenshot FOR: http://example.com SIZE: 992
Queued Screenshot FOR: http://example.com SIZE: 1200
Queued Screenshot FOR: http://www.google.co.za SIZE: 320
Queued Screenshot FOR: http://www.google.co.za SIZE: 480
Queued Screenshot FOR: http://www.google.co.za SIZE: 768
Queued Screenshot FOR: http://www.google.co.za SIZE: 992
Queued Screenshot FOR: http://www.google.co.za SIZE: 1200
Queued, awaiting response
rudis1261@TheCracken:~/GitHub/snap$ Rendered:  http://example.com 480w X720h
Rendered:  http://example.com 320w X480h
Rendered:  http://example.com 992w X793.6h
Rendered:  http://example.com 1200w X960h
Rendered:  http://example.com 768w X1152h
Rendered:  http://www.google.co.za 480w X720h
Rendered:  http://www.google.co.za 1200w X960h
Rendered:  http://www.google.co.za 768w X1152h
Rendered:  http://www.google.co.za 320w X480h
Rendered:  http://www.google.co.za 992w X793.6h
```

## TODOS
These are things I still need TODO to consider this usable

* Document everything! - Maybe never :-D
* Create a web-interface to serve the images - In Progress
