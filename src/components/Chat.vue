<template>
    <div class="chat block" :class="{'full-width': fullWidth}">
      <Arrow></Arrow>
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

</style>
