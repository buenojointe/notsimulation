import uuid
import random
from notmodel.processes.dataobjects import Order
# from conf import *
import numpy as np


#from techactors.emitter import *



def make_and_process_market_orders(t,trader,exchange,amount_to_satiate,side):
	
	
	### when lendee gets credit he must sell his tokens thus satiate buy book with sell orders
	
	#if explicit==True:
	#	print('satiating ',side,' order book with',amount_to_satiate,'crt')
	amount_to_satiate=float(amount_to_satiate)
	amount_to_satiate_init_= float(amount_to_satiate)
	exchange_state=exchange.get_state()
	orders=[]
	satiated=0

	if side=='buy':
		book='sell_book'
	elif side=='sell':
		book='buy_book'

	summqua=0
	
	for z in range(len(exchange_state[book])):
		price=exchange_state[book][z].price
		quantity=exchange_state[book][z].quantity
		
		#price=float("%.8f" % price)
		#quantity=float("%.8f" % quantity)
		
		
		
		if quantity<amount_to_satiate:
			amount_to_satiate=amount_to_satiate-quantity
			
			order=Order({'type':'market',
			             'order_id':uuid.uuid4(),
			             'timestamp':t,
			             'trader':trader,
			             'side':side,
			             'quantity':quantity,
			             'price':price})

			summqua+=order.quantity
			orders.append(order)
		
		else:
			order=Order({'type':'market',
			             'order_id':uuid.uuid4(),
			             'timestamp':t,
			             'trader':trader,
			             'side':side,
			             'quantity':amount_to_satiate,
			             'price':price})

			summqua+=order.quantity
			orders.append(order)
			break


	if summqua==amount_to_satiate_init_:
		pass#print('orders have been formed correctly!',summqua,amount_to_satiate_init_)

	else:
		# print('niguuh dunn fucked it up!',summqua,amount_to_satiate_init_)
		# print('attempting to make a limit order')
		left=amount_to_satiate_init_-summqua
		# print()
		# print()

		order=Order({'type':'market',
					 'order_id':uuid.uuid4(),
					 'timestamp':t,
					 'trader':trader,
					 'side':side,
					 'quantity':left,
					 'price':price})

		orders.append(order)
		summqua+=order.quantity

		# print('double check')

		#if summqua==amount_to_satiate_init_:
		#	pass
		# 	print('orders have been formed double correctly!',summqua,amount_to_satiate_init_)
		# 	print(' you win')
	#	else:
	#		print('shit boi')
	#		input()

		#input()

		# if explicit==True:
		# 	print()
		# 	print()
		#
		# 	for z in range(len(orders)):
		# 		print(orders[z].side,orders[z].quantity,orders[z].price)
		#
		# 	print()
        #
        #
        # else:
        #
        #
        # print()
        # print()

	
	for z in range(len(orders)):
		exchange.process_order(t,orders[z])
		
		

def make_and_process_limit_order(t,trader,exchange,price,amount,side):
	
	
	#if side=='buy':
	to_drain=amount
		
		
	#elif side=='sell':
	#to_drain=int(amount)
	
	price=float("%.4f" % price)
		
	order=Order({'type':'limit',
	             'order_id':uuid.uuid4(),
	             'timestamp':t,
	             'trader':trader,
	             'side':side,
	             'quantity':to_drain,
	             'price':price})
		
	exchange.process_order(t,order)
	
	
class BankAccount:
	
	def __init__(self,config):
		
		lendeeCreditRanges=[config['lendeeCreditRanges'][x][0]+'-'+config['lendeeCreditRanges'][x][1] for x in range(len(config['lendeeCreditRanges']))]
		lendeeCreditProbabilities=config['lendeeCreditProbabilities']
		lendeeCreditProbabilities=[float(config['lendeeCreditProbabilities'][x]) for x in range(len(config['lendeeCreditProbabilities']))]

		randrange=np.random.choice(lendeeCreditRanges,p=lendeeCreditProbabilities)
		randrange=randrange.split('-')
		#print(randrange)
		self.credit_score=random.randint(int(randrange[0]),int(randrange[1]))
		
		#self.ptoic=gl_conf.model['agents']['lendee_constants']['variant_one']['starter_bank_config']['probability_to_inquire_credit']
		self.ptoic=0.01
		

class ExchangeAccount:
	
	def __init__(self,config):
		
		self.open_buy_orders=0
		self.open_sell_orders=0
		
		self.max_buy_orders=config['max_buy_orders']
		self.max_sell_orders=config['max_sell_orders']
		
		self.trade_history=[]


class Wallet:
	
	def __init__(self,config):
		# pass
		
		### drain from emitter
		# observer.emitted_coins_counter+=config['start_balance_CRT']
		
		# toemit=config['start_balance_CRT']
		
		# bank.emitTokens(toemit,roleofclaimer)
		
		self.balance_CRT=config['start_balance_CRT']
		self.balance_USDT=config['start_balance_USDT']
		
		
		
	def drain_CRT(self,name,much):
		#bal_before=self.balance_CRT
		self.balance_CRT-=much
		#bal_after=self.balance_CRT
		#if explicit==True:
		#	print(name, much,'CRT drained, before:',bal_before,'now:',bal_after)
		
	def pour_CRT(self,name,much):
		#bal_before=self.balance_CRT
		self.balance_CRT+=much
		#bal_after=self.balance_CRT
		#if explicit==True:
		#	print(name, much,'CRT poured, before:',bal_before,'now',bal_after)
		
	def drain_USDT(self,name,much):
		#bal_before=self.balance_USDT
		self.balance_USDT-=much
		#bal_after=self.balance_USDT
		#if explicit==True:
		#	print(name, much,'USDT drained, before:',bal_before,'now',bal_after)
		
	def pour_USDT(self,name,much):
		#bal_before=self.balance_USDT
		self.balance_USDT+=much
		#bal_after=self.balance_USDT
	#	if explicit==True:
	#		print(name, much,'USDT poured, before:',bal_before,'now',bal_after)