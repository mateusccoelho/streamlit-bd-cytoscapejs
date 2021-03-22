import { Streamlit, RenderData } from "streamlit-component-lib"
import Cytoscape from "cytoscape"
import deepEqual from "deep-equal"

// Creates a graph instance
const cy_div = document.body.appendChild(document.createElement("div"))
var cy = Cytoscape({
  container: cy_div
});

// Returns the tapped node's id to python
cy.on('tap', function(evt){
  var target = evt.target;
  if(target !== cy) {
    Streamlit.setComponentValue(target.id())
  }
});

var past_elements = {}

function onRender(event: Event): void {
  // Unpacking input from python
  const data = (event as CustomEvent<RenderData>).detail
  let elements = data.args["elements"]
  let stylesheet = data.args["stylesheet"]
  let layout = data.args["layout"]

  console.log(elements)

  // Draw the graph if it's empty or if it changed its elements
  if(cy.nodes().size() === 0 || !deepEqual(past_elements, elements)){
    // Fix the height of the graph
    cy_div.setAttribute("style", "height:400px;")

    cy.elements().remove()
    cy.add(elements)
    past_elements = elements
    cy.style(stylesheet)

    // Set default options if the layout is not specified
    let height = cy_div.offsetHeight
    let width = cy_div.offsetWidth
    let bounding_box = {x1: 0, y1: 0, x2: width, y2: height, w: width, h: height}
    if(Object.keys(layout).length === 0){
      layout = {
        name: "grid",
        boundingBox: bounding_box
      }
    } else {
      layout['boundingBox'] = bounding_box
    }

    cy.layout(layout).run()
  }

  Streamlit.setFrameHeight()
}

// Activating internal Streamlit functions
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()
