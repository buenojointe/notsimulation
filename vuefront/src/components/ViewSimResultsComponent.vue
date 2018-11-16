<template>
    
<div class="Page">
    <div v-if="ready">
        <br>
        <h2>Simulation {{info.simName}} results:</h2>
        <br>
        <div class="container">
        <h3>Token Price</h3>
        <line-chart v-if="lineChartData.datasets[0].data" id="Chart" :data="lineChartData" :options="lineChartOptions" :width="600" :height="400"></line-chart>
        </div>
        <br>
        <!-- <h3>System IncomeLossesProfit</h3>
        <line-chart v-if="agentQuantity.datasets[0].data" id="Chart" :data="agentQuantity" :options="lineChartOptions" :width="600" :height="300"></line-chart>
        </div>
        <br> -->
        <div class="container">
        <table>
          <tr>
            <th>
        <h3>Agent Quantity</h3>
        <line-chart v-if="agentQuantity.datasets[0].data" id="Chart" :data="agentQuantity" :options="lineChartOptions" :width="500" :height="300"></line-chart>
        </th>
          <th>
        <h3>Agent Activity</h3>
        <line-chart v-if="agentActivity.datasets[0].data" id="Chart" :data="agentActivity" :options="lineChartOptions" :width="500" :height="300"></line-chart>
        </th>
          </tr>
        </table>
        </div>
        <div class="container">
        <h3>Bank Total</h3>
        <line-chart v-if="bankTotal.datasets[0].data" id="Chart" :data="bankTotal" :options="lineChartOptions" :width="600" :height="400"></line-chart>
        </div>
        <br>
        <div class="container">
          <table>
            <tr>
              <th>
        <h3>Contracts Initated History</h3>
        <line-chart v-if="contractsInitiatedHistory.datasets[0].data" id="Chart" :data="contractsInitiatedHistory" :options="lineChartOptions" :width="500" :height="300"></line-chart>    
              </th>
              <th>
        <h3>Contracts Initated Per Day</h3>      
        <line-chart v-if="contractsInitiatedPerDay.datasets[0].data" id="Chart" :data="contractsInitiatedPerDay" :options="lineChartOptions" :width="500" :height="300"></line-chart>  
              </th>
            </tr>
          </table>
        </div>
        <br>

        <div class="container">
          <h2>Marketmaker</h2>
          <table>
            <tr>
              <th>
        <h3>USDT required</h3>
        <line-chart v-if="wastedUsdtByMarketmaker.datasets[0].data" id="Chart" :data="wastedUsdtByMarketmaker" :options="lineChartOptions" :width="500" :height="300"></line-chart>    
              </th>
              <th>
        <h3>Tokens required</h3>      
        <line-chart v-if="wastedTokensByMarketmaker.datasets[0].data" id="Chart" :data="wastedTokensByMarketmaker" :options="lineChartOptions" :width="500" :height="300"></line-chart>  
              </th>
            </tr>
          </table>
        </div>
        <br>

        
<div class="container">
          <!-- <h2></h2> -->
          
          <!-- <table> -->
            <!-- <tr> -->
              <!-- <th> -->
        <h3>System Total</h3>

        <h4>systemCosts=marketingCost+wastedUsdtByMarketmaker</h4>

        <h4>systemIncome=mmIncome+exchangeComission+affiliateInvestorIncome</h4>

        <line-chart v-if="systemCosts.datasets[0].data" id="Chart" :data="systemCosts" :options="lineChartOptions" :width="500" :height="300"></line-chart>    
              <!-- </th> -->
              <!-- <th> -->
        <!-- <h3>Tokens required</h3>       -->
        <!-- <line-chart v-if="wastedTokensByMarketmaker.datasets[0].data" id="Chart" :data="wastedTokensByMarketmaker" :options="lineChartOptions" :width="500" :height="300"></line-chart>   -->
              <!-- </th> -->
            <!-- </tr> -->
          <!-- </table> -->
        </div>
        <br>
      <div class="container">
        <h3>Config Used</h3>
        <div class="row">
        <div class="col-sm">
          <table>
          General
          <tr><th>Sim Name:</th><th>{{info.configUsed.simName}}</th></tr>
          <tr><th>Compute Time:</th><th>{{info.configUsed.computeTime}}</th></tr>
            <br>
          Marketing Campaign #1
          <tr><th>Start Date</th><th>{{info.configUsed.mk1startDate}}</th></tr>
          <tr><th>End Date</th><th>{{info.configUsed.mk1endDate}}</th></tr>
          <tr><th>Lendees lured</th><th>{{info.configUsed.mk1LendeesLured}}</th></tr>
          <tr><th>Speculants lured</th><th>{{info.configUsed.mk1SpeculantsLured}}</th></tr>
          <tr><th>Investors lured</th><th>{{info.configUsed.mk1InvestorsLured}}</th></tr>
          <tr><th>Cost of 1 Lendee</th><th>{{info.configUsed.mk1LendeeCost}}</th></tr>
          <tr><th>Cost of 1 Speculant</th><th>{{info.configUsed.mk1SpeculantCost}}</th></tr>
          <tr><th>Cost of 1 Investor</th><th>{{info.configUsed.mk1InvestorCost}}</th></tr>
