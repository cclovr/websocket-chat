<template>
  <div class="main block" :class="{'full-width': fullWidth}">
    <Arrow></Arrow>
    <div class="welcome-text">
      <h1>Hello! 👋</h1>
      <p class="description">Sign in and start chat</p>
    </div>
    <div class="form-main">
      <form class="form-item">
        <label for="username" class="label">Your username</label>
        <input type="text"
               id="username"
               v-model="username"
               class="form-input"
               placeholder="your username"
               aria-label="Username">
        <button @click.prevent="createUser()" :disabled="!username.length" class="btn-circle">Create user</button>
      </form>
      <div class="form-item">
        <span class="label">Select interlocutor</span>
        <div class="dropdown">
          <button
            class="btn-circle dropdown-toggle"
            type="button" id="dropdownMenuButton"
            data-bs-toggle="dropdown"
            aria-expanded="false">
            {{ chosenName ? chosenName : 'Select user'}}
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li><a class="dropdown-item" href="#" @click="chooseUser('Anna')">Anna</a></li>
            <li><a class="dropdown-item" href="#" @click="chooseUser('Kate')">Kate</a></li>
          </ul>
        </div>
        <button @click="startChat()" :disabled="!chosenName" class="btn-circle">Start chat</button>
      </div>
    </div>
  </div>
</template>

<script>
import Arrow from '../components/arrow.vue'
import {eventBus} from '../main'

export default {
  name: 'HelloWorld',
  components: {
    Arrow
  },
  sockets: {
    connect () {
      // Fired when the socket connects.
      console.log('1')
    },

    disconnect () {
      console.log('2')
    },

    // Fired when the server sends something on the "messageChannel" channel.
    messageChannel (data) {
      console.log('3')
    }
  },
  data () {
    return {
      username: '',
      connection: null,
      users: [],
      fullWidth: false,
      chosenName: ''
    }
  },
  mounted () {
    this.listenConnectionUsers()
    this.listenFullWidth()
  },
  methods: {
    startChat () {
      this.$store.commit('openChat', window.localStorage.setItem('open-chat', true))
    },
    listenFullWidth () {
      eventBus.$on('isFullWidth', data => {
        this.fullWidth = data
      })
    },
    chooseUser (name) {
      this.chosenName = name
    },
    createUser () {
      this.connection.send(JSON.stringify({name: this.username}))
    },
    listenConnectionUsers () {
      console.log(this.users)
      // const users = []
      // this.users = users
      this.connection = new WebSocket('ws://localhost:8888/api/listen_connection_users')

      this.connection.onmessage = function (event) {
        this.users.push(JSON.parse(event.data))
      }

      this.connection.onopen = function (event) {
        console.log('Successfully connected to the echo websocket server...')
      }
    }
  }
}
</script>
<style scoped lang="sass">
.welcome-text
  width: 100%
  margin-bottom: 20px
  .description
    color: var(--opacity-white)
    font-size: 18px

.label
  font-size: 12px
  margin-bottom: 3px
  color: var(--opacity-white)
  display: block

.form-item
  margin-bottom: 30px
  &:last-child
    margin-bottom: 0

.form-main
  width: 100%
  .dropdown,
  .btn,
  .dropdown-menu
    width: 100%

.dropdown-toggle
  &.show
    border-radius: 20px 20px 0 0
.dropdown-menu
  border-radius: 0 0 10px 10px
</style>
