<template>
  <section id="dashboard">
    <card class="mb-12">
      <CardHeader>General</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
      <table>
        <!-- <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Group</th>
            <th scope="col">Name</th>
            <th scope="col">Description</th>
            <th scope="col">Value</th>
            <th scope="col">Range</th>
          </tr>
        </thead> -->
        <!-- <tbody> -->
        <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>

        <tr><th>1</th><th>Simulation Name</th><th>Название симуляции</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.simName"></b-form-input></th><th>string</th></tr>
        <tr><th>2</th><th>Compute Time</th><th>Количество дней в симуляции</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.computeTime"></b-form-input></th><th>0-10000</th></tr>
        
        <!-- </tbody> -->
      </table>

      </card-body>
    </card>
    <br>

    <card class="mb-12">
      <CardHeader>Marketing Campaign #1</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>

        <!-- <table class="table"> -->
          <!-- <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Group</th>
            <th scope="col">Name</th>
            <th scope="col">Description</th>
            <th scope="col">Value</th>
            <th scope="col">Range</th>
          </tr>
        </thead> -->

        <!-- <tbody> -->
           <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>


        <!-- <tr><th></th><th></th><th></th><th></th><th></th><th></th></tr> -->
        <tr><th>3</th><th>Start Date</th><th>Дата Начала</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk1startDate"></b-form-input></th><th></th></tr>
        <tr><th>4</th><th>End Date</th><th>Дата конца</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk1endDate"></b-form-input></th><th></th></tr>
        <tr><th>5</th><th>Lendees lured, cost</th><th>Заемщиков привлечено</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk1LendeesLured"></b-form-input></th><th></th></tr>
        <tr><th>6</th><th>Speculants lured, cost</th><th>Заемщиков привлечено</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk1SpeculantsLured"></b-form-input></th><th></th></tr>
        <tr><th>7</th><th>Investors lured, cost</th><th>Заемщиков привлечено</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk1InvestorsLured"></b-form-input></th><th></th></tr>
        <tr><th>8</th><th>Cost of 1 Lendee</th><th>Стоимость 1 заемщика</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk1LendeeCost"></b-form-input></th><th></th></tr>
        <tr><th>9</th><th>Cost of 1 Speculant</th><th>Стоимость 1 спекулянта</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk1SpeculantCost"></b-form-input></th><th></th></tr>
        <tr><th>10</th><th>Cost of 1 Investor</th><th>Стоимость 1 инветсора</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk1InvestorCost"></b-form-input></th><th></th></tr>
        <!-- </tbody> -->
        </table>
      </card-body>
    </card>
    <br>

    <card class="mb-12">
      <CardHeader>Marketing Campaign #2</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>
           <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>

        <tr><th>11</th><th>Start Date</th><th>Дата Начала</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk2startDate"></b-form-input></th><th></th></tr>
        <tr><th>12</th><th>End Date</th><th>Дата конца</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk2endDate"></b-form-input></th><th></th></tr>
        <tr><th>13</th><th>Lendees lured, cost</th><th>Заемщиков привлечено</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk2LendeesLured"></b-form-input></th><th></th></tr>
        <tr><th>14</th><th>Speculants lured, cost</th><th>Заемщиков привлечено</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk2SpeculantsLured"></b-form-input></th><th></th></tr>
        <tr><th>15</th><th>Investors lured, cost</th><th>Заемщиков привлечено</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk2InvestorsLured"></b-form-input></th><th></th></tr>
        <tr><th>16</th><th>Cost of 1 Lendee</th><th>Стоимость 1 заемщика</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk2LendeeCost"></b-form-input></th><th></th></tr>
        <tr><th>17</th><th>Cost of 1 Speculant</th><th>Стоимость 1 спекулянта</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk2SpeculantCost"></b-form-input></th><th></th></tr>
        <tr><th>18</th><th>Cost of 1 Investor</th><th>Стоимость 1 инветсора</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mk2InvestorCost"></b-form-input></th><th></th></tr>
        </table>
      </card-body>
    </card>
    <br>

    <card class="mb-12">
      <CardHeader>Lendee parameters</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>
           <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>

        <tr><th>19</th><th>Activity</th><th>Индекс активности</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.lendeeActivity"></b-form-input></th><th></th></tr>
        <tr><th>20</th><th>Credit Score Ranges</th><th>Кредитные рейтинги</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.lendeeCreditRanges"></b-form-input></th><th></th></tr>
        <tr><th>21</th><th>Range Probabilities</th><th>Вероятности выпадения кредитных рейтингов заемщику</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.lendeeCreditProbabilities"></b-form-input></th><th></th></tr>
        <tr><th>22</th><th>Inquiry Sums</th><th>Суммы заявок на кредит</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.lendeeInquirySums"></b-form-input></th><th></th></tr>
        <tr><th>23</th><th>Sum Probabilities</th><th>Вероятности выпадения сумм заявок</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.lendeeInquiryProbabilities"></b-form-input></th><th></th></tr>
        </table>
      </card-body>
    </card>
    <br>

    <card class="mb-12">
      <CardHeader>Credit Contract</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>
          
          <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>

        
        <tr><th>24</th><th>Scenario #1 Probability</th><th>Вероятность просхождения сценария 1 с контрактом</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.contractScen1Prob"></b-form-input></th><th></th></tr>
        <tr><th>25</th><th>Scenario #2 Probability</th><th>Вероятность просхождения сценария 2 с контрактом</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.contractScen2Prob"></b-form-input></th><th></th></tr>
        <tr><th>26</th><th>Scenario #3 Probability</th><th>Вероятность просхождения сценария 3 с контрактом</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.contractScen3Prob"></b-form-input></th><th></th></tr>
        <tr><th>27</th><th>Chance to delay</th><th>Вероятность отсрочить очередной регулярный платеж в сценарии 3</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.contractScen3ChanceToDelay"></b-form-input></th><th></th></tr>
        <tr><th>28</th><th>Delay period</th><th>Срок задержки регулярного платежа в сценарии 3, дней</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.contractScen3DelayPeriod"></b-form-input></th><th></th></tr>
        </table>
      </card-body>
    </card>
    <br>

    <card class="mb-12">
      <CardHeader>Speculant parameters</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>

 <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>


          <tr><th>29</th><th>Price Deviation</th><th>Отклонения от рыночной цены, принимаемые для торговли спекулянтами</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.specPriceDeviations"></b-form-input></th><th></th></tr>
          <tr><th>30</th><th>Deviation Probabilities</th><th>Вероятности ценовых отклонений</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.specPriceDeviationsProbs"></b-form-input></th><th></th></tr>
          <tr><th>31</th><th>Amounts</th><th>Торгуемые объемы спекулянтом</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.specAmounts"></b-form-input></th><th></th></tr>
          <tr><th>32</th><th>Amount Probabilities</th><th>Вероятности выпадения спекулянту торгуемых объемов</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.specAmountProbs"></b-form-input></th><th></th></tr>
        </table>
      </card-body>
    </card>
    <br>

    <card class="mb-12">
      <CardHeader>Investor parameters</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>

 <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>



        <tr><th>33</th><th>Desired ROI</th><th>Желаемые Возвраты на Инвестиции Инвесторов</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.investorDesiredROI"></b-form-input></th><th></th></tr>
        <tr><th>34</th><th>Desired ROI Probabilities</th><th>Вероятности желаемых возвратов</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.investorDesiredROIProbs"></b-form-input></th><th></th></tr>
        <tr><th>35</th><th>Investment Amounts</th><th>Объемы инвестиций</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.investorAmounts"></b-form-input></th><th></th></tr>
        <tr><th>36</th><th>Investment Amount Probabilities</th><th>Вероятности объемов</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.investorAmountProbs"></b-form-input></th><th></th></tr>    
        </table>
      </card-body>
    </card>
    <br>


      <card class="mb-12">
        <CardHeader>Marketmaker parameters</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>

 <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>


        <tr><th>37</th><th>Price to manipulate</th><th>Цена, от которой маркетмейкер берет шаг и восстанавливает ликвидность, если рынку эту необходимо</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mmPriceToManipulate"></b-form-input></th><th></th></tr>
        <tr><th>38</th><th>Climb Rate</th><th>Скорость роста курса, в день</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mmClimbRate"></b-form-input></th><th></th></tr>
        <tr><th>39</th><th>Order Price deviation</th><th>Шаг ордеров маркетмейкера</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mmDeviation"></b-form-input></th><th></th></tr>
        <tr><th>40</th><th>Amount Base</th><th>Основа ордеров маркетмейкера, увеличивается итеративно, удаляясь от спреда, с шагом</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mmAmountBase"></b-form-input></th><th></th></tr>
        <tr><th>41</th><th>Liquidity Threshold</th><th>Если ликвидность какого-либо ордера бука снизится ниже этого порога, то маркет мейкер будет добавлять ликвидность</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.mmLiqThresh"></b-form-input></th><th></th></tr>
        </table>
      </card-body>
    </card>
    <br>

          <card class="mb-12">
            <CardHeader>Exchange parameters</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>

 <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>


          <tr><th>42</th><th>Comission on trades</th><th>Комиссия Биржи на трейды</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.exchangeComission"></b-form-input></th><th></th></tr>
        </table>
      </card-body>
    </card>
    <br>

          <card class="mb-12">
            <CardHeader>Bank Products</CardHeader>
      <card-body class="d-sm-flex justify-content-between">
        <table>

 <colgroup>
        <col span="1" style="width: 5%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 25%;">
        <col span="1" style="width: 30%;">
        </colgroup>


      
        <tr><th>37</th><th>Incoming Credit Score</th><th>Диапазоны рейтинга</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.bankScoreRanges"></b-form-input></th><th></th></tr>
        <tr><th>38</th><th>Credit Interest</th><th>Процентная ставка</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.bankCreditInterests"></b-form-input></th><th></th></tr>
        <tr><th>39</th><th>Credit Period</th><th>Кредитный период</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.bankCreditPeriods"></b-form-input></th><th></th></tr>
        <tr><th>40</th><th>Daily Fine</th><th>Сумма ежедневного штрафа в случае просрочки</th><th><b-form-input id="exampleInput1"v-model="outgoingConfig.bankDailyFines"></b-form-input></th><th></th></tr>
        


        </table>
      </card-body>
    </card>
    <br>


    <card class="mb-12">
      <card-body class="d-sm-flex justify-content-between">
        <table>
        
                


        
            
            <tr>
              <!-- <b-link :to="{ path: "/load" }"> -->
              <b-link :to="{ path: '/load' }">
              <b-button style="margin-left:60%;" size="lg" variant="primary" v-on:click="click">
                SIMULATE

                
            </b-button>
            </b-link>
        </tr>
        <!-- {{outgoingConfig.computeTime}} -->
        </table>
            
             
        
      </card-body>
    </card>
  </section>
