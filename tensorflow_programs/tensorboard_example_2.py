# Visualize a giant graph
import tensorflow as tf
from tensorflow.python.ops import summary_ops_v2

a = tf.Variable(2.0, name='a')
b = tf.Variable(3.0, name='b')
c = tf.Variable(7.0, name='c')

@tf.function
def graph_to_visualize(a, b, c):
    d = tf.multiply(a, b, name='d-mul')
    e = tf.add(b, c, name='e-add')
    f = tf.subtract(e, a, name='f-sub')
    g = tf.multiply(d, b, name='g-mul')
    h = tf.divide(g, d, name='h-div')
    i = tf.add(h, f, name='i-add')

writer = tf.summary.create_file_writer('./graphs')

with writer.as_default():
    # get graph from function
    graph = graph_to_visualize.get_concrete_function(a, b, c).graph
    # visualize
    summary_ops_v2.graph(graph.as_graph_def())

writer.close()