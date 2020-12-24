<template>
  <div id="app">
    <Main v-if="!openChat"></Main>
    <Chat v-if="openChat"></Chat>
    <Networks></Networks>
    <Background></Background>
  </div>
</template>

<script>
import Main from './components/main.vue'
import Networks from './components/networks.vue'
import Background from './components/background.vue'
import Chat from './components/chat.vue'
import {eventBus} from './main'

export default {
  name: 'App',
  data () {
    return {
      openChat: false
    }
  },
  components: {
    Main,
    Networks,
    Background,
    Chat
  },
  mounted () {
    this.startChat()
  },
  methods: {
    startChat () {
      eventBus.$on('startChat', data => {
        this.openChat = data
      })
    }
  }
}
</script>

<style scoped lang="sass">
#app
  font-family: 'Roboto', sans-serif
  height: 100vh
  display: flex
</style>
