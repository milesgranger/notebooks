from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import randrange

fig = figure(x_range=(0, 11), y_range=(0, 11))

source = ColumnDataSource(dict(x=[], y=[]))

fig.circle(x='x', y='y', size=10, fill_color='red', line_color='blue', source=source)

def update():
    new_data = dict(x=[randrange(1, 10)],
                    y=[randrange(1, 10)])
    source.stream(new_data=new_data, rollover=15)
    print(source.data)

curdoc().add_root(fig)
curdoc().add_periodic_callback(update, 500)