import time
from datetime import datetime

this_day = time.time()
today = datetime.now()
print(f'Seconds since January 1, 1970: {this_day:,.4f} or {this_day:.2e} in scientific notation')
print(today.strftime("%b %d %Y"))
