from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.layouts import layout

# column data source
source = ColumnDataSource(dict(average_grades=['B+', 'A', 'D-'],
                               exam_grades=['A+', 'C', 'D'],
                               student_names=['Stephan', 'Helder', 'Riazudidn']))

fig = figure(x_range=['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
             y_range=['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'])

# Add labels for glyphs
labels = LabelSet(x='average_grades',
                  y='exam_grades',
                  text='student_names',
                  source=source,
                  y_offset=5, x_offset=5)
fig.add_layout(labels)

fig.circle(x='average_grades',
           y='exam_grades',
           source=source,
           size=8)

def update_labels(attr, old, new):
    '''Update the labels'''
    print 'Attr: {}, Old: {}, New: {}'.format(attr, old, new)
    labels.text = select.value

# Create select widget
select = Select(title='Attribute', options=[('average_grades', 'Avg Grades'),
                                            ('exam_grades', 'Exam Grades'),
                                            ('student_names', 'Student Names')])
select.on_change('value', update_labels)

lay_out = layout([
    [select]
])
curdoc().add_root(fig)
curdoc().add_root(lay_out)