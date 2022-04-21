from dash import dcc, html, callback, Output, Input
from app.data import page1


result = page1.create_data()

layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(result["list"], result["value"], id='page-1-dropdown'),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

@callback(Output('page-1-content', 'children'),
              [Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return f'You have selected {value}'
