'use strict';

// Requires
var system = require('system'),
  page = require('webpage').create();

// Check that we received the minimum required params
if (system.args.length <= 3) {
  console.log('Invalid amount of arguments provided');
  console.log('Usage:   phantomjs render.js url screenwidth outputpath.png');
  console.log('Example: phantomjs render.js http://example.com 320 screenshot/folder/image.png')
  phantom.exit(1);
} 

// Put it all together
var url = system.args[1],
  breakPoint = system.args[2],
  outputPath = system.args[3],
  userAgent = system.args[4] || false;

// Determine width / height based on type of screen size
if (breakPoint < 800) {
  var breakPointHeight = (breakPoint * 1.5);
} else {
  var breakPointHeight = (breakPoint * 0.8);
}

// Set some parameters
// TODO optional iphone / android user agent
page.viewportSize = { width: breakPoint, height: breakPointHeight };
//page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };
page.open(url, function() {
  page.render(outputPath);
  console.log("Rendered: ", url, breakPoint+"w X "+breakPointHeight+"h");
  phantom.exit();
});
