from dash import Input, Output, callback
from app.layouts import index_page, page1, page2

# Update the index
@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page1.layout
    elif pathname == '/page-2':
        return page2.layout
    else:
        return index_page.layout
    # You could also return a 404 "URL not found" page here