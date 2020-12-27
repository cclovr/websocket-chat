<template>
  <div class="main block" :class="{'full-width': $store.state.isFullWidthContent}">
    <Arrow></Arrow>
    <div class="welcome-text">
      <h1>Hello! 👋</h1>
      <p class="description">Sign in and start chat</p>
    </div>
    <div class="form-main">
      <form class="form-item" @submit.prevent="createUser()">
        <label for="username" class="label">Your username</label>
        <input type="text"
               id="username"
               v-model="username"
               class="form-input"
               placeholder="your username"
               aria-label="Username">
        <button type="submit" :disabled="!username.length" class="btn-circle">Create user</button>
      </form>
      <div class="form-item">
        <span class="label">Select interlocutor</span>
        <div class="dropdown">
          <button
            class="btn-circle dropdown-toggle"
            type="button" id="dropdownMenuButton"
            data-bs-toggle="dropdown"
            aria-expanded="false">
            {{ interlocutorName ? interlocutorName : 'Select user'}}
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li v-for="(user, index) in $store.state.users"
                :key="index"
                class="dropdown-item"
                @click="chooseUser(user.name)">
              {{user.name}}
            </li>
          </ul>
        </div>
        <button @click="startChat()" :disabled="!interlocutorName" class="btn-circle">Start chat</button>
      </div>
    </div>
  </div>
</template>

<script>
import Arrow from '../components/arrow.vue'

export default {
  name: 'HelloWorld',
  components: {
    Arrow
  },
  data () {
    return {
      username: '',
      socketAddUser: new WebSocket('ws://localhost:8888/api/listen_connection_users'),
      socketStartChat: new WebSocket('ws://localhost:8888/api/connect_users_to_chat'),
      users: [],
      fullWidth: false,
      interlocutorName: ''
    }
  },
  mounted () {
    this.listenConnectionUsers()
  },
  methods: {
    startChat () {
      this.$store.commit('openChat', window.localStorage.setItem('open-chat', true))
      this.socketStartChat.send(JSON.stringify({
        name: this.username,
        interlocutor: this.interlocutorName
      }))
    },
    chooseUser (name) {
      this.chosenName = name
    },
    createUser () {
      this.socketAddUser.send(JSON.stringify({name: this.username}))
    },
    listenConnectionUsers () {
      // For add user
      this.socketAddUser.onopen = () => {
        console.log('socket add user connected')
      }
      this.socketAddUser.onmessage = (event) => {
        this.$store.commit('addUser', JSON.parse(event.data))
      }
      // For start chat
      this.socketStartChat.onopen = () => {
        console.log('socket start chat connected')
      }
      // this.socketStartChat.onmessage = (event) => {
      //   this.$store.commit('addPairUsers', JSON.parse(event.data))
      // }
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
  margin: 0
  &.show
    border-radius: 20px 20px 0 0
.dropdown-menu
  border-radius: 0 0 10px 10px
  li
    cursor: pointer
  a
    text-decoration: none
</style>
