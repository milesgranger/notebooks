import requests
from datetime import datetime
from math import radians
from pytz import timezone
from bs4 import BeautifulSoup
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, DatetimeTickFormatter


def extract_value():
    """Grabs current bitcoin value"""
    response = requests.get('http://bitcoincharts.com/markets/okcoinCNY.html', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')
    value = float(soup.find_all('p')[0].span.text)
    return value


def update():
    """Update the data at every N periodic callback time"""
    new_data = dict(x=[datetime.now(tz=timezone('Europe/Oslo'))],
                    y=[extract_value()])
    source.stream(new_data=new_data, rollover=25)
    print(source.data)



# Create figure
fig = figure(x_axis_type='datetime')

# data source
source = ColumnDataSource(dict(x=[], y=[]))

# Glyphs
fig.circle(x='x', y='y', color='red', line_color='blue', source=source)
fig.line(x='x', y='y', source=source)

# Format the xaxis
fig.xaxis.formatter = DatetimeTickFormatter(formats=dict(seconds=['%Y-%m-%d-%H-%M-%S'],
                                                         minsec=['%Y-%m-%d-%H-%M-%S'],
                                                         minutes=['%Y-%m-%d-%H-%M-%S'],
                                                         hourmin=['%Y-%m-%d-%H-%M-%S'],
                                                         hours=['%Y-%m-%d-%H-%M-%S'],
                                                         days=['%Y-%m-%d-%H-%M-%S'],
                                                         months=['%Y-%m-%d-%H-%M-%S'],
                                                         years=['%Y-%m-%d-%H-%M-%S'],))

fig.xaxis.major_label_orientation = radians(45)  # deg. to radians

curdoc().add_root(fig)
curdoc().add_periodic_callback(update, 2000)