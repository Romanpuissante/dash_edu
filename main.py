import pandas as pd
from datetime import date



df = pd.DataFrame(dtype={
    "date_start": int
})

print(1)
# from dash import Dash, dcc, html
# import app.router

# app = Dash(__name__, suppress_callback_exceptions=True)

# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])


# if __name__ == '__main__':
#     app.run_server(debug=True)