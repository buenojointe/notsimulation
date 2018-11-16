from notmodel.actor_folder.shared_methods import Wallet
from notmodel.actor_folder.shared_methods import ExchangeAccount
#from actor_folder.shared_methods import BankAccount ### speculants dont need bank account
#from actor_folder.shared_methods import make_and_process_limit_order
#
from notmodel.processes.longtermtrade import LongTermTrade

import numpy as np


import uuid
import random

class Investor:
	
	def __init__(self,incoming_config):
		self.uuid=uuid.uuid4()
		self.name=random.choice(['A','B','C','D'])
		self.role='investor'
		
		
		#conf=gl_conf.model['agents']['investor_constants']
		
		self.wallet=Wallet({'start_balance_CRT':0,'start_balance_USDT':0})
		
		self.exchange_acc=ExchangeAccount({'max_buy_orders': 1,'max_sell_orders': 1})
		

		self.desired_roi=float(np.random.choice(incoming_config['investorDesiredROI'],p=incoming_config['investorDesiredROIProbs']))
		self.inv_amount=float(np.random.choice(incoming_config['investorAmounts'],p=incoming_config['investorAmountProbs']))
		
		# self.ptoi=incoming_config['investorActivity']
		self.ptoi=0.01
		
		self.status='free'
		
		self.balance_CRT_history=[]
		self.balance_USDT_history=[]
		
		
	def activate(self,t,bank,exchange,linkFromPool):

		
		
		
		# self.balance_CRT_history.append(self.wallet.balance_CRT)
		# self.balance_USDT_history.append(self.wallet.balance_USDT)
		
		
		if self.status=='free':
			self.status=np.random.choice(['decided_to_invest', 'free'], p=[self.ptoi, 1-self.ptoi])
		
		if self.status=='decided_to_invest':

			linkFromPool.agentActivityInvestors_counter+=1
			# observer.decided_to_invest_counter.append(self.__dict__)
			
			self.active_ltt=LongTermTrade(t,self,exchange)
			
			self.status='a_trade_is_active'
			
		if self.status=='a_trade_is_active':
			self.active_ltt.advance_time(t,exchange)
		
		
		
	