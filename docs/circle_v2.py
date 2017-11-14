from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import figure, output_file, show
from math import cos, sin, radians, pi

output_file("circle_v2.html")

xx = [cos(radians(xx)) for xx in range(-1,360)]
yy = [sin(radians(yy)) for yy in range(-1,360)]

plot = figure(plot_width=400, plot_height=400, match_aspect=True, x_range=[-1.1,1.1], y_range=[-1.1,1.1], tools='save')
plot.line(xx,yy,color="navy")

# slider is here for some other stuff I'll be doing later
callback = CustomJS(code="""
        source.change.emit();
    """)
slider = Slider(start=0, end=360, value=15, step=15, title="degrees", callback=callback)
layout = column(slider, plot)

show(layout)

