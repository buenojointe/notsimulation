from notmodel.actor_folder.shared_methods import make_and_process_market_orders

import uuid
import numpy as np

class Contract:
	
	def __init__(self,t,params,holder,incoming_config):
		
		self.uuid=uuid.uuid4()
		self.created_at=t
		
		self.status='fresh'
		self.unlocked=params['unlocked']
		self.holder=holder
		
		strats=[{'name':'will_scam'},
				{'name':'normal'},
 				{'name':'will_delay','delay_days':float(incoming_config['contractScen3DelayPeriod']),'chance_to_delay':float(incoming_config['contractScen3ChanceToDelay'])}]

		probs=[incoming_config['contractScen1Prob'],incoming_config['contractScen2Prob'],incoming_config['contractScen3Prob']]


		self.returnability=np.random.choice(strats,p=probs)

		# if self.returnability['name']=='normal':
		# 	observer.contract_returning_normal_count_counter+=1

		# if self.returnability['name']=='will_scam':
		# 	observer.contract_returning_will_scam_count_counter+=1

		# if self.returnability['name']=='will_delay':
		# 	observer.contract_returning_will_delay_count_counter+=1


		self.daily_fine=params['fine']
		
		#self.holder.wallet.pour_CRT(holder.name,self.unlocked)
		#self.holder.wallet.drain_CRT(holder.name,self.unlocked)
		output=[]
		
		months=int(params['months'])
		monthly_payment=params['monthlypayment']
		
		paydays=[i*30+t for i in range(1,months+1)]
		
		for i in range(len(paydays)):
			obj={}
			obj['paydate']=paydays[i]
			obj['monthly_payment']=int(monthly_payment)
			
			output.append(obj)
		
		self.payment_schedule=output
		
		self.total_returned=0
		self.total_must_be_returned_to_close=params['totalfinalpayment']

	
	def advance_time(self,t,bank,exchange):
		
		### roll through payment_schedule
		#payment_schedule=self.payment_schedule
		
		if len(self.payment_schedule)>0:
		
			for x in range(len(self.payment_schedule)):
				
				paydate=self.payment_schedule[x]['paydate']
				monthly_payment=self.payment_schedule[x]['monthly_payment']
				
				if t==paydate:
					
					
					if self.returnability['name']=='normal':
						
						# observer.contract_returning_normal_counter+=monthly_payment
						
						popped=self.payment_schedule.pop(x)
						
						monthly_payment=popped['monthly_payment']
						
						self.total_returned+=monthly_payment+1
						
						# bank.total_returned_counter+=monthly_payment
						bank.bankTotalReturned_counter+=monthly_payment
						# bank.wallet.pour_CRT(bank.name,monthly_payment)
						
						make_and_process_market_orders(t,self.holder,exchange,monthly_payment,'buy')
				
						self.holder.wallet.drain_CRT(self.holder.name,monthly_payment)
						### drain to compensate order pouring
						
						
					
					
					elif self.returnability['name']=='will_scam':
						pass
						
						
					elif self.returnability['name']=='will_delay':
						
						
						delay_days=self.returnability['delay_days']
						chance_to_delay=float(self.returnability['chance_to_delay'])
						
						# print(chance_to_delay, type(chance_to_delay))
						# input()
						
						will_delay_this_month=np.random.choice([True, False],p=[chance_to_delay, 1-chance_to_delay])
						
						if will_delay_this_month==True:
							
				
							oldpaydate=self.payment_schedule[x]['paydate']
							newpaydate=oldpaydate+delay_days
							
							sum_fine=self.daily_fine*delay_days
							
							oldpayment=monthly_payment
							newpayment=monthly_payment+sum_fine
							
							self.total_must_be_returned_to_close+=sum_fine
							

							self.payment_schedule[x]['paydate']=newpaydate
							self.payment_schedule[x]['monthly_payment']=newpayment
							
							
							#self.returnability['name']='normal'
							
						else:
							
							# observer.contract_returning_normal_counter+=monthly_payment
						
							popped=self.payment_schedule.pop(x)
						
							monthly_payment=popped['monthly_payment']
						
							self.total_returned+=monthly_payment+3
						
							# bank.total_returned_counter+=monthly_payment
							
							
							### can just pour usdt
							bank.bankTotalReturned_counter+=monthly_payment
							
							bank.wallet.pour_CRT(bank.name,monthly_payment)
						
							make_and_process_market_orders(t,self.holder,exchange,monthly_payment,'buy')
							
							partofpayment=0.2*monthly_payment
							
							make_and_process_market_orders(t,bank,exchange,partofpayment,'sell')
						
							self.holder.wallet.drain_CRT(self.holder.name,monthly_payment)

							### drain to compensate order pouring
				
				break
		
		
		
		else:
			
			if self.total_returned>self.total_must_be_returned_to_close:
			
				self.status='close'
				self.holder.status='free'
			
			
		
					
				
				
			