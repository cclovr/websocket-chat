<template>
    <div class="chat block" :class="{'full-width': fullWidth}">
      <Arrow></Arrow>
      <div class="chat-wrap">
        <h1>Chat</h1>
        <div class="chat-container">
          <div class="chat-items-wrap">
            <div class="chat-item">
              <span class="name">Lorem</span>
              <p class="description">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus blanditiis deleniti distinctio eius excepturi, iure numquam quasi ut voluptas voluptatibus?</p>
            </div>
            <div class="chat-item">
              <span class="name">Lorem ipsum.</span>
              <p class="description">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus blanditiis deleniti distinctio eius excepturi, iure numquam quasi ut voluptas voluptatibus?</p>
            </div>
            <div class="chat-item">
              <span class="name">Lorem ipsum.</span>
              <p class="description">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus blanditiis deleniti distinctio eius excepturi, iure numquam quasi ut voluptas voluptatibus?</p>
            </div>
          </div>
          <div class="chat-main">
            <div class="interlocutor-message">Lorem ipsum dolor sit amet.</div>
            <div class="my-message">Lorem ipsum dolor sit amet.</div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import Arrow from '../components/arrow.vue'
import {eventBus} from '../main'
export default {
  name: 'Chat',
  components: {
    Arrow
  },
  data () {
    return {
      fullWidth: false
    }
  },
  mounted () {
    this.listenFullWidth()
  },
  methods: {
    listenFullWidth () {
      eventBus.$on('isFullWidth', data => {
        this.fullWidth = data
      })
    }
  }
}
</script>

<style scoped lang="sass">
.chat
  &-container
    display: flex
    background: var(--opacity-white)
    height: calc(100% - 60px)
    border-radius: var(--border-radius)
    box-shadow: var(--box-shadow)
    padding: 10px
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
    max-width: 230px
    cursor: pointer
    /*position: absolute*/
    /*animation-iteration-count: 1*/
    /*animation-duration: 8s*/
    /*animation-fill-mode: forwards*/
    /*animation-name: msg*/
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
    margin-left: 20px
    background: white
    border-radius: var(--border-chat)
    padding: 10px 20px
    position: relative

// Animation message
  <!--@keyframes msg1-->
  <!--  0%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height))-->
  <!--    left: -4em-->
  <!--    transform: scale(0)-->
  <!--  5%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height))-->
  <!--    left:-->
  <!--    transform: scale(1)-->
  <!--  12%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height))-->
  <!--  17%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg2-height))-->
  <!--  30%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg2-height))-->
  <!--  35%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg2-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg3-height))-->
  <!--  49%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg2-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg3-height))-->
  <!--  54%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg2-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg3-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg4-height))-->
  <!--  70%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg2-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg3-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg4-height))-->
  <!--  75%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg2-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg3-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg4-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg5-height))-->
  <!--  95%-->
  <!--    top: calc(var(&#45;&#45;msg-content-height) - var(&#45;&#45;msg1-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg2-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg3-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg4-height) - var(&#45;&#45;msg-spacing) - var(&#45;&#45;msg5-height))-->
  <!--  100%-->
  <!--    top: 0-->
  <!--    left: 0-->
</style>
