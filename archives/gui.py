import eel
from query_data import query_rag;

eel.init('Page')

@eel.expose
def queryLLM(question):
    return query_rag(question)

eel.start('index.html', size = (300,450), host='localhost', port='80')


