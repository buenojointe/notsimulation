#from metrics import *
#from queue_processing import *
#from dataobjects import *
import requests
import json
from prettytable import PrettyTable
# from conf import *

#from techactors.emitter import *



class Levels:
	
	def __init__(self,config):
		
		### drain from emitter
		
		#observer.emitted_coins_counter+=config['start_level_CRT']
		
		self.balance_CRT=config['start_level_CRT']
		self.balance_USDT=config['start_level_USDT']
	
	
	
	def drain_CRT(self,name,much):
	#	bal_before=self.balance_CRT
		self.balance_CRT-=much
	#	bal_after=self.balance_CRT
		#if explicit==True:
		#	print(name,much,'CRT drained, before:',bal_before,'now:',bal_after)
	
	def pour_CRT(self,name,much):
	#	bal_before=self.balance_CRT
		self.balance_CRT+=much
	#	bal_after=self.balance_CRT
		#if explicit==True:
		#	print(name,much,'CRT poured, before:',bal_before,'now',bal_after)
	
	def drain_USDT(self,name,much):
	#	bal_before=self.balance_USDT
		self.balance_USDT-=-much
	#	bal_after=self.balance_USDT
		#if explicit==True:
		#	print(name,much,'USDT drained, before:',bal_before,'now',bal_after)
	
	def pour_USDT(self,name,much):
	#	bal_before=self.balance_USDT
		self.balance_USDT+=much
	#	bal_after=self.balance_USDT
		#if explicit==True:
		#	print(name,much,'USDT poured, before:',bal_before,'now',bal_after)








