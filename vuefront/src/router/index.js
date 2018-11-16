import Vue from 'vue'
import Router from 'vue-router'
import StartNewComponent from '@/components/StartNewComponent'
import LoadSavedComponent from '@/components/LoadSavedComponent'
import ViewSimResultsComponent from '@/components/ViewSimResultsComponent'
import Maps from '@/components/Maps'


Vue.use(Router)

export default new Router({
  mode: 'history',
  relative: true,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
  routes: [
    {
      path: '/startnew',
      name: 'StartNewComponent',
      component: StartNewComponent,
      alias: '/',
      props: { page: 1 },
      
    },
    {
      path: '/view/:simName',
      name: 'ViewSimResultsComponent',
      component: ViewSimResultsComponent,
      props: { page: 4 }
    },
    {
      path: '/load',
      name: 'LoadSavedComponent',
      props: { page: 2, max:10},
      component: LoadSavedComponent
    },
    {
      path: '/about',
      name: 'Maps',
      component: Maps,
      props: { page: 3 },
      // alias: '/'
    },
  ]
})
