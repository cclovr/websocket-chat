import Vue from 'vue'
import App from './App'
import router from './router'
// import VueSocketIO from 'vue-socket.io'
import store from './store/index'

// styles
import '../src/assets/base.sass'
// import {io} from 'socket.io-client'

Vue.config.productionTip = false
// Vue.use(new VueSocketIO({
//   debug: true,
//   connection: io('http://localhost:8888')
//   // vuex: {
//   //   store,
//   //   actionPrefix: 'SOCKET_',
//   //   mutationPrefix: 'SOCKET_'
//   // }
// }))

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
