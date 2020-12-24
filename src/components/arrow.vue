<template>
  <img src="../assets/arrow.svg"
       alt="arrow" class="arrow"
       @click="setFullWidth()"
       :class="{'rotate-arrow': fullWidth}">
</template>

<script>
import {eventBus} from '../main'

export default {
  name: 'arrow',
  data () {
    return {
      fullWidth: false
    }
  },
  methods: {
    setFullWidth () {
      this.fullWidth = !this.fullWidth
      eventBus.$emit('isFullWidth', this.fullWidth)
    }
  }
}
</script>

<style scoped lang="sass">
.arrow
  position: absolute
  width: 30px
  top: 20px
  right: 20px
  cursor: pointer
  &.rotate-arrow
    transform: rotate(-180deg)
</style>
