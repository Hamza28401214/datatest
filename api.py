import flask
import logging
from etl.etl import *
logging.basicConfig(filename='logs/record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to test api'


@app.route('/read/first-chunk', methods=['GET'])
def read_ten():
    con = sqlite3.connect(pat + '\\database//final_data.db')
    res = pd.read_sql_query("SELECT * from tun_tab LIMIT 10", con)
    res.drop('index', axis=1, inplace=True)
    res = res.to_json(orient='records')
    con.close()
    return res

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
