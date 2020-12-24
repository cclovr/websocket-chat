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
        <button @click="createUser()" :disabled="!username.length" class="btn-circle">Create user</button>
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
// import axios from 'axios'
// import UserService from '../services/userService'
import {eventBus} from '../main'

export default {
  name: 'HelloWorld',
  components: {
    Arrow
  },
  // sockets: {
  //   connect: function () {
  //     console.log('socket to notification channel connected')
  //   }
  // },
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
      eventBus.$emit('startChat', true)
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
  h1
    color: white
    font-size: 32px
    margin-bottom: 10px
  .description
    color: rgba(255, 255, 255, 0.8)
    font-size: 18px

.form-input
  border-radius: 20px
  font-size: 14px
  padding: 10px 15px
  border: none
  outline: none
  width: 100%
  &:focus
    border: none

.label
  font-size: 12px
  margin-bottom: 3px
  color: rgba(255, 255, 255, 0.8)
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