<br>
          Marketing Campaign #2
          <tr><th>Start Date</th><th>{{info.configUsed.mk2startDate}}</th></tr>
          <tr><th>End Date</th><th>{{info.configUsed.mk2endDate}}</th></tr>
          <tr><th>Lendees lured</th><th>{{info.configUsed.mk2LendeesLured}}</th></tr>
          <tr><th>Speculants lured</th><th>{{info.configUsed.mk2SpeculantsLured}}</th></tr>
          <tr><th>Investors lured</th><th>{{info.configUsed.mk2InvestorsLured}}</th></tr>
          <tr><th>Cost of 1 Lendee</th><th>{{info.configUsed.mk2LendeeCost}}</th></tr>
          <tr><th>Cost of 1 Speculant</th><th>{{info.configUsed.mk2SpeculantCost}}</th></tr>
          <tr><th>Cost of 1 Investor</th><th>{{info.configUsed.mk2InvestorCost}}</th></tr>
<br>
          </tr>
        </table>
        </div>
        <div class="col-sm">
          <table>
          Lendee parameters
          <tr><th>Activity</th><th>{{info.configUsed.lendeeActivity}}</th></tr>
          <tr><th>Credit Score Ranges</th><th>{{info.configUsed.lendeeCreditRanges}}</th></tr>
          <tr><th>Range Probabilities</th><th>{{info.configUsed.lendeeCreditProbabilities}}</th></tr>
          <tr><th>Inquiry Sums</th><th>{{info.configUsed.lendeeInquirySums}}</th></tr>
          <tr><th>Sum Probabilities</th><th>{{info.configUsed.lendeeInquiryProbabilities}}</th></tr>
          <br>
          Credit Contract
          <tr><th>Scenario #1 Probability</th><th>{{info.configUsed.contractScen1Prob}}</th></tr>
          <tr><th>Scenario #2 Probability</th><th>{{info.configUsed.contractScen2Prob}}</th></tr>
          <tr><th>Scenario #3 Probability</th><th>{{info.configUsed.contractScen3Prob}}</th></tr>
          <tr><th>Chance to delay</th><th>{{info.configUsed.contractScen3ChanceToDelay}}</th></tr>
          <tr><th>Delay period</th><th>{{info.configUsed.contractScen3DelayPeriod}}</th></tr>
          
          <br>
          Speculant parameters
          <tr><th>Price Deviation</th><th>{{info.configUsed.specPriceDeviations}}</th></tr>
          <tr><th>Deviation Probabilities</th><th>{{info.configUsed.specPriceDeviationsProbs}}</th></tr>
          <tr><th>Amounts</th><th>{{info.configUsed.specAmounts}}</th></tr>
          <tr><th>Amount Probabilities</th><th>{{info.configUsed.specAmountProbs}}</th></tr>
          <br>

          </table>
        </div>
        <div class="col-sm">
          
          <table>
            Investor parameters
          <tr><th>Desired ROI</th><th>{{info.configUsed.investorDesiredROI}}</th></tr>
          <tr><th>Desired ROI Probabilities</th><th>{{info.configUsed.investorDesiredROIProbs}}</th></tr>
          <tr><th>Investment Amounts</th><th>{{info.configUsed.investorAmounts}}</th></tr>
          <tr><th>Investment Amount Probabilities</th><th>{{info.configUsed.investorAmountProbs}}</th></tr>


          <br>
          Marketmaker parameters
          <tr><th>Price to manipulate</th><th>{{info.configUsed.mmPriceToManipulate}}</th></tr>
          <tr><th>Climb Rate</th><th>{{info.configUsed.mmClimbRate}}</th></tr>
          <tr><th>Order Price deviation</th><th>{{info.configUsed.mmDeviation}}</th></tr>
          <tr><th>Amount Base</th><th>{{info.configUsed.mmAmountBase}}</th></tr>
          <tr><th>Liquidity Threshold</th><th>{{info.configUsed.mmLiqThresh}}</th></tr>

          <br>
          Exchange parameters
          <tr><th>Comission on trades</th><th>{{info.configUsed.exchangeComission}}</th></tr>
          
          Bank Products
          <tr><th>Incoming Credit Score</th><th>{{info.configUsed.bankScoreRanges}}</th></tr>
          <tr><th>Credit Interest</th><th>{{info.configUsed.bankCreditInterests}}</th></tr>
          <tr><th>Credit Period</th><th>{{info.configUsed.bankCreditPeriods}}</th></tr>
          <tr><th>Daily Fine</th><th>{{info.configUsed.bankDailyFines}}</th></tr>

          </table>
        </div>
        </div>
        
        
        
        <!-- {{info.configUsed.simName}} -->
        <!-- {{info.configUsed.computeTime}} -->
        <!-- {{info.configUsed}} -->





        <!-- <line-chart v-if="lineChartData.datasets[0].data" id="Chart" :data="lineChartData" :options="lineChartOptions" :width="600" :height="300"></line-chart> -->
        </div>


        

    </div>
  </div>
