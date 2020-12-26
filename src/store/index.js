import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  isOpenChat: false
}

const mutations = {
  openChat (state) {
    state.isOpenChat = true
  }
}

// state.subscribe((mutation, state) => {
//   // Store the state object as a JSON string
//   localStorage.setItem('open-chat', true)
// });

export default new Vuex.Store({
  state,
  mutations
})
