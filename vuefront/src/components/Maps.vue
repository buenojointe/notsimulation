<template>
  <section id="maps">
    <row>
      <column md="12">
        <card cascade narrow class="mt-5">
          <view-wrapper class="gradient-card-header blue darken-2">
            <h4 class="h4-responsive text-white">
              Built On
            </h4>
          </view-wrapper>
          <card-body class="text-center" style="height:100px">
          Python, Vuejs, Vue MDB  
          </card-body>
        </card>
      </column>
    </row>
  </section>
</template>

<script>
import { Row, Column, Card, ViewWrapper, CardBody } from 'mdbvue'

export default {
  name: 'Maps',
  components: {
    Row,
    Column,
    Card,
    ViewWrapper,
    CardBody
  },
  data () {
    return {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#maps{
  min-height:100vh;
}
.card.card-cascade .view.gradient-card-header {
  padding: 1rem 1rem;
  text-align: center;
}
.card.card-cascade h3, .card.card-cascade h4 {
  margin-bottom: 0px;
}
</style>
