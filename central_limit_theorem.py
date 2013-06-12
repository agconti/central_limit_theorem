# central limit theroem vis in python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation


def lvl(d):
  # given a triangle element index, calculate it's y depth within
  # the larger peramind of triangles
  d = d + 1
  i = 0 
  n = 1
  
  while (i + n) < d:
    i += n
    n += 1
  
  return n - 1


def pos(l):
  # give a y level depth within the peramind of triangles, calculate
  # the first triangle element index at that level
  l = l + 1
  n = 0
  i = 0
  
  while( n < l):
    i += n
    n += 1 
  return i


speed = 500
frame
histogram_height = 100
def init():
  def histo(bins, rwidth):
    '''
    our hist. maybe well use this with d3py / vega / vincent
    '''
    plt.hist(x, bins=10, range=None, normed=False, weights=None,
           cumulative=False, bottom=None, histtype='bar', align='mid',
           orientation='vertical', rwidth=None, log=False,
           color='steelblue', label=None, stacked=False,
           **kwargs)

  def drop_a_ball():
  
  

  def animate():
    c = d3.select(this)
    d = c.datum()
    if(d.lvl > bins - 2) {
      # drop the ball into its histogram bin
      c.transition()
        .duration(speed / 2)
        .attr('cy', def(d): return (d.lvl * sy + 20 + histogram_height) + 'px')
        .style('opacity', '0.0')
        .remove() # remove the balls once they're invisible
      values.push( bins / 2 + d.pos / 2)
      update()
      return
    
    if(d.lvl === -1) d.pos = 0 # when the ball drops into the first position
    else if( Math.random() > 0.5 ) d.pos += 1
    else d.pos--
    d.lvl += 1
    c.datum(d)
    c.transition()
      .ease('bounce')
      .attr('cx', def(d): return (d.pos * sx / 2) + 'px' )
      .attr('cy', def(d): return (d.lvl * sy + sy) + 'px' )
      .each('end', animate)
    .duration(speed)
  

  x = d3.scale.linear()
      .domain([0, bins])
      .range([0, width - margin.left - margin.right])
  formatCount = d3.format(",.0f")
  data = d3.layout.histogram().bins(d3.range(0,bins + 1))(values)
  histogram = d3.select('svg')
    .append('g')
    .attr('transform','translate(' + margin.left + ',' + histogram_y + ')')

  xAxis = d3.svg.axis()
    .scale(x)
    .ticks(bins)
    .orient('bottom')

  bar = histogram.selectAll('.bar')
    .data(data)
    .enter().append('g')
      .attr('class', 'bar')

  bar.append('rect')
    .attr('x', 1)
    .attr('width', x(data[0].dx) - 1)

  bar.append('text')
    .attr('dy', '.5em')
    .attr('y', 10)
    .attr('x', x(data[0].dx) / 2)
    .attr('text-anchor', 'middle')

  histogram.append('g')
    .attr('class', 'x axis')
    .attr('transform', 'translate(0,' + (histogram_height) + ')')
    .call(xAxis)

  def update():
    data = d3.layout.histogram().bins(d3.range(0, bins + 1))(values)
    bar = histogram.selectAll('.bar')
    y = d3.scale.linear()
      .domain([0, d3.max(data.map(def(d): return d.y ))])
      .range([histogram_height, 0])
    bar.data(data)
      .transition()
      .duration(speed)
      .attr('transform', def(d): return 'translate(' + x(d.x) + ',' + y(d.y) + ')' )
      .select('rect')
        .attr('height', def(d): return (histogram_height - y(d.y)) )
    bar.select('text')
      .text(def(d): return Math.floor(d.y / values.length * 100) + '%' )
  
  update()


def interval():
  if(frame) frame()
  setTimeout(interval, speed)



# setup buttons
document.getElementsByName('speed')[0].onchange = def(e):
  speed = e.target.value

document.getElementsByName('bins')[0].onchange = restart

def restart(e):
  init(Number( e ? e.target.value : 5), Number(document.getElementById('central-limit-therom-vis').offsetWidth))


restart()
