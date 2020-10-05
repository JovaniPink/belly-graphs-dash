import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        html.H1("Stock Tickers"),
        dcc.Dropdown(
            id="my-dropdown",
            className="",
            options=[
                {"label": "Coke", "value": "COKE"},
                {"label": "Tesla", "value": "TSLA"},
                {"label": "Apple", "value": "AAPL"},
            ],
            value="COKE",
        ),
        dcc.Graph(id="my-graph"),
        html.H2("Table"),
        dbc.Table(
            [
                html.Thead(
                    html.Tr(
                        [html.Th("#"), html.Th("First name"), html.Th("Last name"),]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Th("1", scope="row"),
                                html.Td("Tom"),
                                html.Td("Cruise"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th("2", scope="row"),
                                html.Td("Jodie"),
                                html.Td("Foster"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th("3", scope="row"),
                                html.Td("Chadwick"),
                                html.Td("Boseman"),
                            ]
                        ),
                    ]
                ),
            ],
            responsive=True,
            striped=True,
            hover=True,
        ),
    ],
    style={"width": "500"},
)
