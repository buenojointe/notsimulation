<h1>Инструкция по запуску</h1>

<h2>Сборка Docker образа</h2>

скачать репо, собрать командой

<code>docker build -t НАЗВАНИЕ_ОБРАЗА -f Dockerfile .</code>

или подгрузить готовый(предварительно полученный) образ-файл 

<code>docker load -i simulation.docker</code>

<h2>Запуск образа</h2>

Для сохранения запусков симуляций между работой контейнера:

следующая строка содержит привязку к папке Хоста

<code>docker run -v /папка/персистенции:/simulation/backend/saveddata --rm -ti --name НАЗВАНИЕ_ОБРАЗА -p 80:80 test</code>

пройти по http://localhost/#/home

<h3>Рекомендуемая система:</h3>
<code>4x ядра, 4 gb RAM</code>

<h2>Инструкция по параметрам</h2>

Для старта новой симуляции требуется ввести параметры среды и агентов и нажать кнопку Run Simulation

<h1>Таблица параметров</h1>

<table class="table mb-0">
                <thead>
                <tr><th>#</th>
                    <th>Группа Параметров</th>
                    <th>Название Англ</th>
                    <th>Описание</th>
                    <th>Значения</th></tr>
                </thead>
                <tbody>
                <tr>
                    <th scope="row"></th>
                    <td>Общие параметры</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">1</th>
                    <td></td>
                    <td>Simulation Name</td>
                    <td>Название симуляции</td>
                    <td>строчные</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td></td>
                    <td>Compute time</td>
                    <td>Количество дней в симуляции</td>
                    <td>0-10000</td>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <td>Подгруппа Маркетинг</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">3</th>
                    <td></td>
                    <td>Lendee Cost</td>
                    <td>Стоимость привлечения 1 заемщика в USDT</td>
                    <td>0-100</td>
                </tr>
                <tr>
                    <th scope="row">4</th>
                    <td></td>
                    <td>Speculant Cost</td>
                    <td>Стоимость привлечения 1 спекулянта в USDT</td>
                    <td>0-100</td>
                </tr>
                <tr>
                    <th scope="row">5</th>
                    <td></td>
                    <td>Investor Cost</td>
                    <td>Стоимость привлечения 1 инвестора в USDT</td>
                    <td>0-100</td>
                </tr>
                <tr>
                    <th scope="row">6</th>
                    <td></td>
                    <td>Marketmaker Labor Cost per day</td>
                    <td>Стоимость работы маркетмейкера (в сутки)</td>
                    <td>0-10000</td>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <td>Параметры Заемщиков</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">7</th>
                    <td></td>
                    <td>Quantity</td>
                    <td>Начальное количество заемщиков в системе</td>
                    <td>0-1000</td>
                </tr>
                <tr>
                    <th scope="row">8</th>
                    <td></td>
                    <td>Flow</td>
                    <td>Скорость притока/оттока заемщиков </td>
                    <td>0-10</td>
                </tr>
                <tr>
                    <th scope="row">9</th>
                    <td></td>
                    <td>Flow Type</td>
                    <td>Тип тока - приток или отток</td>
                    <td>in/out</td>
                </tr>
                <tr>
                    <th scope="row">10</th>
                    <td></td>
                    <td>Activity</td>
                    <td>при индексе активности 0.01 заемщик будет подавать заявку на кредит в среднем 1 раз в 100 дней</td>
                    <td>0.001-1</td>
                </tr>
                <tr>
                    <th scope="row">11</th>
                    <td></td>
                    <td>Credit Score Ranges</td>
                    <td>Кредитные рейтинги</td>
                    <td>50-55,...</td>
                </tr>
                <tr>
                    <th scope="row">12</th>
                    <td></td>
                    <td>Range Probabilities</td>
                    <td>Вероятности выпадения кредитных рейтингов заемщику</td>
                    <td>0.01,0.02...</td>
                </tr>
                <tr>
                    <th scope="row">13</th>
                    <td></td>
                    <td>Inquiry Sums</td>
                    <td>Суммы заявок на кредит</td>
                    <td>1000,2000...</td>
                </tr>
                <tr>
                    <th scope="row">14</th>
                    <td></td>
                    <td>Sum Probabilities</td>
                    <td>Вероятности выпадения сумм заявок</td>
                    <td>0.01,0.02...</td>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <td>Параметры Кредитных Договоров</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">15</th>
                    <td></td>
                    <td>Scenario #1 Probability</td>
                    <td>Вероятность просхождения сценария 1 с контрактом</td>
                    <td>0.1</td>
                </tr>
                <tr>
                    <th scope="row">16</th>
                    <td></td>
                    <td>Scenario #2 Probability</td>
                    <td>Вероятность просхождения сценария 2 с контрактом</td>
                    <td>0.2</td>
                </tr>
                <tr>
                    <th scope="row">17</th>
                    <td></td>
                    <td>Scenario #3 Probability</td>
                    <td>Вероятность просхождения сценария 3 с контрактом</td>
                    <td>0.7</td>
                </tr>
                <tr>
                    <th scope="row">18</th>
                    <td></td>
                    <td>Chance to delay</td>
                    <td>Вероятность отсрочить очередной регулярный платеж в сценарии 3</td>
                    <td>0.2</td>
                </tr>
                <tr>
                    <th scope="row">19</th>
                    <td></td>
                    <td>Delay period</td>
                    <td>Срок задержки регулярного платежа в сценарии 3, дней</td>
                    <td>20</td>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <td>Параметры Спекулянтов</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">20</th>
                    <td></td>
                    <td>Quantity</td>
                    <td>Начальное количество спекулянтов в системе</td>
                    <td>0-1000</td>
                </tr>
                <tr>
                    <th scope="row">21</th>
                    <td></td>
                    <td>Flow</td>
                    <td>Скорость притока/оттока спекулянтов</td>
                    <td>0-10</td>
                </tr>
                <tr>
                    <th scope="row">22</th>
                    <td></td>
                    <td>Flow type</td>
                    <td>Тип тока - приток или отток</td>
                    <td>in/out</td>
                </tr>
                <tr>
                    <th scope="row">23</th>
                    <td></td>
                    <td>Price Deviation</td>
                    <td>Отклонения от рыночной цены, принимаемые для торговли спекулянтами</td>
                    <td>0.01,0.02,0,03...</td>
                </tr>
                <tr>
                    <th scope="row">24</th>
                    <td></td>
                    <td>Deviation Probabilities</td>
                    <td>Вероятности ценовых отклонений</td>
                    <td>0.1,0.2,0,7...</td>
                </tr>
                <tr>
                    <th scope="row">25</th>
                    <td></td>
                    <td>Amounts</td>
                    <td>Торгуемые объемы спекулянтом</td>
                    <td>100,200,300</td>
                </tr>
                <tr>
                    <th scope="row">26</th>
                    <td></td>
                    <td>Amount Probabilities</td>
                    <td>Вероятности выпадения спекулянту торгуемых объемов</td>
                    <td>0.1,0.2,07...</td>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <td>Параметры Инвесторов</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">27</th>
                    <td></td>
                    <td>Quantity</td>
                    <td>Начальное количество инвесторов в система</td>
                    <td>0-1000</td>
                </tr>
                <tr>
                    <th scope="row">28</th>
                    <td></td>
                    <td>Flow</td>
                    <td>Скорость притока/оттока инвесторов</td>
                    <td>0-10</td>
                </tr>
                <tr>
                    <th scope="row">29</th>
                    <td></td>
                    <td>Flow type</td>
                    <td>Тип тока - приток или отток</td>
                    <td>in/out</td>
                </tr>
                <tr>
                    <th scope="row">30</th>
                    <td></td>
                    <td>Desired ROI</td>
                    <td>Желаемые Возвраты на Инвестиции Инвесторов</td>
                    <td>0.05,0.1,0.2</td>
                </tr>
                <tr>
                    <th scope="row">31</th>
                    <td></td>
                    <td>Desired ROI Probabilities</td>
                    <td>Вероятности желаемых возвратов</td>
                    <td>0.1,0.2,0.7...</td>
                </tr>
                <tr>
                    <th scope="row">32</th>
                    <td></td>
                    <td>Investment Amounts</td>
                    <td>Объемы инвестиций</td>
                    <td>1000,2000,10000...</td>
                </tr>
                <tr>
                    <th scope="row">33</th>
                    <td></td>
                    <td>Investment Amount Probabilities</td>
                    <td>Вероятности объемов</td>
                    <td>0.1,0.2,0.7...</td>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <td>Параметры Маркетмейкера</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">34</th>
                    <td></td>
                    <td>Price to manipulate</td>
                    <td>Цена, от которой маркетмейкер берет шаг и восстанавливает ликвидность, если рынку эту необходимо</td>
                    <td>1</td>
                </tr>
                <tr>
                    <th scope="row">35</th>
                    <td></td>
                    <td>Climb Rate</td>
                    <td>Скорость роста курса, в день</td>
                    <td>0.0001</td>
                </tr>
                <tr>
                    <th scope="row">36</th>
                    <td></td>
                    <td>Order Price deviation</td>
                    <td>Шаг ордеров маркетмейкера</td>
                    <td>0.02</td>
                </tr>
                <tr>
                    <th scope="row">37</th>
                    <td></td>
                    <td>Amount Base</td>
                    <td>Основа ордеров маркетмейкера, увеличивается итеративно, удаляясь от спреда, с шагом</td>
                    <td>200</td>
                </tr>
                <tr>
                    <th scope="row">38</th>
                    <td></td>
                    <td>Liquidity Threshold</td>
                    <td>Если ликвидность какого-либо ордера бука снизится ниже этого порога, то маркет мейкер будет добавлять ликвидность, </td>
                    <td>10000</td>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <td>Параметры Биржи</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">39</th>
                    <td></td>
                    <td>Comission on trades</td>
                    <td>Комиссия Биржи на трейды</td>
                    <td>0.0001-0.01 (не %)</td>
                </tr>
                <tr>
                    <th scope="row"></th>
                    <td>Параметры Банковских продуктов</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <th scope="row">40</th>
                    <td></td>
                    <td>Incoming Credit Score</td>
                    <td>Диапазоны рейтинга</td>
                    <td>фикс.</td>
                </tr>
                <tr>
                    <th scope="row">41</th>
                    <td></td>
                    <td>Credit Interest</td>
                    <td>Процентная ставка</td>
                    <td>20,15...</td>
                </tr>
                <tr>
                    <th scope="row">42</th>
                    <td></td>
                    <td>Credit Period</td>
                    <td>Кредитный период</td>
                    <td>30,120...</td>
                </tr>
                <tr>
                    <th scope="row">43</th>
                    <td></td>
                    <td>Daily Fine</td>
                    <td>Сумма ежедневного штрафа в случае просрочки</td>
                    <td>10,20...</td>
                </tr>
                </tbody>
            </table>
            
