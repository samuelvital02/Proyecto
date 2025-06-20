from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal: inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para medidas formativas académicas
@app.route('/academico')
def academico():
    return render_template('academico.html')

# Ruta para protocolo disciplinario
@app.route('/disciplinario')
def disciplinario():
    return render_template('disciplinario.html')

# Ruta para descarga de formatos
@app.route('/formatos')
def formatos():
    return render_template('formatos.html')

if __name__ == '__main__':
    app.run(debug=True)
