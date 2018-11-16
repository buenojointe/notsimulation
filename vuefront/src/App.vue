<template>


  <div class="flexible-content">



    <div class="sidebar-fixed position-fixed">
      <a class="logo-wrapper"><img alt="" class="img-fluid" src="./assets/logo-mdb-vue-small.png"/></a>
      
      

      <list-group class="list-group-flush">
        <router-link to="/startnew" @click.native="activeItem = 1">
          <list-group-item :action="true" :class="activeItem === 1 && 'active'"><fa icon="pie-chart" class="mr-3"/>Start New Sim</list-group-item>
        </router-link>
        <router-link to="/load" @click.native="activeItem = 2">
          <list-group-item :action="true" :class="activeItem === 2 && 'active'"><fa icon="user" class="mr-3"/>Load Saved</list-group-item>
        </router-link>
        <router-link to="/about"  @click.native="activeItem = 3">
          <list-group-item :action="true" :class="activeItem === 3 && 'active'"><fa icon="table" class="mr-3"/>About</list-group-item>
        </router-link>
      </list-group>
    </div>
    <main>
      <div class="mt-5 p-5">
        <transition name="fade" mode="out-in" appear>
        <router-view></router-view>
        </transition>
      </div>
      <ftr color="primary-color-dark" class="text-center font-small darken-2">
        <div class="pt-4">
        </div>
        <hr class="my4"/>
        <div class="pb-4">
          <a href="#"><fa icon="facebook" class="mr-3"/></a>
          <a href="#"><fa icon="twitter" class="mr-3"/></a>
          <a href="#"><fa icon="youtube" class="mr-3"/></a>
          <a href="#"><fa icon="google-plus" class="mr-3"/></a>
          <a href="#"><fa icon="dribbble" class="mr-3"/></a>
          <a href="#"><fa icon="pinterest" class="mr-3"/></a>
          <a href="#"><fa icon="github" class="mr-3"/></a>
          <a href="#"><fa icon="codepen" class="mr-3"/></a>
        </div>
      </ftr>
    </main>
  </div>
</template>

<script>
import { Container, Navbar, NavbarItem, NavbarNav, NavbarCollapse, Btn, Fa, ListGroup, ListGroupItem, CardBody, Footer, waves } from 'mdbvue'
import StartNewComponent from './components/StartNewComponent'

export default {
  name: 'AdminTemplate',
  components: {
    Container,
    Navbar,
    NavbarItem,
    NavbarNav,
    NavbarCollapse,
    Btn,
    ListGroup,
    ListGroupItem,
    Fa,
    CardBody,
    'ftr': Footer,
    StartNewComponent,
  },
  data () {
    return {
      activeItem: 1
    }
  },
  beforeMount () {
    this.activeItem = this.$route.matched[0].props.default.page
  },
  mixins: [waves]
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s
}

.fade-enter, .fade-leave-active {
  opacity: 0
}


main {
  background-color: #EDEDEE;
}

.flexible-content {
  transition: padding-left 0.3s;
  padding-left: 270px;
}

.flexible-navbar {
  transition: padding-left 0.5s;
  padding-left: 270px;
}

.sidebar-fixed {
  left: 0;
  top: 0;
  height: 100vh;
  width: 270px;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
  z-index: 1050;
  background-color: #fff;
  padding: 1.5rem;
  padding-top: 0;
}

.sidebar-fixed .logo-wrapper img{
  width: 100%;
  padding: 2.5rem;
}

.sidebar-fixed .list-group-item {
  display: block !important;
  transition: background-color 0.3s;
}

.sidebar-fixed .list-group .active {
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
  border-radius: 5px;
}

@media (max-width: 1199.98px) {
  .sidebar-fixed {
    display: block;
  }
  .flexible-content {
    padding-left: 0;
  }
  .flexible-navbar {
    padding-left: 10px;
  }
}
</style>
<style>
.navbar-light .navbar-brand {
  margin-left: 15px;
  color: #2196f3 !important;
  font-weight: bolder;
}
</style>
