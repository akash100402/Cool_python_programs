# install pywhatkit package 
# terminal command --> pip install pywhatkit

import pywhatkit as pwk

p = "+917539XXX711"  # Phone number along with country code
m = "hi bruh..."     # Message to send

pwk.sendwhatmsg(p, m, 10, 30)  # Sends the message at 10:30 AM

