from plotly.offline import plot
import plotly.graph_objs as go
import pandas as pd
import requests
import plotly.plotly as py
import plotly.figure_factory as ff
from apps.tasks.models import Task, Status

def gantt(data):
        tasks = []
        for t in data:
                status = t.status.all()
                f_ini = t.fecha_ini.strftime('%Y-%m-%d')
                f_fin = t.fecha_fin.strftime('%Y-%m-%d')
                st = str(status[0].percent)+ ' %' 
                tasks.append([t.nombre, f_ini, f_fin, st])

        df = pd.DataFrame(tasks, columns=['Task', 'Start', 'Finish', 'Complete'])

        colors = {'0 %': 'rgb(255,0,0)',
                '25 %': 'rgb(255,69,0)',
                '50 %': 'rgb(255,215,0)',
                '75 %': 'rgb(154,205,50)',
                '100 %': 'rgb(0,128,0)'}

        figg = ff.create_gantt(df, colors=colors, index_col='Complete',
                        show_colorbar=True, bar_width=0.3,
                        showgrid_x=True, showgrid_y=True, title='Gantt')

        plot_div = plot(figg, output_type='div',filename='gantt-simple-gantt-chart')
        return plot_div

