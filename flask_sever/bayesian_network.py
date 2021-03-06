from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import os, sys


app = Dash(__name__,
           title='에코 차징 플레이스',
           update_title='데이터를 불러오는 중 입니다.',
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[{
                       'content': 'width=device-width, initial-scale=0.5, maximum-scale=1.2, minimum-scale=0.5,'}]
           )

server = app.server

df_economy = pd.DataFrame({
    "경제적": ["True", "False"],
    "적합확률": [80, 20],
    "경제적 요소": ["True", "False"]
})
df_society = pd.DataFrame({
    "사회적": ["True", "False"],
    "적합확률": [70, 30],
    "사회적 요소": ["True", "False"]
})
df_environment = pd.DataFrame({
    "환경적": ["True", "False"],
    "적합확률": [80, 20],
    "환경적 요소": ["True", "False"]
})
df_technique = pd.DataFrame({
    "기술적": ["True", "False"],
    "적합확률": [75, 35],
    "기술적 요소": ["True", "False"]
})

fig1 = px.bar(df_economy, x="경제적", y="적합확률", color="경제적 요소")
fig1.update_yaxes(visible=False)
fig2 = px.bar(df_society, x="사회적", y="적합확률", color="사회적 요소")
fig2.update_yaxes(visible=False)
fig3 = px.bar(df_environment, x="환경적", y="적합확률", color="환경적 요소")
fig3.update_yaxes(visible=False)
fig4 = px.bar(df_technique, x="기술적", y="적합확률", color="기술적 요소")
fig4.update_yaxes(visible=False)

fig1.update_layout({
    'paper_bgcolor': '#E9EEF6',
}, title_text="전기-경제적", title_font_size=22, showlegend=False, margin_l=10, margin_r=10, legend_y=1.5,
    legend_xanchor='right',
    legend={'title_text': ''}, font_family='NanumSquare')
fig2.update_layout({
    'paper_bgcolor': '#E9EEF6',
}, title_text="전기-경제적", title_font_size=22, showlegend=False, margin_l=10, margin_r=10, legend_y=1.5,
    legend_xanchor='right',
    legend={'title_text': ''}, font_family='NanumSquare')
fig3.update_layout({
    'paper_bgcolor': '#E9EEF6',
}, title_text="전기-경제적", title_font_size=22, showlegend=False, margin_l=10, margin_r=10, legend_y=1.5,
    legend_xanchor='right',
    legend={'title_text': ''}, font_family='NanumSquare')
fig4.update_layout({
    'paper_bgcolor': '#E9EEF6',
}, title_text="전기-경제적", title_font_size=22, showlegend=False, margin_l=10, margin_r=10, legend_y=1.5,
    legend_xanchor='right',
    legend={'title_text': ''}, font_family='NanumSquare')

header = html.Div(
    html.Img(src="assets/logo.png", height="120px")
)

