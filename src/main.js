// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueSocketIO from 'vue-socket.io'
import store from './store/index'

// styles
import '../src/assets/base.sass'

Vue.config.productionTip = false
export const eventBus = new Vue()
Vue.use(new VueSocketIO({
  debug: true,
  connection: 'http://localhost:8888',
  vuex: {
    store,
    actionPrefix: 'SOCKET_',
    mutationPrefix: 'SOCKET_'
  }
}))

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
