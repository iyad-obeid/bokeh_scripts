from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import figure, output_file, show
from math import cos, sin, radians, pi

output_file("callback.html")

a = 20*pi/180 #degrees
x = [cos(a), cos(a)]
y = [sin(a), -sin(a)]

xx = [cos(radians(xx)) for xx in range(-1,360)]
yy = [sin(radians(yy)) for yy in range(-1,360)]

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(plot_width=400, plot_height=400, match_aspect=True, x_range=[-1.1,1.1], y_range=[-1.1,1.1], tools='save')
plot.line(xx,yy,color="navy")
plot.circle('x', 'y', source=source, size=20, line_alpha=0.6)
# plot.axis.visible = False
# plot.xgrid.grid_line_color = None
# plot.ygrid.grid_line_color = None

callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var a = Math.PI * cb_obj.value / 180
        x = data['x']
        y = data['y']
        x[0] = Math.cos(a)
        y[0] = Math.sin(a)
        x[1] = Math.cos(a)
        y[1] = -Math.sin(a)
        source.change.emit();
    """)

slider = Slider(start=0, end=360, value=15, step=15, title="degrees", callback=callback)

layout = column(slider, plot)

show(layout)

#        for (i = 0; i < x.length; i++) {
#            y[i] = Math.pow(x[i], f)
#        }
#		x = [Math.cos(a), Math.cos(a)]
#		y = [Math.sin(a), -Math.sin(a)]
