import sys
import webbrowser
#import pyperclip

if len(sys.argv)>2:
    address=' '.join(sys.argv[2:])
#else:
#    address=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+address)
