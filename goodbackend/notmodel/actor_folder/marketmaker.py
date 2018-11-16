from notmodel.actor_folder.shared_methods import Wallet
from notmodel.actor_folder.shared_methods import ExchangeAccount
# from actor_folder.shared_methods import BankAccount ## market maker does not interact with bank
from notmodel.actor_folder.shared_methods import make_and_process_limit_order

from notmodel.actor_folder.shared_methods import make_and_process_market_orders

from notmodel.processes.dataobjects import Order


import uuid
import random


class MarketMaker:
	
	def __init__(self,incoming_config):
		
		self.uuid=uuid.uuid4()
		self.name=random.choice(['FDA','NRA','SEC'])
		self.role='marketmaker'

		self.wallet=Wallet({'start_balance_CRT':0,'start_balance_USDT':0})
		self.exchange_acc=ExchangeAccount({'max_buy_orders': 20,'max_sell_orders': 20})
		#self.bank_acc=BankAccount(config['starter_bank_config'])  ### marketmaker does not interact wth bank

		self.status='free'
		self.climb_rate=incoming_config['mmClimbRate']
		self.price_to_manipulate=float(incoming_config['mmPriceToManipulate'])

		self.history_usdt=[]

		self.history_crt=[]

		self.amount_base=incoming_config['mmAmountBase']


		self.mmDeviation=float(incoming_config['mmDeviation'])
		self.mmLiqThresh=incoming_config['mmLiqThresh']

		
		

		self.wastedUsdt=[]
		self.wastedTokens=[]

		self.wastedUsdt_counter=0
		self.wastedTokens_counter=0


		#self.history_usdt_iter=[]




	def initiate_manipulation(self,exchange,bank):

		price_to_manipulate=float(self.price_to_manipulate)
		amount_base=self.amount_base
		
		sides=['buy','sell']
		
		for hau in range(len(sides)):
		
			side=sides[hau]
			
			if side=='buy':
				price=price_to_manipulate-(1/100)
		
			elif side=='sell':
				price=price_to_manipulate+(1/100)
	
			amount=2*amount_base

			
			order=Order({'type':'market',
				        'order_id':uuid.uuid4(),
				        'timestamp':0,
				        'trader':self,
				        'side':side,
				        'quantity':int(amount),
				        'price':price})
			
			if side=='buy':
				## withdrawrfom balance
				# self.wasted_usdt_counter+=amount
				#bank.lend_usdt_to_mm(amount)
				#self.wallet.pour_USDT('bank',amount)
				exchange.buy_book.append(order)
	
			elif side=='sell':
				
				#bank.emitTokens(amount,'marketmaker')
				#self.wallet.pour_CRT('bank',amount)
				exchange.sell_book.append(order)

	
	def advanced_manipulate(self,t,exchange):

		# self.history_usdt.append(self.wallet.balance_USDT)
		# self.history_crt.append(self.wallet.balance_CRT)

		# self.wasted_usdt.append(self.wasted_usdt_counter)


		
		self.price_to_manipulate=float(self.price_to_manipulate)+float(self.climb_rate)

		# print('self.price_to_manipulate')
		# print(self.price_to_manipulate)
		
		orders_to_mirror=[]
		
		for x in range(len(exchange.sell_book)):
			
			if exchange.sell_book[x].price<=self.price_to_manipulate:
				obj={'price':exchange.sell_book[x].price,'quantity':exchange.sell_book[x].quantity}
				orders_to_mirror.append(obj)
			
			
		for x in range(len(orders_to_mirror)):
			
			price=orders_to_mirror[x]['price']
			amount=orders_to_mirror[x]['quantity']
			
			make_and_process_market_orders(t,self,exchange,amount,'buy')
			#make_and_process_limit_order(t,self,exchange,price,amount,'buy')

		
			
	
	def activate(self,t,bank,exchange,linkFromPool):
		### regular market monitorings
		### if some book liquidity gets lower than threshold mm adds orders
		
		self.wastedUsdt.append(self.wastedUsdt_counter)
		self.wastedTokens.append(self.wastedTokens_counter)

		# self.wastedUsdt_counter=0
		# self.wastedTokens_counter=0


		liquidity_threshold=float(self.mmLiqThresh)
		price_to_manipulate=float(self.price_to_manipulate)
		
		amount_base=self.amount_base

		price_deviation_step=self.mmDeviation
		
		sides=['buy','sell']
		
		for hau in range(len(sides)):
			side=sides[hau]
			
			n=0
			
			while True:
				n+=1
				
				exchange_state=exchange.get_state()
				state=exchange_state[side+'_book']

				# print('state')
								
				
				summ_of_book=0
				
				for z in range(len(state)):
					summ_of_book+=state[z].quantity
					
				if summ_of_book<liquidity_threshold:
					
					# if explicit==True:
						# print('market maker is attempting to restore OB')
						# print('market maker rolling out, OB are', summ_of_book, side)
						# print()

					
					

					if side=='buy':
						
						price=price_to_manipulate-(n*price_deviation_step)
						try:
							firstopposite=exchange_state['sell_book'][0].price
						except IndexError:
							firstopposite=self.price_to_manipulate
						
						# print('debug')
						# print(firstopposite)


						if firstopposite<price:
							price=firstopposite
						
					elif side=='sell':
						price=price_to_manipulate+(n*price_deviation_step)
						firstopposite=exchange_state['buy_book'][0].price
						
					
						if firstopposite>price:
							price=firstopposite
				
				
					amount=n*amount_base
					
					if side=='sell':
						self.wastedTokens_counter+=float(amount)
						# bank.emitTokens(amount,'marketmaker')

					elif side=='buy':
						# pass
						self.wastedUsdt_counter+=float(amount)

						# self.wasted_usdt_counter+=amount
						# bank.lend_usdt_to_mm(amount)


					make_and_process_limit_order(t,self,exchange,price,amount,side)
					
					
				else:
					#print (t,side,'book liquidity restored by marketmaker',summ_of_book)
					#input()
					break
		
		
		
		
		
		
		
		
		
		
		


