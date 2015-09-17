'use strict';

// Requires
var system = require('system'),
  page = require('webpage').create();

// Check that we received the minimum required params
if (system.args.length <= 4) {
  console.log('Invalid amount of arguments provided');
  console.log('Usage:   phantomjs render.js url screenwidth screenheight outputpath.png');
  console.log('Example: phantomjs render.js http://example.com 320 480 screenshot/folder/image.png')
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
  breakPointWidth = system.args[2] || 800,
  breakPointHeight = system.args[3] || 600,
  outputPath = system.args[4],
  cookies = system.args[5] || false,
  userAgent = system.args[6] || false;

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

// Set some parameters
// TODO optional iphone / android user agent
page.viewportSize = { width: breakPointWidth, height: breakPointHeight };
//page.clipRect = { top: 0, left: 0, width: 1024, height: 768 };
page.open(url, function() {
  page.render(outputPath);
  console.log("Rendered: ", url, breakPointWidth+"w X "+breakPointHeight+"h");
  phantom.exit();
});
