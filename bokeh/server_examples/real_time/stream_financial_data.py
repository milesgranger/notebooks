import requests
from bs4 import BeautifulSoup
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource


# Create figure
fig = figure()

# data source
source = ColumnDataSource(dict(x=[1], y=[]))

# Glyphs
fig.circle(x='x', y='y', color='red', line_color='blue', source=source)
fig.line(x='x', y='y', source=source)


def extract_value():
    """Grabs current bitcoin value"""
    response = requests.get('http://bitcointcharts.com/markets/okcointCNY.html', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')
    value = float(soup.find_all('p')[0].span.text)
    return value


def update():
    new_data = dict(x=[source.data['x'][-1] + 1],
                    y=[extract_value()])
    