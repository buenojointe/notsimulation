from agentpool import AgentPool

from environments.bank import Bank
from environments.exchange import Exchange

# from conf import *

import statistics


class World:
	def __init__(self,incoming_config):
		
		self.bank=Bank(self.observer,incoming_config)
		self.agentpool=AgentPool(self.observer,self.bank,incoming_config)
		
		self.exchange=Exchange(self.agentpool.marketmaker,self.observer,self.bank,incoming_config)
		
	def advance_plancktime(self,t):
		
		self.agentpool.cycle(t,self.bank,self.exchange)
		
		
		
	
	

		