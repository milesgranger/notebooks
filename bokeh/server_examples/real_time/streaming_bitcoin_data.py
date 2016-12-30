import requests
from bs4 import BeautifulSoup
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource


def extract_value():
    """Grabs current bitcoin value"""
    response = requests.get('http://bitcoincharts.com/markets/okcoinCNY.html', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')
    value = float(soup.find_all('p')[0].span.text)
    return value


def update():
    new_data = dict(x=[source.data['x'][-1] + 1],
                    y=[extract_value()])
    source.stream(new_data=new_data, rollover=25)
    print(source.data)


# Create figure
fig = figure()

# data source
source = ColumnDataSource(dict(x=[1], y=[extract_value()]))

# Glyphs
fig.circle(x='x', y='y', color='red', line_color='blue', source=source)
fig.line(x='x', y='y', source=source)

curdoc().add_root(fig)
curdoc().add_periodic_callback(update, 5000)
