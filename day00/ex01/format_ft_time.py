import time
import datetime
#format specifier
"""
: format specifier introducer
, how will the number be separated (Thousand separator)
.2f number of fixed point after the dot
"""
seconds = "{:,.6f}".format(time.time())
scientific = "{:e}".format(time.time())
date = datetime.datetime.now()
print('Seconds since January 1, 1970: %s or %s in scientific notation' % (seconds, scientific ))


#%b textual month

print(date.strftime("%b %d %Y"))