environment_chart = html.Div([
    # 환경적 하위요소
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                id='1',
                figure=fig4,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                id='2',
                figure=fig2,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                id='81',
                figure=fig4,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
    ]),
    # dbc.Row(),
    # dbc.Row([
    #     dbc.Col([
    #         dcc.Graph(
    #             className="standard_1",
    #             id='3',
    #             figure=fig4,
    #         )
    #     ], xs=3, sm=3, md=3, lg=6, xl=6, style={'padding': '12px'}),
    #     dbc.Col([
    #         dcc.Graph(
    #             className="standard_1",
    #             id='4',
    #             figure=fig1,
    #         )
    #     ], xs=3, sm=3, md=3, lg=6, xl=6, style={'padding': '12px'}),
    # ]),
    # 환경적 상위요소
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig3,
            )
        ], xs=12, sm=12, md=12, lg=12, xl=12, style={'margin-top': '2%'})
    ])

])
economy_chart = html.Div([
    # 경제적 하위요소
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig2,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig1,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig1,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
    ]),
    # dbc.Row([
    #     dbc.Col([
    #         dcc.Graph(
    #             className="standard_1",
    #             figure=fig4,
    #         )
    #     ], xs=3, sm=3, md=6, lg=6, xl=6, style={'padding': '12px'}),
    #     dbc.Col([
    #         dcc.Graph(
    #             className="standard_1",
    #             figure=fig3,
    #         )
    #     ], xs=3, sm=3, md=6, lg=6, xl=6, style={'padding': '12px'}),
    # ]),
    dbc.Row([  # 경제적 상위요소
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig1,
            )
        ], xs=12, sm=12, md=12, lg=12, xl=12, style={'margin-top': '2%'})
    ])
], )
technique_chart = html.Div([

    # 기술적 상위요소
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig4,
            )
        ], xs=12, sm=12, md=12, lg=12, xl=12, style={'margin-bottom': '2%'})
    ]),

    # 기술적 하위요소
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                id='9',
                figure=fig2,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                id='10',
                figure=fig1,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                id='77',
                figure=fig1,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4)
    ]),
    # dbc.Row([
    #     dbc.Col([
    #         dcc.Graph(
    #             className="standard_1",
    #             id='11',
    #             figure=fig4,
    #         )
    #     ], xs=3, sm=3, md=6, lg=6, xl=6, style={'padding': '12px'}),
    #     dbc.Col([
    #         dcc.Graph(
    #             className="standard_1",
    #             id='12',
    #             figure=fig3,
    #         )
    #     ], xs=3, sm=3, md=6, lg=6, xl=6, style={'padding': '12px'}),
    # ])

])
society_chart = html.Div([

    # 사회적 상위요소
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig2,
            )
        ], xs=12, sm=12, md=12, lg=12, xl=12, style={'margin-bottom': '2%'})

    ]),

    # 사회적 하위요소
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                id='13',
                figure=fig3,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig2,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dcc.Graph(
                className="standard_1",
                figure=fig2,
            )
        ], xs=4, sm=4, md=4, lg=4, xl=4),
    ]),
    # dbc.Row([
    #     dbc.Col([
    #         dcc.Graph(
    #             className="standard_1",
    #             id='15',
    #             figure=fig4,
    #         )
    #     ], xs=3, sm=3, md=6, lg=6, xl=6, style={'padding': '12px'}),
    #     dbc.Col([
    #         dcc.Graph(
    #             className="standard_1",
    #             id='16',
    #             figure=fig1,
    #         )
    #     ], xs=3, sm=3, md=6, lg=6, xl=6, style={'padding': '12px'}),
    # ])

])

app.layout = html.Div(className='main', children=[
    # navbar,
    header,
    dbc.Row([
        dbc.Col([
            html.H1("환경적"),
            environment_chart
        ], className="B_chart", xs=5, sm=5, md=5, lg=5, xl=5, style={'padding': '1%'}),
        # dbc.Col(xs=3, sm=3,md=3,lg=3, xl=3),
        dbc.Col(xs=2, sm=2, md=2, lg=2, xl=2),
        dbc.Col([
            html.H1("경제적"),
            economy_chart
        ], className="B_chart", xs=5, sm=5, md=5, lg=5, xl=5, style={'padding': '1%'})
    ]),

    # 최종확률
    dbc.Row([
        dbc.Col(xs=4, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            html.H1("최종확률"),
            dcc.Graph(
                className="standard_1",
                figure=fig2, id="last_stand"
            )
        ], style={'padding': '1%', 'margin': '1%'}, xs=4, sm=4, md=4, lg=4, xl=4, className="B_chart"),
        dbc.Col(xs=4, sm=4, md=4, lg=4, xl=4),
    ]),

    dbc.Row([
        dbc.Col([
            html.H1("사회적"),
            society_chart
        ], className="B_chart", xs=5, sm=5, md=5, lg=5, xl=5, style={'padding': '1%'}),
        dbc.Col(xs=2, sm=2, md=2, lg=2, xl=2),
        # dbc.Col(xs=3, sm=3,md=3,lg=3, xl=3),
        dbc.Col([
            html.H1("기술적"),
            technique_chart
        ], className="B_chart", xs=5, sm=5, md=5, lg=5, xl=5, style={'padding': '1%'})
    ])
])

layout = app.layout
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=9999, debug=True)