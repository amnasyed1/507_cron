import datetime
import random

currentdatetime = datetime.datetime.now()
print (currentdatetime)
datetimestring = str(currentdatetime)

output = f'the current date/time that this script was run happpened at: (datatimestring)'
print (output)

randonnumber = str(random.randint(0, 100000))

filename = f'cron_output_{randonnumber}'
with open('cron_stuff/output/' + filename, 'w') as f: 
       f.write(output)
    
## first open workspace as cron_stuff
## make output in a way where it looks like an upside down ^ next to output
