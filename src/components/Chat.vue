<template>
    <div class="chat block" :class="{'full-width': $store.state.isFullWidthContent}">
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
            <div class="my-message">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid consequatur facere fugiat laboriosam, minima nesciunt nihil pariatur possimus ratione sequi?</div>
            <div class="my-message">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid consequatur facere fugiat laboriosam, minima nesciunt nihil pariatur possimus ratione sequi?</div>
            <div class="interlocutor-message">Lorem ipsum dolor sit amet.</div>
            <div class="interlocutor-message">Lorem ipsum dolor sit amet.</div>
            <div class="my-message">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid consequatur facere fugiat laboriosam, minima nesciunt nihil pariatur possimus ratione sequi?</div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import Arrow from '../components/arrow.vue'
export default {
  name: 'Chat',
  components: {
    Arrow
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
    margin-left: 20px
    background: white
    border-radius: var(--border-chat)
    padding: 10px 20px
    position: relative
    overflow: auto
    &::-webkit-scrollbar
      width: 7px
      background-color: #f9f9fd
    &::-webkit-scrollbar-thumb
      background-color: #b3b3b3
      border-radius: 5px

  .interlocutor-message,
  .my-message
    animation: msg 1s
    padding: 15px
    border-radius: 10px
    display: inline-block
    margin-bottom: 10px
    max-width: 400px

  .interlocutor-message
    background: #c5dcff
    float: left

  .my-message
    background: #ebebeb
    float: right

// Animation message
@keyframes msg
  0%
    opacity: 0
  100%
    opacity: 1
</style>
