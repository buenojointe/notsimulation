<template>
    <div class="Page">
        <h1 v-if="!ready">Loading</h1>
        <transition name="fade">
        <div v-if="ready">
            
            <card class="mb-12">
            <card-header> Load Saved Simulation</card-header>
            <card-body>
              <div style="display: block">
                
            <table class="table">
            <thead>
            <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Time Started</th>
            <th scope="col">Status</th>
            <th scope="col">Progress</th>
            <th scope="col">Controls</th>
            </tr>
            </thead>

            <tbody>
            <tr v-for="(simulation,index) in simulations">
            <th scope="row">{{index+1}}</th>
            <th>{{simulation.pureName}}</th>
            <th>{{simulation.timeStarted}}</th>
            <th>
            <b-progress :value="simulation.t" :max="simulation.computeTime" show-progress animated></b-progress>
            </th>
            <th>{{simulation.t}}/{{simulation.computeTime}}</th>
            <th style="width:300px;">
            <router-link :to="{ path: '/view/'+simulation.simName}">
            <btn class="notbtn" :disabled="!simulation.ready" size="sm" color="primary">Load</btn>
            </router-link>
            <!-- <router-link :to="{ path: '/view/'+simulation.simName}"> -->
            <!-- <btn class="notbtn" v-on:click="renameSim(simulation.simName)" :disabled="!simulation.ready" size="sm" color="default">Rename</btn> -->
            <btn class="notbtn" v-on:click="deleteSim(simulation.simName)" :disabled="!simulation.ready" size="sm" color="default">Delete</btn>
            <!-- </router-link> -->


            </th>
            </tr>
            </tbody>
            </table>
            </div>
            </card-body>
            </card>
            </div>
            </transition>
</div>
</template>
<script>

import { Row, Column, Card,CardHeader, ViewWrapper, CardBody,Btn  } from 'mdbvue'
export default {

    
    name: 'Load',
    components:{Card,CardHeader,CardBody,ViewWrapper,Btn },
    
    data () {
        return {
        info: null,
        simulations:[],
        ready:false,
        }
    },

    created(){
            this.getData();

            this.intervalid= setInterval(()=>{
                this.getData();
                console.log('subscription phase');
            }, 1000);
    },

    destroyed () {
        clearInterval(this.intervalid)
    },
        
    methods:{
        
        renameSim:function(simName){
            this.$http.post("http://127.0.0.1:5000/api/rename",{'simName':simName})
                .then(function(data){
                    console.log(data);
                });
        },

        

        deleteSim:function(simName){
            this.$http.post("http://127.0.0.1:5000/api/delete",{'simName':simName})
                .then(function(data){
                    console.log(data);
                });
            

        },
        getDataInterval: function() {
                setInterval(() => {
                    // this.messages.unshift(this.message);
                    const axios = require('axios');
                    axios
                    .get('http://127.0.0.1:5000/api/folderCache')
                    .then(response => (this.simulations = response.data.response.simulations))
                    .catch(function (error) {console.log(error);});
                    console.log(this.simulations)
                    this.ready=true;
                    }, 1000);
        },
        getData: function(){
            const axios = require('axios');
            axios
            .get('http://127.0.0.1:5000/api/folderCache')
            .then(response => (this.simulations = response.data.response.simulations))
            .catch(function (error) {console.log(error);});
            console.log(this.simulations)
            this.ready=true;
        },
    
    // ready: function(){
    //     this.getData();
    //     this.getDataInterval();
    // //     this.getData();

    //     setInterval(() => {
    //         this.getData();

    //     },3000);
    }
      
    
    }

    




</script>




<style scoped>

/* table{width:90%;margin-left:auto;margin-right: auto;}; */

.notbtn{margin: 0;padding:5px; width:70px;}

th{text-align: center}

.myButton{
    width:100px;
    border: solid 1px;
    text-align:center;
    padding:5px;
    margin:5px;
    border-radius:5px;
}

.myButton:hover{
    border: red;
}


.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}



.Page{ min-height:100vh;}


</style>
