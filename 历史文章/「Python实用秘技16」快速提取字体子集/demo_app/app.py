import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

app = dash.Dash(__name__)

# 读入示例文本内容
with open('./将进酒.txt', encoding='utf-8') as t:
    source_text = t.read()

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            fac.AntdSpace(
                [
                    fac.AntdText(
                        line,
                        style={
                            'fontFamily': '钟齐志莽行书mini',
                            'fontSize': 38
                        }
                    )
                    for line in
                    source_text.split('\n')
                ],
                direction='vertical',
                style={
                    'width': '100%'
                }
            ),
            shadow='always-shadow-light',
            style={
                'padding': '24px',
                'borderRadius': 10,
                'width': 'fit-content',
                'margin': '0 auto',
                'backgroundImage': 'url("assets/金箔效果背景.jpg")',
                '-webkit-background-clip': 'text',
                '-webkit-text-fill-color': 'transparent'
            }
        )
    ],
    style={
        'paddingTop': 40
    }
)


if __name__ == '__main__':
    app.run()
