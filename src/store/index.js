import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  isOpenChat: false,
  isFullWidthContent: false,
  users: [],
  usersPair: []
}

const mutations = {
  openChat (state) {
    state.isOpenChat = true
  },
  setFullWidth (state, stateWidth) {
    state.isFullWidthContent = stateWidth
  },
  addUser (state, user) {
    state.users.push(user)
  },
  addPairUsers (state, pair) {
    state.usersPair.push(pair)
  }
}

export default new Vuex.Store({
  state,
  mutations
})
