from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import figure, output_file, show

output_file("circle_v1.html")

plot = figure(plot_width=400, plot_height=400, match_aspect=True, x_range=[-1.1,1.1], y_range=[-1.1,1.1], tools='save')
plot.circle(0,0,radius=1,fill_color=None,line_color='OliveDrab')


# slider is here for some other stuff I'll be doing later
callback = CustomJS(code="""
        source.change.emit();
    """)
slider = Slider(start=0, end=360, value=15, step=15, title="degrees", callback=callback)
layout = column(slider, plot)

show(layout)
