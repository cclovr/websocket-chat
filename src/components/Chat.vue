<template>
    <div class="chat block" :class="{'full-width': $store.state.isFullWidthContent}">
      <Arrow></Arrow>
      <div class="chat-wrap">
        <h1>Chat</h1>
        <div class="chat-container">
          <div class="chat-head">
            <span class="name">{{ username.id }}</span>
          </div>
          <div class="chat-main">
            <div class="interlocutor-message"
                 v-for="(message, index) in messages"
                 :key="index"
                 :class="{'my-message': message.id === myUsername}"
            >
             {{ message.message }}
            </div>
          </div>
          <form class="input-wrapper" @submit.prevent="sendMessage()">
            <input type="text" class="form-input" placeholder="type message" v-model="message">
            <button type="submit" class="btn-send-message">
              <img src="../assets/send_message.svg" alt="send_message">
            </button>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
import Arrow from '../components/arrow.vue'
import WS from '../services/ws'

export default {
  name: 'Chat',
  components: {
    Arrow
  },
  data () {
    return {
      username: '',
      socket: WS,
      message: '',
      messages: [],
      myUsername: window.localStorage.getItem('username')
    }
  },
  mounted () {
    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data)
      if (data.name_option === 'message') {
        this.message = ''
        this.messages.push(data)
      }
      if (data.name_option === 'all-users') {
        this.username = data.users.filter(el => {
          return el.id !== this.myUsername
        })[0]
      }
    }
  },
  methods: {
    sendMessage () {
      this.socket.send(JSON.stringify({
        name_option: 'message',
        message: this.message,
        id: this.myUsername
      }))
    }
  }
}
</script>

<style scoped lang="sass">
.chat
  &.full-width
    .chat-item
      max-width: 230px
  &-container
    display: flex
    background: var(--opacity-white)
    height: calc(100% - 60px)
    border-radius: var(--border-radius)
    box-shadow: var(--box-shadow)
    padding: 10px
    position: relative
  &-wrap
    height: 100%
    padding: 20px 0
    width: 100%
  &-item
    background: white
    box-shadow: var(--box-shadow)
    border-radius: var(--border-chat)
    padding: 10px 20px
    width: 100%
    margin-bottom: 10px
    max-width: 100px
    cursor: pointer
    &:last-child
      margin-bottom: 0
    .description
      white-space: nowrap
      overflow: hidden
      text-overflow: ellipsis
      margin-bottom: 0
    .name
      font-weight: bold
  &-main
    width: 100%
    background: white
    padding: 10px 10px 0
    position: relative
    overflow: auto
    display: flex
    flex-direction: column
    height: calc(100% - 100px)
    margin-top: 52px
    &::-webkit-scrollbar
      width: 7px
      background-color: #f9f9fd
    &::-webkit-scrollbar-thumb
      background-color: #b3b3b3
      border-radius: 5px

  .interlocutor-message,
  .my-message
    animation: msg .5s
    padding: 15px
    border-radius: 10px
    display: inline-block
    margin-bottom: 10px
    max-width: 400px

  .interlocutor-message
    background: #c5dcff
    align-self: baseline

  .my-message
    background: #ebebeb!important
    align-self: flex-end!important

  .chat-head
    position: absolute
    z-index: 2
    background: white
    padding: 15px
    width: 100%
    left: 0
    top: 0
    font-size: 20px
    font-weight: bold
    text-transform: capitalize
    border-radius: 15px 15px 0 0
    box-shadow: var(--box-shadow)

  .input-wrapper
    z-index: 2
    bottom: 0
    position: absolute
    background: #ebebeb
    width: 100%
    left: 0
    border-radius: 0 0 15px 15px
    padding: 10px 10px
    box-shadow: var(--box-shadow)

  .btn-send-message
    position: absolute
    width: 33px
    border: none
    outline: none
    height: 33px
    border-radius: 50%
    right: 15px
    top: 14px

// Animation message
@keyframes msg
  0%
    opacity: 0
  100%
    opacity: 1
</style>
