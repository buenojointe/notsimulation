
from conf import *

class Observer:
	
	def __init__(self):
		
		### to inquire for credit
		self.decided_tifc=[]
		self.decided_tifc_counter=[]
		
		### credit offer duh
		self.recieved_credit_offer=[]
		self.recieved_credit_offer_counter=[]
		
		### to deploy grid
		self.decided_tdg=[]
		self.decided_tdg_counter=[]
		
		self.contract_returning_normal=[]
		self.contract_returning_normal_counter=0
		
		self.contract_returning_scammed=[]
		self.contract_returning_scammed_counter=0
		
		self.contract_returning_delayed=[]
		self.contract_returning_delayed_counter=0
		
		self.decided_to_invest=[]
		self.decided_to_invest_counter=[]
		
		self.emitted_coins=[]
		self.emitted_coins_counter=0


		self.contract_returning_normal_count=[]
		self.contract_returning_will_scam_count=[]
		self.contract_returning_will_delay_count=[]

		self.contract_returning_normal_count_counter=0
		self.contract_returning_will_scam_count_counter=0
		self.contract_returning_will_delay_count_counter=0



	def take_snapshot(self):
		
		
		self.decided_tifc.append(len(self.decided_tifc_counter))
		self.decided_tifc_counter=[]
		
		self.recieved_credit_offer.append(len(self.recieved_credit_offer_counter))
		self.recieved_credit_offer_counter=[]
		
		self.decided_tdg.append(len(self.decided_tdg_counter))
		self.decided_tdg_counter=[]
		
		
		self.contract_returning_normal.append(self.contract_returning_normal_counter)
		#self.contract_returning_normal_counter=0
		
		self.contract_returning_scammed.append(self.contract_returning_scammed_counter)
		#self.contract_returning_will_scam_counter=0
		
		self.contract_returning_delayed.append(self.contract_returning_delayed_counter)
		#self.contract_returning_will_delay_counter=0
	
		self.emitted_coins.append(self.emitted_coins_counter)
		#self.emitted_coins_counter=0

		self.contract_returning_normal_count.append(self.contract_returning_normal_count_counter)
		self.contract_returning_will_scam_count.append(self.contract_returning_will_scam_count_counter)
		self.contract_returning_will_delay_count.append(self.contract_returning_will_delay_count_counter)

	
	