</template>

<script>
import {Card,CardBody,CardHeader,CardText, LineChart} from 'mdbvue';
import ConfigUsedComponent from './ViewSimComponents/ConfigUsedComponent';
// lineChartData.labels
// lineChartData.datasets[0].data

export default {
    name: 'ViewComponent',
    components: {
    LineChart,Card,
    CardBody,
    CardHeader,
    CardText,
    ConfigUsedComponent,
    
    },
    data() {
      return {
    info:{simName:null},
    ready:false,

    lineChartData: {
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Token Buy Price on Exchange",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(178, 212, 245, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "Token Sell Price on Exchange",fillColor: "rgba(120,220,220,0.2)",strokeColor: "rgba(110,220,220,1)",backgroundColor: 'rgba(143, 209, 187, 0.3)',
            pointColor: "rgba(160,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(150,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
      },

    agentQuantity: {
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Lendees",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(248, 180, 201, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "Specs",fillColor: "rgba(220,220,280,0.2)",strokeColor: "rgba(0,220,290,1)",backgroundColor: 'rgba(211, 189, 235, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "Investors",fillColor: "rgba(280,220,220,0.2)",strokeColor: "rgba(290,220,220,1)",backgroundColor: 'rgba(131, 209, 218, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
      },
    agentActivity: {
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Lendees",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(248, 180, 201, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "Specs",fillColor: "rgba(220,220,280,0.2)",strokeColor: "rgba(0,220,290,1)",backgroundColor: 'rgba(211, 189, 235, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "Investors",fillColor: "rgba(280,220,220,0.2)",strokeColor: "rgba(290,220,220,1)",backgroundColor: 'rgba(131, 209, 218, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
      },
    contractsInitiatedHistory: {
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Contracts initiated History",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(178, 212, 245, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
    },
    contractsInitiatedPerDay: {
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Contracts initiated Per Day",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(143, 209, 187, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
    },

    bankTotal: {
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Total Lended",fillColor: "rgba(20,20,220,0.4)",strokeColor: "rgba(20,20,220,1)", backgroundColor: 'rgba(178, 212, 245, 0.3)',
            pointColor: "rgba(20,20,220,1)",pointStrokeColor: "#aaa",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "Total Returned",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(252, 195, 167, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "Total Difference",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(143, 209, 187, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
    },


    wastedUsdtByMarketmaker:{
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "USDT Required by Marketmaker",fillColor: "rgba(20,20,220,0.4)",strokeColor: "rgba(20,20,220,1)", backgroundColor: 'rgba(153, 160, 249, 0.3)',
            pointColor: "rgba(20,20,220,1)",pointStrokeColor: "#aaa",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
    },
    wastedTokensByMarketmaker:{
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Tokens Required by Marketmaker",fillColor: "rgba(20,20,220,0.4)",strokeColor: "rgba(20,20,220,1)", backgroundColor: 'rgba(153, 160, 249, 0.3)',
            pointColor: "rgba(20,20,220,1)",pointStrokeColor: "#aaa",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
    },
    systemCosts:{
        // labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "System Costs",fillColor: "rgba(20,20,220,0.4)",strokeColor: "rgba(20,20,220,1)", backgroundColor: 'rgba(153, 160, 249, 0.3)',
            pointColor: "rgba(20,20,220,1)",pointStrokeColor: "#aaa",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "System Income",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(252, 195, 167, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          },{
            label: "System Difference",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)",backgroundColor: 'rgba(143, 209, 187, 0.3)',
            pointColor: "rgba(220,220,220,1)",pointStrokeColor: "#fff",pointHighlightFill: "#fff",pointHighlightStroke: "rgba(220,220,220,1)",
            // data: [65, 59, 80, 81, 56, 55, 40]
          }]
    },




    








      lineChartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [{
            gridLines: {
              display: true,
              color: "rgba(0, 0, 0, 0.1)",
            }
          }],
          yAxes: [{
            gridLines: {
              display: true,
              color: "rgba(0, 0, 0, 0.1)",
            }
          }],
        }
      }
    
    
  };
},

    created () {
        const axios = require('axios');
        const simName = this.$route.params.simName;
        axios
            .get('http://127.0.0.1:5000/api/datarequest?filename='+simName)
            .then(response => (

                this.info = response.data.response,
                this.lineChartData.datasets[0].data= response.data.response.tokenBuyPriceHistory,
                this.lineChartData.datasets[1].data= response.data.response.tokenSellPriceHistory,
                this.lineChartData.labels=response.data.response.timeSteps,

                this.agentQuantity.datasets[0].data= response.data.response.agentQuantityLendees,
                this.agentQuantity.datasets[1].data= response.data.response.agentQuantitySpecs,
                this.agentQuantity.datasets[2].data= response.data.response.agentQuantityInvestors,
                this.agentQuantity.labels=response.data.response.timeSteps,

                this.agentActivity.datasets[0].data= response.data.response.agentActivityLendees,
                this.agentActivity.datasets[1].data= response.data.response.agentActivitySpecs,
                this.agentActivity.datasets[2].data= response.data.response.agentActivityInvestors,
                this.agentActivity.labels=response.data.response.timeSteps,
                
                this.contractsInitiatedHistory.datasets[0].data= response.data.response.contractsInitiatedHistory,
                this.contractsInitiatedHistory.labels=response.data.response.timeSteps,

                this.contractsInitiatedPerDay.datasets[0].data= response.data.response.contractsInitiatedPerDay,
                this.contractsInitiatedPerDay.labels=response.data.response.timeSteps,

                this.bankTotal.datasets[0].data= response.data.response.bankTotalLended,
                this.bankTotal.datasets[1].data= response.data.response.bankTotalReturned,
                this.bankTotal.datasets[2].data= response.data.response.bankTotalDiff,

                this.bankTotal.labels=response.data.response.timeSteps,

                this.wastedUsdtByMarketmaker.datasets[0].data=response.data.response.wastedUsdtByMarketmaker,
                this.wastedUsdtByMarketmaker.labels=response.data.response.timeSteps,

                this.wastedTokensByMarketmaker.datasets[0].data=response.data.response.wastedTokensByMarketmaker,
                this.wastedTokensByMarketmaker.labels=response.data.response.timeSteps,

                this.systemCosts.datasets[0].data=response.data.response.systemCosts,
                this.systemCosts.datasets[1].data=response.data.response.systemIncome,
                this.systemCosts.datasets[2].data=response.data.response.systemDiff,
                this.systemCosts.labels=response.data.response.timeSteps

                ));

            console.log('retrieved');
            this.ready=true;
            // this.renderChart()
        },


}
</script>

<style scoped>

.container{
  padding-top:5%;
  padding-bottom:5%;
}

table{width:100%}
/* th{width: 100%;height: 600px;} */
/* th{border: solid 1px;} */


.Page{min-height: 100vh;}
.chart{
    width: 100%;
    height: 500px;
  }
</style>
