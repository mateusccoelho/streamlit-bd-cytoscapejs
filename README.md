# streamlit-bd-cytoscapejs

This package is a Streamlit bidrectional component that wraps the JavaScript 
library Cytoscape.js. It can draw networks (a.k.a. graphs) and its API is very similar 
to the JS package.

## Installation

`pip install -i https://test.pypi.org/simple/ streamlit-bd-cytoscapejs`

## Parameters

elements (dict):
    A dictionary specifing the nodes and edges that will be draw in the
    graph. It follows the Cytoscape.js standard.
    
stylesheet (dict):
    Dictionary specifing the style of the elements in the graph. Although
    this parameter is named style, the dictionary follows the Cytoscape.js
    standard of the style parameter.
    
layout (dict):
    A dictionary with the layout options. If not specified, it defaults to
    a grid.
    
key (str or None):
    An optional key that uniquely identifies this component. If this is
    None, and the component's arguments are changed, the component will
    be re-mounted in the Streamlit frontend and lose its current state.

## Returns

object:
    The id of the element (node or edge) tapped.
    
## Example

``` python
import streamlit as st
import numpy as np
import pandas as pd
import streamlit_bd_cytoscapejs

check = st.checkbox('Click here to choose a different graph')

if(check):
    elements = [
        {'data': {'id': 'a'}},
        {'data': {'id': 'b'}},
        {'data': {
            'id': 'ab',
            'source': 'a',
            'target': 'b'
        }}
    ]
    layout = {}
else:
    elements = [
        {'data': {'id': 'c'}},
        {'data': {'id': 'd'}},
        {'data': {
            'id': 'cd',
            'source': 'c',
            'target': 'd'
        }}
    ]
    layout = {'name': 'random'}

node_id = streamlit_bd_cytoscapejs.st_bd_cytoscape(
    elements,
    layout=layout,
    key='foo'
)
st.write(node_id)
```
