from flask import Flask, render_template

app = Flask(__name__)

posicao = {'x': 175, 'y': 175}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posicao')
def get_posicao():
    return posicao

@app.route('/move/<dx>/<dy>')
def mover(dx, dy):
    global posicao
    posicao['x'] += int(dx)
    posicao['y'] += int(dy)
    posicao['x'] = max(0, min(posicao['x'], 370))
    posicao['y'] = max(0, min(posicao['y'], 370))
    return posicao

if __name__ == "__main__":
    app.run(debug=True)