from datetime import *

today = datetime.today()
print(today)
for attr in ['year','month','day','hour','minute','second','microsecond']:
    print(attr, ' :\t ',getattr(today,attr))
print('=====================================================================')
month = today.strftime('%B')
print('Full Month is : ',month)