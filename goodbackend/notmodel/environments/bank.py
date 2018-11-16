from notmodel.environments.shared_methods import Levels

from notmodel.processes.contract import Contract

from notmodel.actor_folder.shared_methods import ExchangeAccount

# from actor_folder.shared_methods import ExchangeAccount


import random
# from conf import *

def debuildBankProducts(incoming_config):

	credit_categories=[]

	bankScoreRanges=incoming_config['bankScoreRanges']
	bankCreditInterests=incoming_config['bankCreditInterests']
	bankCreditPeriods=incoming_config['bankCreditPeriods']
	bankDailyFines=incoming_config['bankDailyFines']

	for x in range(len(bankScoreRanges)):

		obj={}
		obj['cred_range']=[bankScoreRanges[x][0],bankScoreRanges[x][1]]
		obj['30_day_interest_rate']=bankCreditInterests[x]
		obj['period']=bankCreditPeriods[x]
		obj['daily_overdue_fine']=bankDailyFines[x]

		credit_categories.append(obj)

	return credit_categories




class Bank:
	
	def __init__(self,incoming_config):

		self.name='Cryptobank'
		self.role='bank'
		
		self.wallet=Levels({'start_level_CRT':0,'start_level_USDT':0})
		
		self.level_crt_history=[]
		self.level_usdt_history=[]
		self.exchange_acc=ExchangeAccount({'max_buy_orders':1,'max_sell_orders':1})
		self.creditProducts=debuildBankProducts(incoming_config)

		self.contractsInitiatedHistory=[]
		self.contractsInitiatedPerDay=[]
		self.contractsInitiatedHistory_counter=0
		self.contractsInitiatedPerDay_counter=0

		# self.credit_offer_issued=[]
		# self.credit_offer_issued_counter=[]
		
		self.bankTotalLended=[]
		self.bankTotalLended_counter=0

		self.bankTotalReturned=[]
		self.bankTotalReturned_counter=0
		
		
		# self.contracts_initiated=[]
		# self.contracts_initiated_counter=[]
		
		# #self.emission_lendees=0
		# #self.emission_speculants=0
		# #self.emission_marketmaker=0
		
		# self.emission_lendees_history=[]
		# self.emission_lendees_counter=0
		
		# self.emission_speculants_history=[]
		# self.emission_speculants_counter=0
		
		# self.emission_marketmaker_history=[]
		# self.emission_marketmaker_counter=0

		# self.lended_to_mm=[]
		# self.lended_to_mm_counter=0

	
	
	
	def take_snapshot(self):

		self.bankTotalLended.append(self.bankTotalLended_counter)
		self.bankTotalReturned.append(self.bankTotalReturned_counter)

		# self.contractsInitiatedHistory_counter=0
		# self.contractsInitiatedPerDay+=self.contractsInitiatedHistory_counter
		
		
		self.contractsInitiatedPerDay.append(self.contractsInitiatedPerDay_counter)
		self.contractsInitiatedHistory.append(self.contractsInitiatedHistory_counter)

		self.contractsInitiatedPerDay_counter=0
		# self.contractsInitiatedHistory_counter=0






		# self.total_lended.append(float(self.total_lended_counter))
		# self.total_returned.append(float(self.total_returned_counter))
		
		# print(self.contractsInitiatedHistory,'snap')
		
		# self.contractsInitiatedPerDay=[]
		# pass### advance time
		
		# self.credit_offer_issued.append(len(self.credit_offer_issued_counter))
		# self.credit_offer_issued_counter=[]
		
		# self.level_crt_history.append((float(self.wallet.balance_CRT)))
		# self.level_usdt_history.append((float(self.wallet.balance_USDT)))
		
		
		# self.contracts_initiated.append(len(self.contracts_initiated_counter))
		# self.contracts_initiated_counter=[]
	
		# self.emission_lendees_history.append(float(self.emission_lendees_counter))
		# self.emission_speculants_history.append(float(self.emission_speculants_counter))
		# self.emission_marketmaker_history.append(float((self.emission_marketmaker_counter)))

		# self.lended_to_mm.append(float(self.lended_to_mm_counter))
		# self.lended_to_mm_counter=0


	
	
	
	def emitTokens(self,toemit,role):
		
		
		#if role=='lendee':
		#	self.emission_lendees_counter+=toemit
		
		if role=='speculant':
			self.emission_speculants_counter+=toemit
			
		elif role=='marketmaker':
			
			#print(self.emission_marketmaker_counter,'self.emission_marketmaker_counter')
			#input()
			self.emission_marketmaker_counter+=toemit

	def lend_usdt_to_mm(self,amount):

		self.lended_to_mm_counter+=amount
		self.wallet.drain_USDT('bank',amount)






	
	def process_raw_inquiry(self,t,inq,inqauthor,incoming_config):
		
		# print('processing raw inquiry inqauthor',self.contractsInitiatedPerDay)
		self.contractsInitiatedHistory_counter+=1
		self.contractsInitiatedPerDay_counter+=1
		
		
		score=inq.app_docs['credit_score']
		amount=float(inq.app_docs['will_incquire_credit_crt'])
		
		for hau in range(len(self.creditProducts)):
		
			line=self.creditProducts[hau]
			the_range=line['cred_range']
			interest=float(line['30_day_interest_rate'])
			period=float(line['period'])
			fine=float(line['daily_overdue_fine'])

			if float(the_range[0]) <= score <= float(the_range[1]):
				#	print('bank has found a product for lendee')
				break
				
		### forming credit offer parameters for annuitate payments
		
		months=period/30

		totalfinalpayment=months*interest*amount+amount

		monthlypayment=totalfinalpayment/months
		
		self.bankTotalLended_counter+=amount
		
		### draining banks money for creditoffer
		
		self.wallet.drain_CRT(self.name,amount)
		
		parameters={'score':score,
		            'unlocked':amount,
		            'interest':interest,
		            'months':months,
		            'monthlypayment':monthlypayment,
		            'totalfinalpayment':totalfinalpayment,
		            'fine':fine}
				
		inq.status='approved'
		
	
		contract=Contract(t,parameters,inqauthor,incoming_config)

		
		return contract
	