import graph
from flask import Flask
app = Flask(__name__)

final_histo = None
grapher = None

@app.route('/')
def hello_world():
    start_word = graph.sentence.first_word(final_histo)
    return (" ".join(grapher.gen_sentence(start_word, 20)))


def gen_graph():
    filename = "corpus.txt"
    token_list = graph.tokenization.tokenize(filename)

    my_graph = graph.Markov_Chain()
    for i, k in enumerate(token_list):
        if my_graph.get(k) is None:
            my_graph.set(k, True)
        else:
            my_graph.get(k).occured = True
            my_graph.get(k).node_val += 1
        if i < len(token_list) - 1:
            my_graph.update(k, token_list[i+1])

    return my_graph

def gen_histo(a_graph):
    histo = graph.sample.stochastic(a_graph)
    return histo

if __name__ == '__main__':
    grapher = gen_graph()
    final_histo = gen_histo(grapher)
    print("starting")
    app.run(debug=True)
