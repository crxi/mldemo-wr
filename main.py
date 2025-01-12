import writer as wf
import knn
from knn import draw_graph, graph_click
import wwt
from wwt import plot_line, reset, minus1, options_changed, click
import kcl
from kcl import draw_cluster

# Initialise the state
initial_state = wf.init_state({
    "my_app": {
        "title": "ML Demo"
    },
    "knn" : knn.initial_state,
    "wwt" : wwt.initial_state,
    "kcl" : kcl.initial_state,
})

knn.draw_graph(initial_state)
wwt.plot_line(initial_state)
kcl.draw_cluster(initial_state)