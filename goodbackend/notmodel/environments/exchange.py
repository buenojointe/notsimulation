from prettytable import PrettyTable

from notmodel.environments.shared_methods import Levels

class Exchange():
	def __init__(self,marketmaker,bank,incoming_config):
		self.name='Exchange'
		self.role='exchange'
		#config=gl_conf.model['environments']['exchange']['variant_one'] ### can distribute here
	
		self.levels=Levels({'start_level_CRT':0,'start_level_USDT':5000})
		self.levels_history=[]
		
		self.buy_book=[]
		self.sell_book=[]
		
		self.tokenBuyPriceHistory=[]
		self.tokenSellPriceHistory=[]
		
		#self.commission_stake=gl_conf.model['environments']['exchange']['variant_one']['commission_on_trades']
		self.commission_stake=incoming_config['exchangeComission']
		
		# self.intersected_orders=[]
		# self.intersected_orders_counter=[]
		
		# self.token_price_history_buy=[]
		# self.token_price_history_sell=[]
		
		# self.buy_book_liquidity=[]
		# self.sell_book_liquidity=[]
		
		# self.buy_trades_history=[]
		# self.buy_trades_history_counter=[]
		# self.sell_trades_history=[]
		# self.sell_trades_history_counter=[]
		
		# self.intersected_trades=[]
		# self.intersected_trades_counter=[]
		
		# self.balance_crt_history=[]
		# self.balance_usdt_history=[]

		# self.spread_history=[]
		self.volume_USDT=0

		marketmaker.initiate_manipulation(self,bank)

		self.mmIncome=[]
		self.mmIncome_counter=0

		# self.mm_income_cumu=[]
		# self.mm_income_cumu_counter=0
		# #=[]
		
		#self.mm_income_counter=0
		
	def take_snapshot(self):
		
		state=self.get_state()

		self.tokenBuyPriceHistory.append(state['buy_book'][0].price)
		self.tokenSellPriceHistory.append(state['sell_book'][0].price)

		self.mmIncome.append(self.mmIncome_counter)
		# self.mm_income_cumu.append(self.mm_income_cumu_counter)

		# self.mm_income.append(self.mm_income_counter)
		# self.mm_income_counter=0
		
		# self.intersected_orders.append(len(self.intersected_orders_counter))
		# self.intersected_orders_counter=[]
		
		# state=self.get_state()

		# try:
		# 	self.token_price_history_buy.append(state['buy_book'][0].price)
		# except IndexError:
		# 	self.token_price_history_buy.append(0)


		# self.token_price_history_sell.append(state['sell_book'][0].price)

		# self.balance_crt_history.append(self.levels.balance_CRT)
		# self.balance_usdt_history.append(self.levels.balance_USDT)

		# try:
		# 	self.spread_history.append(state['sell_book'][0].price-state['buy_book'][0].price)
		# except IndexError:
		# 	self.spread_history.append(0)
		# #buy_book=[]
		# summofbuybook=0
		
		# for x in range(len(self.buy_book)):
		# #	buy_book.append(self.buy_book[x].__dict__)
		# 	summofbuybook+=self.buy_book[x].quantity
		
		# #sell_book=[]
		# summofsellbook=0
		
		# for x in range(len(self.sell_book)):
		# #	sell_book.append(self.sell_book[x].__dict__)
		# 	summofsellbook+=self.sell_book[x].quantity
		
		# self.buy_book_liquidity.append(summofbuybook)
		# self.sell_book_liquidity.append(summofsellbook)

		# self.buy_trades_history.append(len(self.buy_trades_history_counter))
		# self.buy_trades_history_counter=[]

		# self.sell_trades_history.append(len(self.sell_trades_history_counter))
		# self.sell_trades_history_counter=[]

		# self.intersected_trades.append(len(self.intersected_trades_counter))
		# self.intersected_trades_counter=[]
		
		
		
		
	def get_state(self):
		state={'buy_book':self.buy_book,'sell_book':self.sell_book}
		return state
	
	
	def process_order(self,t,order):
		
		### this function handles adding the order to the
		### respective order book and then starting the match engine
		
		### draining the money and pouring the comission
		
		### this function handles draining actor wallet with pouring commission to exchange
		### and incrementing len of open orders, buy or sell
		
		to_drain=order.quantity
		
		#if explicit==True:
		#	print(t,'processing order',order.uuid,order.side,to_drain,order.price)
		
		abs_commission=to_drain*float(self.commission_stake)
			
		if order.side=='sell':
			
			order.trader.wallet.drain_CRT(order.trader.name,to_drain)
			# order.trader.exchange_acc.open_sell_orders+=1
			
			#self.arrived_at_ex_BTC_counter+=orders[z].quantity
			# self.sell_trades_history_counter.append(order.__dict__)
			
			### comission is poured on exchange levels
			self.levels.pour_CRT(self.name,abs_commission)
	
			self.sell_book.append(order)
			
			
		elif order.side=='buy':
			
			order.trader.wallet.drain_USDT(order.trader.name,to_drain)
			order.trader.exchange_acc.open_buy_orders+=1
			
			#self.arrived_at_ex_USDT_counter+=orders[z].quantity
			# self.buy_trades_history_counter.append(order.__dict__)
			
			
			### comission is poured on exchange levels
			self.levels.pour_USDT(self.name,abs_commission)
			
			self.buy_book.append(order)
		
		self.match_drive(t)
		### order matching engine
		
	
	
	
	
	
	def match_drive(self,t):
		
		### this function matches the orders in books for an instance of time,
		### handles reducing and popping opposing orders, as well as pouring wallets
		x,y=0,0
		
		while True:
					
					# if freeze==True:
					#self.printOBs()

					self.buy_book = sorted(self.buy_book, key=lambda k: k.price)
					self.buy_book.reverse()
				
					self.sell_book = sorted(self.sell_book, key=lambda k: k.price)
				
					try:

						buy_order=self.buy_book[x]
						sell_order=self.sell_book[y]

						if buy_order.price>sell_order.price:

							#self.printOBs()
							#print('exchange has fucked up')
							#print('crashed')

							self.buy_book.pop(0)

							#input()
							#input()
							#exit()
						

						if buy_order.price==sell_order.price:
							
							# self.intersected_trades_counter.append('trade')
							# self.intersected_orders_counter.append('order')
							
							buyer_trader=self.buy_book[x].trader
							seller_homjak=self.sell_book[y].trader
							
							if buy_order.quantity==sell_order.quantity:
								
								usdt=float(sell_order.quantity)*float(sell_order.price)
								
								buyer_trader.wallet.pour_CRT(buyer_trader.name,buy_order.quantity)
								buyer_trader.exchange_acc.open_buy_orders-=1
								self.buy_book.pop(0)
								
								seller_homjak.wallet.pour_USDT(seller_homjak.name,usdt)

								if seller_homjak.role=='marketmaker':self.mmIncome_counter+=usdt

									# self.mm_income_counter+=usdt
									# self.mm_income_cumu_counter+=usdt

								self.volume_USDT+=usdt



								seller_homjak.exchange_acc.open_sell_orders-=1
								self.sell_book.pop(0)
								#if explicit==True:
								#	print('order have same amount, popping both sides order1:',buy_order.quantity,'order2:',sell_order.quantity)
								#print('order have same amount, popping both sides order1:',buyer_trader.name,'order2:',seller_homjak.name)
								
							
								
							elif buy_order.quantity>sell_order.quantity:
								
								delta=buy_order.quantity-sell_order.quantity
								
								###collateral
								delta=float("%.6f" % delta)
								
								#if delta==float(0):
								#	self.buy_book.pop(0)
								#	self.buy_book[x].trader.exchange_acc.open_buy_orders-=1
									
								

								
								self.buy_book[x].quantity=delta
								
								usdt=float(sell_order.quantity)*float(sell_order.price)
								
								seller_homjak.wallet.pour_USDT(seller_homjak.name,usdt)

								if seller_homjak.role=='marketmaker':self.mmIncome_counter+=usdt
									# self.mm_income_cumu_counter+=usdt


								self.volume_USDT+=usdt
								buyer_trader.wallet.pour_CRT(buyer_trader.name,buy_order.quantity)
								
								seller_homjak.exchange_acc.open_sell_orders-=1
								self.sell_book.pop(0)
								
								#if explicit==True:
								#	print('buy is more than sell, popping sell',sell_order.quantity)
								
								
							
							elif buy_order.quantity<sell_order.quantity:
								
								delta=sell_order.quantity-buy_order.quantity
								
								###collateral
								delta=float("%.6f" % delta)

								if delta<0.00000001:
									#print('amount correction')
									self.sell_book.pop(0)
									#delta=0.0001
									#quit()
								else:

									self.sell_book[y].quantity=delta
								
								usdt=float(buy_order.quantity)*float(sell_order.price)
								seller_homjak.wallet.pour_USDT(seller_homjak.name,usdt)

								if seller_homjak.role=='marketmaker':self.mmIncome_counter+=usdt
									
									# self.mm_income_cumu_counter+=usdt

								buyer_trader.wallet.pour_CRT(buyer_trader.name,sell_order.quantity)
								
								buyer_trader.exchange_acc.open_buy_orders-=1
								self.buy_book.pop(0)

								#if explicit==True:
								#	print('buy less than sell, popping buy:',sell_order.quantity)

						else:
							break

					except IndexError:

						#self.printOBs()
						break
						#pass
					#raise Exception('buy or sell book is now empty. probably a lendee ate liquidity')



	def printOBs(self):
		
		print()
		print('observing')
		
		table=PrettyTable(['buy_book_price','buy_book_quantity in tokens','trader'])
		for x in range(len(self.buy_book)):
			try:
				tra=str(self.buy_book[x].trader.role)+' '+str(self.buy_book[x].trader.uuid)
			except:
				tra=self.buy_book[x].trader
			table.add_row([self.buy_book[x].price,self.buy_book[x].quantity,tra])
		print(table)
		print(len(self.buy_book))
		print()
		table=PrettyTable(['sell_book_price','sell_book_quantity in tokens','trader'])
		for x in range(len(self.sell_book)):
			try:
				tra=str(self.sell_book[x].trader.role)+' '+str(self.sell_book[x].trader.uuid)
			except:
				tra=self.sell_book[x].trader
			table.add_row([self.sell_book[x].price,self.sell_book[x].quantity,tra])
		print(table)
		print(len(self.sell_book))
		print()
		#input()
	

		

