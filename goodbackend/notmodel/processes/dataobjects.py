
import uuid
import numpy as np

# from conf import *

#from actor_folder.shared_methods import make_and_process_market_orders
#import make_and_process_market_orders

class rawInquiry:
	
	def __init__(self,t,app_docs):

		self.uuid=uuid.uuid4()
		self.created_at=t
		self.app_docs=app_docs
		self.status='init'


class Order:
	
	def __init__(self,params):
		
		self.type=params['type']
		self.side=params['side']
		self.uuid=params['order_id']
		self.trader=params['trader']
		self.created_at=params['timestamp']
		self.quantity=float(params['quantity'])
		self.price=float(params['price'])



#		self.contract_clock+=1
#		print(self.holder.__dict__)
		
#		if self.total_returned==self.total_must_be_returned_to_close:
			
#			self.closecontract()
		
		
		#if self.payment_schedule[0]['paydate']==t:
		#	print(t,self.holder.name,'time for regular payment')
			
			### normal credit conract holder will drain wallet and make market orders
			### repour to returneand pop the first element of payment schedule
			
		#	if self.holder.return_strat['behavior']=='normal':
				
		#		print('self.payment_schedule 0')
				
		#		popped=self.payment_schedule.pop(0)
		#		print('popped')
		#		print(popped)
				
				
		#		self.holder.
				
		#		self.holder.drain_CRT(popped['monthly_payment'])
				
				
				
		#		input()
			
			
			
			#if self.holder.return_strat['behavior']=='will_scam':
			#	print(t,self.holder.name,' is scamming the regular payment')
				
				
			#elif self.holder.return_strat['behavior']=='will_delay_a_payment_for_20_days':
			#	print(t,self.holder.name,' is delaying this months payment for 20 days')
				
			#	print(self.paydays[0])
				
			#	self.paydays[0]=self.paydays[0]+20
				
			#	print(self.paydays[0])
				
				
				
				
				
			#	print()
			#	input()
				
				#self.payment_withheld+=1
				
				### adding fine
				
				#if self.payment_withheld==20:
				#	print(t,self.holder.name,' has successfully fucked up')
					
					###	paying the withheld payment
					#print(to_pay,'to_pay')
				#	print('')
				#	input()
					
					#to_pay=self.paydays.pop(0)
					
					#print(to_pay)
					
					
				#	self.payment_withheld=0
				
				
				
				### have to move payment day
				### and apply the fines for 20 days
				###
				
				
			
				
				
				#pass
			
			
		
		
			#print(self.holder.return_strat)
			
			
			#input()
		
		
		
		
		
		
		#if t
		
		
		
		
		#input()
	
	
#		self.violation=False
#		self.must_be_returned=credit_offer.will_return
#		self.credit_offer=credit_offer
#		self.money_taken=credit_offer.money_taken
#		self.overdue_fine=credit_offer.daily_overdue_fine
#		self.overdue_counter=0



#		self.overdue_money=0
#		self.credit_period=credit_offer.credit_period
		### 7 percet of contracts will not be returned
		### 20 percent will delay for 20 days and return afterwards
		
		
		
#		self.credit_behavior=np.random.choice(choices, p=probs)











