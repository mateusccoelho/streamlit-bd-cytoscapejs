import os
import streamlit as st
import streamlit.components.v1 as components

_RELEASE = True

if(not _RELEASE):
    _st_bd_cytoscape = components.declare_component(
        "streamlit_bd_cytoscapejs",
        url="http://localhost:3001"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_bd_cytoscape = components.declare_component(
        "streamlit_bd_cytoscapejs",
        path=build_dir
    )


def st_bd_cytoscape(elements={}, stylesheet={}, layout={}, key=None):
    """Create a new instance of Bidirectional Cytoscape.

    Parameters
    ----------
    elements: dict
        A dictionary specifing the nodes and edges that will be draw in the
        graph. It follows the Cytoscape.js standard.
    stylesheet: dict
        Dictionary specifing the style of the elements in the graph. Although
        this parameter is named style, the dictionary follows the Cytoscape.js
        standard of the style parameter.
    layout: dict
        A dictionary with the layout options. If not specified, it defaults to
        a grid.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    object
        The id of the element (node or edge) tapped.

    """

    component_value = _st_bd_cytoscape(
        elements = elements,
        stylesheet = stylesheet,
        layout = layout,
        key = key,
        default=0
    )
    return component_value


# Development test code
if(not _RELEASE):
    st.subheader("Component with variable args")
    check = st.checkbox('Check graph')
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
    node_id = st_bd_cytoscape(elements, key='foo')
    st.write(node_id)
    node_id = st_bd_cytoscape(elements, key='doo')
    st.write(node_id)
