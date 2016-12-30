from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN

x = range(1, 6)
y = range(5, 10)

fig = figure()
fig.line(x, y)

js, div = components(fig)
cdn_js=CDN.js_files[0]
cdn_css=CDN.css_files[0]
