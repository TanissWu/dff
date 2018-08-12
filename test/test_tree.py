# coding=utf-8
from __future__ import unicode_literals

import os
import json
import codecs

from pyecharts import Tree


def test_tree_default():
    data = [
        {
            "children": [
                {"children": [], "name": "B"},
                {
                    "children": [
                        {
                            "children": [{"children": [], "name": "I"}],
                            "name": "E",
                        },
                        {"children": [], "name": "F"},
                    ],
                    "name": "C",
                },
                {
                    "children": [
                        {
                            "children": [
                                {"children": [], "name": "J"},
                                {"children": [], "name": "K"},
                            ],
                            "name": "G",
                        },
                        {"children": [], "name": "H"},
                    ],
                    "name": "D",
                },
            ],
            "name": "A",
        }
    ]
    copy_data = data.copy()
    data1 = Tree.collapse_interval(data)
    assert copy_data == data1


def test_tree_collapse_interval():
    with codecs.open(
        os.path.join("fixtures", "flare.json"), "r", encoding="utf-8"
    ) as f:
        j = json.load(f)
    copy_data = j.copy()
    data = Tree.collapse_interval([j], interval=2)
    assert data != copy_data
