# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 17:09:53 2019

@author: matth
"""

from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("figure.html")

p = figure(plot_width=400, plot_height=400,x_axis_type='datetime')
d = stockTicker("GOOGL","02","2012")
# add a circle renderer with a size, color, and alpha
p.line(d['date'], d['close'], line_width=2)

# show the results
show(p)
