from notmodel.actor_folder.shared_methods import Wallet
from notmodel.actor_folder.shared_methods import ExchangeAccount
#from actor_folder.shared_methods import BankAccount ### speculants dont need bank account
from notmodel.actor_folder.shared_methods import make_and_process_limit_order
from notmodel.actor_folder.shared_methods import make_and_process_market_orders

import numpy as np


import uuid
import random

class Speculant:
	
	def __init__(self,incoming_config):
		self.uuid=uuid.uuid4()
		self.name=random.choice(['White','Blue','Red','Green','Pink','Black','Yellow','Orange','Cyan'])
		self.role='speculant'

		self.wallet=Wallet({'start_balance_CRT':0,'start_balance_USDT':5000})
		self.exchange_acc=ExchangeAccount({'max_buy_orders': 1,'max_sell_orders': 1})
		self.status='free'
		# self.ptdg=incoming_config['speculantActivity']
		self.ptdg=0.01

		self.trade_strat={} #random.choice()
		# print(incoming_config['specPriceDeviations'])

		# input()
		incoming_config['specPriceDeviations']=[float(incoming_config['specPriceDeviations'][x]) for x in range(len(incoming_config['specPriceDeviations']))]
		incoming_config['specPriceDeviationsProbs']=[float(incoming_config['specPriceDeviationsProbs'][x]) for x in range(len(incoming_config['specPriceDeviationsProbs']))]
		incoming_config['specAmounts']=[float(incoming_config['specAmounts'][x]) for x in range(len(incoming_config['specAmounts']))]
		incoming_config['specAmountProbs']=[float(incoming_config['specAmountProbs'][x]) for x in range(len(incoming_config['specAmountProbs']))]



		self.trade_strat['price_deviation']=np.random.choice(incoming_config['specPriceDeviations'],p=incoming_config['specPriceDeviationsProbs'])
		self.trade_strat['trade_amount']=np.random.choice(incoming_config['specAmounts'],p=incoming_config['specAmountProbs'])
		# input()
		self.balance_CRT_history=[]
		self.balance_USDT_history=[]
		
		
	def activate(self,t,bank,exchange,linkFromPool):

		
		
		# self.balance_CRT_history.append(self.wallet.balance_CRT)
		# self.balance_USDT_history.append(self.wallet.balance_USDT)
		
		if self.status=='free':
			self.status=np.random.choice(['decided_to_deploy_grid', 'free'],p=[self.ptdg, 1-self.ptdg])
		
		if self.status=='decided_to_deploy_grid':

			# linkFromPool.agentActivitySpecs_counter+=1
			
			
			exchange_state=exchange.get_state()
			
			
		
			firstbuy= float("%.3f"% exchange_state['buy_book'][0].price)
			firstsell= float("%.3f"% exchange_state['sell_book'][0].price)
			
			border_price=(firstbuy+firstsell)/2
			
			price_deviation=self.trade_strat['price_deviation']
			amount=self.trade_strat['trade_amount']
			
			
			for y in range(self.exchange_acc.max_sell_orders+self.exchange_acc.max_buy_orders):
				
				if self.exchange_acc.open_buy_orders<self.exchange_acc.max_buy_orders:
					
					#deviated_buy=border_price-border_price*price_deviation
					deviated_buy=border_price-price_deviation
					
					deviated_buy=float("%.3f"% deviated_buy)
				
				
					if self.wallet.balance_USDT>amount:
						# print('hi')
						linkFromPool.agentActivitySpecs_counter+=1
					
						if deviated_buy<firstsell:
						
							make_and_process_limit_order(t,self,exchange,deviated_buy,amount,'buy')
						
						else:
							
							make_and_process_market_orders(t,self,exchange,amount,'buy')
							

				if self.exchange_acc.open_sell_orders<self.exchange_acc.max_sell_orders:
					
					#deviated_sell=border_price+border_price*price_deviation
					deviated_sell=border_price+price_deviation
					
					deviated_sell=float("%.3f"% deviated_sell)
				
				
					if self.wallet.balance_CRT>amount:
						# print('hi')
						linkFromPool.agentActivitySpecs_counter+=1
				
					
						if deviated_sell>firstbuy:
					
					
							make_and_process_limit_order(t,self,exchange,deviated_sell,amount,'sell')
		
						else:
						
							make_and_process_market_orders(t,self,exchange,amount,'sell')
	