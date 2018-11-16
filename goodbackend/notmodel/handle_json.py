import os
import json
import gzip

import datetime

def updateStatus(t,config):

	os.makedirs(os.path.dirname('saveddata/'+config['simName']+'/cache.json'), exist_ok=True)
	
	computeTime=float(config['computeTime'])

	#print(t,cT)

	if int(t)==int(computeTime):
		ready=True
		# print('yes')
	else:
		ready=False



	with open('saveddata/'+config['simName']+'/cache.json', 'w') as outfile:
		json.dump({'status':t,'ready':ready,'computeTime':computeTime}, outfile)


def writetojson(data):

	
	with open("saveddata/"+data['simName']+"/bigdata.json", 'w') as outfile:
		json.dump(data, outfile)

	# with gzip.GzipFile("saveddata/"+data['simName']+"/bigdata.json", 'w') as fout:
		# fout.write(json.dumps(data).encode('utf-8'))

	print('data from simulation',data['simName']+'.json','saved to disk')
#	print()
#	print()


# def writecachetojson(data,now):


# 	with open('saveddata/'+now+'/cache.json', 'w') as outfile:
# 		json.dump(data, outfile)







def loadcache(folder):
	#pass
	with open('saveddata/'+folder+'/cache.json') as json_data:
		data = json.load(json_data)
    	
	return data



def loadsaveddata():
	
	contents=os.listdir('saveddata')
	
	
	print('saveddata folder:')
	for x in range(len(contents)):
		
		print(x,contents[x])
		
	
	
	filetoload=int(input('choose file to load '))
	
	file='saveddata/'+contents[filetoload]
	
	print(file)
	try:
		with open(file) as json_data:
			data = json.load(json_data)
	except json.decoder.JSONDecodeError:
		pass


	return data
	
	

	
	
	
