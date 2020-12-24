<template>
  <div class='network-graph' id='network-graph' :class="{'hide': hide}">
  </div>
</template>

<script>
import * as d3 from 'd3'
import {eventBus} from '../main'

export default {
  name: 'networks',
  data () {
    return {
      connection: null,
      loadData: {},
      width: 750,
      height: 400,
      margin: {
        top: 50,
        right: 50,
        left: 50,
        bottom: 50
      },
      links: [],
      hide: false
    }
  },
  mounted () {
    this.hideNetworks()
    this.init()
  },
  methods: {
    hideNetworks () {
      eventBus.$on('isFullWidth', data => {
        this.hide = data
        console.log(this.hide)
      })
    },
    init () {
      const nodes = [
        {
          id: 'Andrew',
          group: 1
        },
        {
          id: 'Stark',
          group: 1
        },
        {
          id: 'Lannister',
          group: 2
        },
        {
          id: 'Anna',
          group: 2
        }
      ]
      const links = [
        {
          source: 'Andrew',
          target: 'Anna'
        },
        {
          source: 'Andrew',
          target: 'Stark'
        },
        {
          source: 'Lannister',
          target: 'Stark'
        },
        {
          source: 'Anna',
          target: 'Lannister'
        }
      ]

      const linksObj = links.map(d => Object.create(d))
      const nodesObj = nodes.map(d => Object.create(d))
      const simulation = d3.forceSimulation(nodesObj)
        .force('link', d3.forceLink(linksObj).id(d => d.id))
        .force('charge', d3.forceManyBody())
        .force('center', d3.forceCenter(this.width / 2, this.height / 2))

      const svg = d3.select('#network-graph').append('svg')
        .attr('viewBox', [0, 0, this.width, this.height])

      const link = svg.append('g')
        .attr('stroke', '#fff')
        .attr('stroke-opacity', 1)
        .selectAll('line')
        .data(linksObj)
        .join('line')
        .attr('stroke-width', d => Math.sqrt(d.value))

      const node = svg.append('g')
        .attr('stroke', '#fff')
        .attr('stroke-width', 1.5)
        .selectAll('circle')
        .data(nodesObj)
        .join('circle')
        .attr('r', 9)
        .attr('fill', '#a4a9ff')
        .call(drag(simulation))

      node.append('title')
        .text(d => d.id)

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

      function drag (simulation) {
        function dragstarted (event) {
          if (!event.active) simulation.alphaTarget(0.3).restart()
          event.subject.fx = event.subject.x
          event.subject.fy = event.subject.y
        }

        function dragged (event) {
          event.subject.fx = event.x
          event.subject.fy = event.y
        }

        function dragended (event) {
          if (!event.active) simulation.alphaTarget(0)
          event.subject.fx = null
          event.subject.fy = null
        }

        return d3.drag()
          .on('start', dragstarted)
          .on('drag', dragged)
          .on('end', dragended)
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
