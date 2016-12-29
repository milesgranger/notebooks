from __future__ import print_function
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from random import randrange

fig = figure()

source = ColumnDataSource(dict(x=list(),
                               y=list())
                          )

fig.circle(x='x', y='y', color='red', size=5, line_color='blue', source=source)
fig.line(x='x', y='y', source=source)

# Starter points...
x, y = 0, 5


def update():
    """Steam data into server"""
    global x, y
    x += 1
    y = (y * 0.95) + (randrange(1, 10) * 0.05)

    new_data = dict(x=[x], y=[y])
    source.stream(new_data=new_data, rollover=250)  # rollover == how many datapoints to keep
    print(source.data)


curdoc().add_root(fig)
curdoc().add_periodic_callback(update, 100)  # Milliseconds