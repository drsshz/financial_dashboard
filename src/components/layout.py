from dash import Dash, html
from src.components import companies_dropdown
from src.components import (
    year_dropdown,
    month_dropdown,
    bar_chart,
    pie_chart,
)
from src.data_processor.source import DataSource


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, source),
                    month_dropdown.render(app, source),
                    companies_dropdown.render(app, source),
                ],
            ),
            html.Hr(),
            bar_chart.render(app, source),
            pie_chart.render(app, source),
        ],
    )