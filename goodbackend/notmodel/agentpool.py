
# from conf import *

from notmodel.actor_folder.lendee import Lendee
from notmodel.actor_folder.speculant import Speculant
from notmodel.actor_folder.marketmaker import MarketMaker
from notmodel.actor_folder.investor import Investor

import random

import multiprocessing as mp

def findEvents(t,eventSchedule):
	events=[]
	
	for x in range(len(eventSchedule)):
		if t==eventSchedule[x]['date']:
			events.append(eventSchedule[x])
			
	return events

def generateSchedule(incoming_config):
	
	mks=['mk1','mk2']

	eventlist=[]

	for y in range(len(mks)):

		delta=int(incoming_config[mks[y]+'endDate'])-int(incoming_config[mks[y]+'startDate'])

		lendeeInfluxPerDay=int(incoming_config[mks[y]+'LendeesLured'])/delta
		SpecInfluxPerDay=int(incoming_config[mks[y]+'SpeculantsLured'])/delta
		InvestorInfluxPerDay=int(incoming_config[mks[y]+'InvestorsLured'])/delta

		for x in range(int(incoming_config[mks[y]+'startDate']),int(incoming_config[mks[y]+'endDate'])):
			obj={}
			obj['date']=int(incoming_config[mks[y]+'startDate'])+x
			obj['type']='add'
			obj['lendees']=lendeeInfluxPerDay
			obj['specs']=SpecInfluxPerDay
			obj['investors']=InvestorInfluxPerDay

			eventlist.append(obj)

	return eventlist




class AgentPool:

	def __init__(self,bank,incoming_config):

		self.eventSchedule=generateSchedule(incoming_config)

		self.marketmaker=MarketMaker(incoming_config)
		

		self.incoming_config=incoming_config

		self.lendees=[]
		self.speculants=[]
		self.investors=[]

		self.agentQuantityLendees=[]
		self.agentQuantitySpecs=[]
		self.agentQuantityInvestors=[]


		self.agentActivityLendees=[]
		self.agentActivityLendees_counter=0
		
		self.agentActivitySpecs=[]
		self.agentActivitySpecs_counter=0

		self.agentActivityInvestors=[]
		self.agentActivityInvestors_counter=0

		self.marketingCost=[]
		self.marketingCost_counter=0

		# self.affiliatedInvestor=Investor(self.incoming_config)


		
	
	def cycle(self,t,bank,exchange):

		self.marketingCost.append(self.marketingCost_counter)


		self.agentQuantityLendees.append(len(self.lendees))
		self.agentQuantitySpecs.append(len(self.speculants))
		self.agentQuantityInvestors.append(len(self.investors))

		self.agentActivityLendees.append(self.agentActivityLendees_counter)
		self.agentActivitySpecs.append(self.agentActivitySpecs_counter)
		self.agentActivityInvestors.append(self.agentActivityInvestors_counter)

		self.agentActivityLendees_counter=0	    
		self.agentActivitySpecs_counter=0	    
		self.agentActivityInvestors_counter=0

		
		dates=[self.eventSchedule[x]['date'] for x in range(len(self.eventSchedule))]

		events=findEvents(t,self.eventSchedule)


		# print(events)
		# input()
		
		if events!=[]:
			for x in range(len(events)):
				event=events[x]
				if event['type']=='add':
					
					for y in range(int(event['lendees'])):
						self.lendees.append(Lendee(self.incoming_config))
						self.marketingCost_counter+=float(self.incoming_config['mk2LendeeCost'])

					for y in range(int(event['specs'])):
						self.speculants.append(Speculant(self.incoming_config))
						self.marketingCost_counter+=float(self.incoming_config['mk2SpeculantCost'])

					for y in range(int(event['investors'])):
						self.investors.append(Investor(self.incoming_config))
						self.marketingCost_counter+=float(self.incoming_config['mk2InvestorCost'])

		#print(events)
		#input()

		mixed_agents=self.lendees+self.speculants+self.investors
		random.shuffle(mixed_agents)
		
		actor_queue=[]
		
		for y in range(len(mixed_agents)):
			actor_queue.append(mixed_agents[y]) ### every other actor is the link to marketmaker
			actor_queue.append(self.marketmaker)
			
		actor_queue.reverse() ### for mm to be the first
		
		for y in range(len(actor_queue)):
			actor=actor_queue[y]
			actor.activate(t,bank,exchange,self)

		self.marketmaker.advanced_manipulate(t,exchange)

			
		
		
		
			
		
	