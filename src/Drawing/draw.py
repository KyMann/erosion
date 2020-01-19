from progress.spinner import Spinner
import plotly.offline as plotly
import plotly.graph_objs as go

import pandas as pd

def draw(zDataCSVName):
    z_data = pd.read_csv('../Erosion/' + zDataCSVName)

    data = [
        go.Surface(
            z=z_data.as_matrix(),
            contours=go.surface.Contours(
                z=go.surface.contours.Z(
                    show=True,
                    usecolormap=True,
                    highlightcolor="#42f462",
                    project=dict(z=True)
                )
            )
        )
    ]

    layout = go.Layout(
        title='Testing Plotly',
        autosize=False,
        width=500,
        height=500,
        margin={
            'l':60,
            'r':50,
            'b':65,
            't':90
        }
    )

    fig=go.Figure(data=data, layout=layout)
    spinner = Spinner('Drawing ')
    plotly.iplot(fig, filename='elevations-3d-suface')
    spinner.finish()
    
draw('test.csv')