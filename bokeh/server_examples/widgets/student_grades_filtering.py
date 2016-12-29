from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.widgets import Select, Slider
from bokeh.layouts import layout

# column data sources
source = ColumnDataSource(dict(average_grades=[7, 8, 10],
                               exam_grades=[6, 9, 8],
                               student_names=['Stephan', 'Helder', 'Riazudidn']))
source_original = ColumnDataSource(dict(average_grades=[7, 8, 10],
                                        exam_grades=[6, 9, 8],
                                        student_names=['Stephan', 'Helder', 'Riazudidn']))

# Create figure with ranges
fig = figure(x_range=Range1d(start=0, end=12),
             y_range=Range1d(start=0, end=12))

# Add labels for glyphs
labels = LabelSet(x='average_grades',
                  y='exam_grades',
                  text='student_names',
                  source=source,
                  y_offset=5, x_offset=5)
fig.add_layout(labels)


# glyphs
fig.circle(x='average_grades',
           y='exam_grades',
           source=source,
           size=8)

# Create filtering option
def filter_grades(attr, old, new):

    # Change the source data used by the figure.circle depending on current slider state
    source.data = {key: [value for i, value in enumerate(source_original.data[key])
                         if source_original.data['exam_grades'][i] >= slider.value]
                   for key in source_original.data}

def update_labels(attr, old, new):
    '''Update the labels'''
    print 'Attr: {}, Old: {}, New: {}'.format(attr, old, new)
    labels.text = select.value

# Create select widget
select = Select(title='Attribute', options=[('average_grades', 'Avg Grades'),
                                            ('exam_grades', 'Exam Grades'),
                                            ('student_names', 'Student Names')])
select.on_change('value', update_labels)


# Create slider widget
slider = Slider(start=min(source_original.data['exam_grades']) - 1,
                end=max(source_original.data['exam_grades']) + 1,
                value=8,
                step=0.1,
                title='Exam Grade: ')
slider.on_change('value', filter_grades)


# Create layout of widgets
lay_out = layout([
    [select],
    [slider]
])

# Add figure and widget layout
curdoc().add_root(fig)
curdoc().add_root(lay_out)
