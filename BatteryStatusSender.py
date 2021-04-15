# python script showing battery details 
import psutil
import clx.xms
import requests

# function returning time in hh:mm:ss 
def convertTime(seconds): 
	minutes, seconds = divmod(seconds, 60) 
	hours, minutes = divmod(minutes, 60) 
	return "%d:%02d:%02d" % (hours, minutes, seconds) 

# returns a tuple 
battery = psutil.sensors_battery() 

print("Battery percentage : ", battery.percent) 
print("Power plugged in : ", battery.power_plugged) 

# converting seconds to hh:mm:ss 
print("Battery left : ", convertTime(battery.secsleft))


# Sends SMS

client = clx.xms.Client(service_plan_id='97ecb2c25dcd4177ae8c143e685b1764', token='79218b1625504412a2f2d5928d59deb9')

create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = 'Hello'
create.recipients = {'91 XXXX-XX-XXXX'}
create.body = "Hello Rajat  \n"+"Your Laptop's \U0001f50b : "+str(battery.percent)+"%"+"\nHours Left \u231A :"\
              +str(convertTime(battery.secsleft))+"\n\U0001f64f Thanks "

try:
  batch = client.create_batch(create)
except (requests.exceptions.RequestException,
  clx.xms.exceptions.ApiException) as ex:
  print('Failed to communicate with XMS: %s' % str(ex))
