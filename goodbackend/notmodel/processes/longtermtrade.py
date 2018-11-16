from notmodel.actor_folder.shared_methods import make_and_process_market_orders


import uuid

import numpy as np

class LongTermTrade:
	def __init__(self,t,trader,exchange):
		
		self.holder=trader
		
		exchange_state=exchange.get_state()
		
		inv_buy_price=float("%.3f"% exchange_state['sell_book'][0].price)
	
		self.inv_sell_price=inv_buy_price+inv_buy_price*trader.desired_roi
		
		make_and_process_market_orders(t,self.holder,exchange,self.holder.inv_amount,'buy')
		
		
		
		
	def advance_time(self,t,exchange):
		
		exchange_state=exchange.get_state()
		
		firstbuyprice=exchange_state['buy_book'][0].price
		
		if firstbuyprice>self.inv_sell_price:
		
			make_and_process_market_orders(t,self.holder,exchange,self.holder.inv_amount,'sell')
			self.holder.status=='free'
		
			
	