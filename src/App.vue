<template>
  <div id="app">
    <Main v-if="!$store.state.isOpenChat && !openChat"></Main>
    <Chat v-else></Chat>
    <Networks></Networks>
    <Background></Background>
  </div>
</template>

<script>
import Main from './components/main.vue'
import Networks from './components/networks.vue'
import Background from './components/background.vue'
import Chat from './components/chat.vue'

export default {
  name: 'App',
  data () {
    return {
      openChat: localStorage.getItem('open-chat')
    }
  },
  components: {
    Main,
    Networks,
    Background,
    Chat
  }
}
</script>

<style scoped lang="sass">
#app
  font-family: 'Roboto', sans-serif
  height: 100vh
  display: flex
</style>
