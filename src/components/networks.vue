<template>
  <div class='network-graph' :class="{'hide': $store.state.isFullWidthContent}">
    <d3-network :net-nodes="nodes" :net-links="links" :options="options">
    </d3-network>
  </div>
</template>

<script>
import D3Network from 'vue-d3-network'

export default {
  name: 'networks',
  data () {
    return {
      nodes: [],
      links: [],
      options:
      {
        force: 3000,
        nodeSize: 20,
        nodeLabels: true,
        linkWidth: 2
      }
    }
  },
  components: {
    D3Network
  },
  watch: {
    '$store.state.user' () {
      this.nodes.push(this.$store.state.user)
      this.addColorNode()
    },
    '$store.state.usersPair' () {
      this.links.push(this.$store.state.usersPair)
    }
  },
  methods: {
    addColorNode () {
      this.nodes.forEach((node) => {
        node._color = '#a4a9ff'
      })
    }
  }
}
</script>

<style scoped lang='sass'>
.network-graph
  width: 50%
  z-index: 1
  transition: .3s
  &.hide
    width: 0
    transition: .3s

path.link
  stroke: red!important
  fill: red!important

</style>
