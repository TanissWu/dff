# coding=utf-8
# flake8: noqa

from pyecharts._version import __version__, __author__

# Simple Charts
from pyecharts.charts.bar import Bar
from pyecharts.charts.bar3D import Bar3D
from pyecharts.charts.boxplot import Boxplot
from pyecharts.charts.effectscatter import EffectScatter
from pyecharts.charts.funnel import Funnel
from pyecharts.charts.gauge import Gauge
from pyecharts.charts.geo import Geo
from pyecharts.charts.geolines import GeoLines
from pyecharts.charts.graph import Graph
from pyecharts.charts.heatmap import HeatMap
from pyecharts.charts.kline import Kline
from pyecharts.charts.line import Line
from pyecharts.charts.line3D import Line3D
from pyecharts.charts.liquid import Liquid
from pyecharts.charts.map import Map
from pyecharts.charts.parallel import Parallel
from pyecharts.charts.pie import Pie
from pyecharts.charts.polar import Polar
from pyecharts.charts.radar import Radar
from pyecharts.charts.sankey import Sankey
from pyecharts.charts.scatter import Scatter
from pyecharts.charts.scatter3D import Scatter3D
from pyecharts.charts.surface3D import Surface3D
from pyecharts.charts.themeriver import ThemeRiver
from pyecharts.charts.tree import Tree
from pyecharts.charts.treemap import TreeMap
from pyecharts.charts.wordcloud import WordCloud

# Composite Charts

from pyecharts.charts.composite.grid import Grid
from pyecharts.charts.composite.overlap import Overlap
from pyecharts.charts.composite.timeline import Timeline

# custom component

from pyecharts.contrib.page import Page

# misc
from pyecharts.app import online
from pyecharts.app import enable_nteract
from pyecharts.app import configure
from pyecharts.app import jupyter_image
from pyecharts.utils import NULL

# Deprecated Feature
from pyecharts.echarts.style import Style

# alias
Candlestick = Kline
