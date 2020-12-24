import Vue from 'vue'

export default {
  getUsers () {
    return Vue.http.get('/api/posts')
  }
}
