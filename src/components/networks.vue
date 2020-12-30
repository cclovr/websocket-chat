<template>
  <div class='network-graph' id='network-graph' :class="{'hide': $store.state.isFullWidthContent}">
  </div>
</template>

<script>
import * as d3 from 'd3'
export default {
  name: 'networks',
  data () {
    return {
      nodes: [],
      links: this.$store.state.usersPair,
      width: 750,
      height: 400
    }
  },
  watch: {
    '$store.state.user' () {
      this.init('new-nodes')
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init (isNewNodes) {
      if (isNewNodes === 'new-nodes') {
        this.nodes.push(this.$store.state.user)
      }
      const linksObj = this.links.map(d => Object.create(d))
      const nodesObj = this.nodes.map(d => Object.create(d))
      const simulation = d3.forceSimulation(nodesObj)
        .force('link', d3.forceLink(linksObj).id(d => d.id))
        .force('collide', d3.forceCollide(function () {
          return 50
        }))
        .force('center', d3.forceCenter(this.width / 2, this.height / 2))
        .on('tick', ticked)

      const svg = d3.select('#network-graph').append('svg')
        .attr('viewBox', [0, 0, this.width, this.height])

      let link = svg.append('g')
        .attr('stroke-width', 4)
        .selectAll('line')
        .data(linksObj)
        .join('line')
      repeat()

      const node = svg.append('g')
        .attr('stroke', '#fff')
        .attr('stroke-width', 1.5)
        .selectAll('circle')
        .data(nodesObj)
        .join('circle')
        .attr('r', 9)
        .attr('fill', '#a4a9ff')

      node.append('title')
        .text(d => d.id)

      // simulation.on('tick', () => {
      //   link
      //     .attr('x1', d => d.source.x)
      //     .attr('y1', d => d.source.y)
      //     .attr('x2', d => d.target.x)
      //     .attr('y2', d => d.target.y)
      //
      //   node
      //     .attr('cx', d => d.x)
      //     .attr('cy', d => d.y)
      // })

      function repeat () {
        link
          .attr('stroke', '#a4a9ff')
          .transition()
          .duration(1000)
          .attr('stroke', '#d6d0e8')
          .transition()
          .duration(1000)
          .attr('stroke', '#a4a9ff')
          .on('end', repeat)
      }

      function ticked () {
        simulation.on('tick', () => {
          link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y)

          node
            .attr('cx', d => d.x)
            .attr('cy', d => d.y)
        })
      }
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
</style>
