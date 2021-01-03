import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  isOpenChat: false,
  isFullWidthContent: false,
  user: {},
  usersPair: {}
}

const mutations = {
  openChat (state) {
    state.isOpenChat = true
  },
  setFullWidth (state, stateWidth) {
    state.isFullWidthContent = stateWidth
  },
  addUser (state, user) {
    Vue.set(state, 'user', user)
  },
  addPairUsers (state, pair) {
    Vue.set(state, 'usersPair', pair)
  }
}

export default new Vuex.Store({
  state,
  mutations
})
