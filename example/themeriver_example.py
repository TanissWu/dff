from example.commons import Collector
from pyecharts import options as opts
from pyecharts.charts import Page, ThemeRiver
from pyecharts.commons.utils import JsCode

C = Collector()

themeriver_data = [
    ["2015/11/08", 10, "DQ"],
    ["2015/11/09", 15, "DQ"],
    ["2015/11/10", 35, "DQ"],
    ["2015/11/14", 7, "DQ"],
    ["2015/11/15", 2, "DQ"],
    ["2015/11/16", 17, "DQ"],
    ["2015/11/17", 33, "DQ"],
    ["2015/11/18", 40, "DQ"],
    ["2015/11/19", 32, "DQ"],
    ["2015/11/20", 26, "DQ"],
    ["2015/11/08", 35, "TY"],
    ["2015/11/09", 36, "TY"],
    ["2015/11/10", 37, "TY"],
    ["2015/11/11", 22, "TY"],
    ["2015/11/12", 24, "TY"],
    ["2015/11/13", 26, "TY"],
    ["2015/11/14", 34, "TY"],
    ["2015/11/15", 21, "TY"],
    ["2015/11/16", 18, "TY"],
    ["2015/11/17", 45, "TY"],
    ["2015/11/18", 32, "TY"],
    ["2015/11/19", 35, "TY"],
    ["2015/11/20", 30, "TY"],
    ["2015/11/08", 21, "SS"],
    ["2015/11/09", 25, "SS"],
    ["2015/11/10", 27, "SS"],
    ["2015/11/11", 23, "SS"],
    ["2015/11/12", 24, "SS"],
    ["2015/11/13", 21, "SS"],
    ["2015/11/14", 35, "SS"],
    ["2015/11/15", 39, "SS"],
    ["2015/11/16", 40, "SS"],
    ["2015/11/17", 36, "SS"],
    ["2015/11/18", 33, "SS"],
    ["2015/11/19", 43, "SS"],
    ["2015/11/20", 40, "SS"],
    ["2015/11/14", 7, "QG"],
    ["2015/11/15", 2, "QG"],
    ["2015/11/16", 17, "QG"],
    ["2015/11/17", 33, "QG"],
    ["2015/11/18", 40, "QG"],
    ["2015/11/19", 32, "QG"],
    ["2015/11/20", 26, "QG"],
    ["2015/11/21", 35, "QG"],
    ["2015/11/22", 40, "QG"],
    ["2015/11/23", 32, "QG"],
    ["2015/11/24", 26, "QG"],
    ["2015/11/25", 22, "QG"],
    ["2015/11/08", 10, "SY"],
    ["2015/11/09", 15, "SY"],
    ["2015/11/10", 35, "SY"],
    ["2015/11/11", 38, "SY"],
    ["2015/11/12", 22, "SY"],
    ["2015/11/13", 16, "SY"],
    ["2015/11/14", 7, "SY"],
    ["2015/11/15", 2, "SY"],
    ["2015/11/16", 17, "SY"],
    ["2015/11/17", 33, "SY"],
    ["2015/11/18", 40, "SY"],
    ["2015/11/19", 32, "SY"],
    ["2015/11/20", 26, "SY"],
    ["2015/11/21", 35, "SY"],
    ["2015/11/22", 4, "SY"],
    ["2015/11/23", 32, "SY"],
    ["2015/11/24", 26, "SY"],
    ["2015/11/25", 22, "SY"],
    ["2015/11/08", 10, "DD"],
    ["2015/11/09", 15, "DD"],
    ["2015/11/10", 35, "DD"],
    ["2015/11/11", 38, "DD"],
    ["2015/11/12", 22, "DD"],
    ["2015/11/13", 16, "DD"],
    ["2015/11/14", 7, "DD"],
    ["2015/11/15", 2, "DD"],
    ["2015/11/16", 17, "DD"],
    ["2015/11/17", 33, "DD"],
    ["2015/11/18", 4, "DD"],
    ["2015/11/19", 32, "DD"],
    ["2015/11/20", 26, "DD"],
]

@C.funcs
def themeriver_example() -> ThemeRiver:
    c = (
        ThemeRiver()
        .add(
            ["DQ", "TY", "SS", "QG", "SY", "DD"],
            themeriver_data,
            singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="ThemeRiver-基本示例"))
    )
    return c


@C.funcs
def themeriver_graphic_component() -> ThemeRiver:
    c = (
        ThemeRiver()
        .add(
            ["DQ", "TY", "SS", "QG", "SY", "DD"],
            themeriver_data,
            singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="ThemeRiver-Graphic"),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=110,
                        bottom=110,
                        z=100,
                    ),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_shape_opts=opts.GraphicShapeOpts(
                                width=400, height=50
                            ),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="rgba(0,0,0,0.3)"
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text="pyecharts bar chart",
                                font="bold 26px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="#fff"
                                ),
                            ),
                        ),
                    ],
                )
            ],
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