</template>

<script>
import { Row, Column, Btn, Card, CardBody, CardHeader, CardText, Fa, BarChart, PieChart, LineChart, RadarChart, DoughnutChart, ListGroup, ListGroupItem, Badge, Modal, ModalHeader, ModalTitle, ModalBody, ModalFooter } from 'mdbvue'

export default {
  name: 'Dashboard',
  components: {
    Row,
    Column,
    Btn,
    Card,
    CardBody,
    CardHeader,
    CardText,
    Fa,
    BarChart,
    PieChart,
    LineChart,
    RadarChart,
    DoughnutChart,
    ListGroup,
    ListGroupItem,
    Badge,
    Modal,
    ModalHeader,
    ModalTitle,
    ModalBody,
    ModalFooter
  },
   methods:{
        click:function(){
            this.$http.post("http://127.0.0.1:5000/api/newSimThread",{'incomingConfig':this.outgoingConfig})
                .then(function(data){
                    console.log(data);
                });
            // window.location.href = '/load';
            // this.ready=false
        },
        

  },
  data () {
    return {
      // ready:true,
      outgoingConfig:{
                simName:'hello1',
                computeTime: '500',

                
                mk1startDate: '0',
                mk1endDate: '10',
                mk1LendeesLured: '100',
                mk1SpeculantsLured: '50',
                mk1InvestorsLured: '30',

                mk1LendeeCost: '4',
                mk1SpeculantCost: '5',
                mk1InvestorCost:'6',

                mk2startDate: '0',
                mk2endDate: '10',
                mk2LendeesLured: '100',
                mk2SpeculantsLured: '50',
                mk2InvestorsLured: '30',

                mk2LendeeCost: '4',
                mk2SpeculantCost: '5',
                mk2InvestorCost:'6',

                lendeeActivity: '0.01',
                lendeeCreditRanges: '50-75,75-90,90-100',
                lendeeCreditProbabilities: '0.1,0.8,0.1',
                lendeeInquirySums: '1000,5000,10000',
                lendeeInquiryProbabilities: '0.3,0.4,0.3',
                
                contractScen1Prob: '0.07',
                contractScen2Prob: '0.73',
                contractScen3Prob: '0.2',
                contractScen3ChanceToDelay: '0.2',
                contractScen3DelayPeriod: '20',

                specPriceDeviations: '0.02,0.04,0.06',
                specPriceDeviationsProbs: '0.2,0.3,0.5',
                specAmounts: '50,200,800',
                specAmountProbs: '0.5,0.3,0.2',

                investorDesiredROI: '0.05,0.1,0.2,0.3,0.4',
                investorDesiredROIProbs: '0.05,0.15,0.3,0.3,0.2',
                investorAmounts: '6000,7000,8000,9000,10000',
                investorAmountProbs: '0.05,0.15,0.3,0.3,0.2',

                mmPriceToManipulate: '1',
                mmClimbRate: '0.0000',
                mmDeviation: '0.02',
                mmAmountBase: '100',
                mmLiqThresh: '10000',
            
                exchangeComission: '0.0001',

                bankScoreRanges: '50-75,75-90,90-100',
                bankCreditInterests: '0.25,0.22,0.2',
                bankCreditPeriods: '30,90,200',
                bankDailyFines: '15,10,8',
            },
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

th{
  padding-left:5px;
  /* width:300px; */
}
table{
  width:100%
}
.cascading-admin-card {
  margin: 20px 0;
}
.cascading-admin-card .admin-up {
  margin-left: 4%;
  margin-right: 4%;
  margin-top: -20px;
}
.cascading-admin-card .admin-up .fa {
  box-shadow: 0 2px 9px 0 rgba(0, 0, 0, 0.2), 0 2px 13px 0 rgba(0, 0, 0, 0.19);
}
.cascading-admin-card .admin-up .fa {
  padding: 1.7rem;
  font-size: 2rem;
  color: #fff;
  text-align: left;
  margin-right: 1rem;
  border-radius: 3px;
}
.cascading-admin-card .admin-up .data {
  float: right;
  margin-top: 2rem;
  text-align: right;
}
.admin-up .data p {
  color: #999999;
  font-size: 12px;
}
.classic-admin-card .card-body {
  color: #fff;
  margin-bottom: 0;
  padding: 0.9rem;
}
.classic-admin-card .card-body p {
  font-size: 13px;
  opacity: 0.7;
  margin-bottom: 0;
}
.classic-admin-card .card-body h4 {
  margin-top: 10px;
}
</style>
