from flask import Flask, render_template
from controllers.products import products_blueprint
from controllers.suppliers import suppliers_blueprint

app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(suppliers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)