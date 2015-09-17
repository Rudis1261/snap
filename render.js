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

// http://stackoverflow.com/a/31847721/2080324
function hostname(url) {
  var match = url.match(/:\/\/(www[0-9]?\.)?(.[^/:]+)/i);
  if ( match != null && match.length > 2 && typeof match[2] === 'string' && match[2].length > 0 ) {
    return match[2];
  }
}

// Put it all together
var url = system.args[1],
  breakPoint = system.args[2],
  outputPath = system.args[3],
  cookies = system.args[4] || false,
  userAgent = system.args[5] || false;

// Allow cookies to be added
if (cookies){
  var cookieJar = JSON.parse(cookies);
  if (cookieJar) {
    var cookieKeys = Object.keys(cookieJar);
    cookieKeys.forEach(function(key){
      var cookieRecipe = {
          'name': key,
          'value': cookieJar[key],
          'domain': hostname(url)
      };
      if (!phantom.addCookie(cookieRecipe)) {
        console.log("Failed to set cookie, recipe:", JSON.stringify(cookieRecipe));
      }
    });
  }
}

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
