// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router'
import * as VueGoogleMaps from 'vue2-google-maps'
import VueResource from 'vue-resource'
import 'font-awesome/css/font-awesome.min.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'mdbvue/build/css/mdb.css'


import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(VueResource)
Vue.use(BootstrapVue)

// app.use(cors())

Vue.use(VueGoogleMaps, {
  load: {
    libraries: 'places'
  }
})

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
