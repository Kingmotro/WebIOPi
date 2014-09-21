import webiopi
import subprocess
# import Serial driver
#from webiopi.devices.serial import Serial
text =''
# initialize Serial driver
subprocess.call(['rmmod', 'dvb_usb_rtl28xxu'])
proc = subprocess.Popen(["dump1090", "--interactive"], stdout=subprocess.PIPE)
def setup():
    webiopi.debug("Script with macros - Setup")

def loop():
  tmptext = proc.stdout.read()
  if tmptext != '':
      text = tmptext	

# this macro scales sensor value and returns it as percent string
@webiopi.macro
def getdump1090():
    return text 

