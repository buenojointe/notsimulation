from notmodel.actor_folder.shared_methods import Wallet
from notmodel.actor_folder.shared_methods import ExchangeAccount
from notmodel.actor_folder.shared_methods import BankAccount


from notmodel.processes.contract import Contract
from notmodel.actor_folder.shared_methods import make_and_process_market_orders

import uuid
import random
import numpy as np

from notmodel.processes.dataobjects import rawInquiry



class Lendee:
	
	def __init__(self,incoming_config):
		self.uuid=str(uuid.uuid4())
		self.name=random.choice(['Sophia','Jacob','Isabella','Mason','Emma','William','Olivia','Jayden','Nathan'])
		self.role='lendee'
		self.wallet=Wallet({'start_balance_CRT':0,'start_balance_USDT':5000})
		self.exchange_acc=ExchangeAccount({'max_buy_orders': 1,'max_sell_orders': 1})
		self.bank_acc=BankAccount(incoming_config)
		self.status='free'
		self.balance_CRT_history=[]
		self.balance_USDT_history=[]
		self.inqsums=incoming_config['lendeeInquirySums']
		self.inqsumprob=incoming_config['lendeeInquiryProbabilities']
		self.incoming_config=incoming_config


	def activate(self,t,bank,exchange,linkFromPool):
		
		

		# self.balance_CRT_history.append(self.wallet.balance_CRT)
		# self.balance_USDT_history.append(self.wallet.balance_USDT)
		
		if self.status=='free':
			self.status=np.random.choice(['decided_to_inquire_for_credit', 'free'],p=[self.bank_acc.ptoic, 1-self.bank_acc.ptoic])
			
		if self.status=='decided_to_inquire_for_credit':

			# print('hi')
			
			linkFromPool.agentActivityLendees_counter+=1
			# print(linkFromPool.agentActivityLendees_counter,'hi')
			# observer.decided_tifc_counter.append(self.__dict__)
			
			#if explicit==True:
			#	print(t,self.name,self.role,'has',self.status)
			
			### decide credit amount

			newquire=np.random.choice(self.inqsums,p=self.inqsumprob)
			will_inquire=newquire ### try to round the amount
			credit_score=self.bank_acc.credit_score
			
			application_documents= {'applicant_name':self.name,
			                        # 'balance_CRT':self.wallet.balance_CRT,
			                        # 'balance_USDT':self.wallet.balance_USDT,
			                        'will_incquire_credit_crt':will_inquire,
			                        'credit_score':credit_score}
			
			### a returned credit contract means that the bank is ready to serve the credit via card, for example
			### now the lendee initiates the contract by attempting to use the frozen funds
			### the bank counts the global stats
			
			rawinquiry=rawInquiry(t,application_documents)
			contract=bank.process_raw_inquiry(t,rawinquiry,self,self.incoming_config)
			
			self.active_contract=contract
			
			#if explicit==True:
	#		print(t,self.name, 'has recieved raw contract and has initiated',contract.uuid)
			self.status='a_contract_is_active'
			
			### contract init handles pouring from credit card to wallet
			### lendee now has to market sell crt
			amount_to_satiate=will_inquire
			## selling tokens

			## previously we were make only market order and thus the OB crashed,
			## now we will view the xchange and make limit orders

			make_and_process_market_orders(t,self,exchange,amount_to_satiate,'sell')

			
		if self.status=='a_contract_is_active':
			
			self.active_contract.advance_time(t,bank,exchange)
			
