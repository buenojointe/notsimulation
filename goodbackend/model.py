
from notmodel.environments.bank import Bank
from notmodel.environments.exchange import Exchange
from notmodel.agentpool import AgentPool

from notmodel.handle_json import writetojson
from notmodel.handle_json import updateStatus

from tqdm import tqdm


from time import gmtime, strftime

def makeUpdateSchedule(compute_time):

    hund=100

    arange=compute_time/hund
    out=[]

    temp=0

    for x in range(int(arange)):
        temp+=hund
        out.append(temp)

    return out



class Model:

    def __init__(self,incoming_config):


        timeStarted=strftime("%Y-%m-%d-%H-%M-%S", gmtime())
        
        
        self.config=incoming_config

        self.config['simName']=timeStarted+'_'+incoming_config['simName']

        self.bank=Bank(incoming_config)
        self.agentpool=AgentPool(self.bank,incoming_config)
        
        self.exchange=Exchange(self.agentpool.marketmaker,self.bank,incoming_config)
        self.updateSchedule=makeUpdateSchedule(int(incoming_config['computeTime']))
        # print(self.updateSchedule)
        # input()

    def run(self):

        print('model running')

        ct=int(self.config['computeTime'])
	    
        for t in tqdm(range(1,int(ct+1))):

            self.agentpool.cycle(t,self.bank,self.exchange)

            self.exchange.take_snapshot()
            self.bank.take_snapshot()

            if t in self.updateSchedule:
                updateStatus(t,self.config)


            

        

        def reform(dat):
            # out=[]
            out={}

            for x in range(len(dat)):
                # obj={'x':x,'y':dat[x]}
                # obj={x:dat[x]}
                out[x]=dat[x]
            return out

        def cache(alist):

            def split_list(alist, wanted_parts=20):
                length = len(alist)
                return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
                        for i in range(wanted_parts) ]

            def mean(numbers):
                return float(sum(numbers)) / max(len(numbers), 1)

            splitted=split_list(alist)
            out=[]

            for x in range(len(splitted)):
                out.append(mean(splitted[x]))
            
            return out
        
        
        data={}

        
        data['simName']=self.config['simName']
        
        data['configUsed']=self.config
        # data['timeStarted']=strftime("%Y-%m-%d %H:%M:%S", gmtime())
        # data['tokenPriceHistory']=reform(self.exchange.tokenPriceHistory)
        # data['tokenPriceHistory']=self.exchange.tokenPriceHistory
        data['tokenBuyPriceHistory']=cache(self.exchange.tokenBuyPriceHistory)
        data['tokenSellPriceHistory']=cache(self.exchange.tokenSellPriceHistory)

        data['timeSteps']=[ str(x) for x in range(1,len(data['tokenBuyPriceHistory'])+1)]

        data['agentQuantityLendees']=cache(self.agentpool.agentQuantityLendees)
        data['agentQuantitySpecs']=cache(self.agentpool.agentQuantitySpecs)
        data['agentQuantityInvestors']=cache(self.agentpool.agentQuantityInvestors)

        data['contractsInitiatedHistory']=cache(self.bank.contractsInitiatedHistory)
        data['contractsInitiatedPerDay']=cache(self.bank.contractsInitiatedPerDay)
        
        # data['total_lended']=cache(self.bank.total_lended)
        # data['total_returned']=cache(self.bank.total_returned)

        data['agentActivityLendees']=cache(self.agentpool.agentActivityLendees)
        data['agentActivitySpecs']=cache(self.agentpool.agentActivitySpecs)
        data['agentActivityInvestors']=cache(self.agentpool.agentActivityInvestors)

        data['bankTotalLended']=cache(self.bank.bankTotalLended)
        data['bankTotalReturned']=cache(self.bank.bankTotalReturned)
        data['bankTotalDiff']=[data['bankTotalReturned'][x]-data['bankTotalLended'][x] for x in range(len(data['bankTotalLended']))]

        data['wastedUsdtByMarketmaker']=cache(self.agentpool.marketmaker.wastedUsdt)
        data['wastedTokensByMarketmaker']=cache(self.agentpool.marketmaker.wastedTokens)

        data['marketingCost']=cache(self.agentpool.marketingCost)
        data['systemCosts']=[data['wastedUsdtByMarketmaker'][x]+data['marketingCost'][x] for x in range(len(data['marketingCost']))]

        

        data['mmIncome']=cache(self.exchange.mmIncome)

        data['systemIncome']=[data['mmIncome'][x] for x in range(len(data['mmIncome']))]
        data['systemDiff']=[data['systemIncome'][x]-data['systemCosts'][x] for x in range(len(data['bankTotalLended']))]
        
        

	    
        writetojson(data)









		
