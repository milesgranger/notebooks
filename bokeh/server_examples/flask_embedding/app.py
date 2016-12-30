from flask import Flask, render_template
from BasicLine import js, div, cdn_css, cdn_js
from random_generator import fig
from bokeh.embed import autoload_server

app = Flask(__name__)

@app.route('/static_plot')
def static_plot():
    return render_template('static_plot.html', js=js, div=div,
                           cdn_css=cdn_css, cdn_js=cdn_js)

@app.route('/live_plot')
def live_plot():
    bokeh_script = autoload_server(None,
                                   app_path='/random_generator')  # None could also be the figure obj.
    return render_template('live_plot.html', bokeh_script=bokeh_script)


if __name__ == '__main__':
    app.run(debug=True)