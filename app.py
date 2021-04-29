from flask import Flask, render_template
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secured'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

@app.route('/')
def home():
    return render_template('base.html', num=10)

@app.route('/admin/delete')
def news():
    return render_template('/admin/add-post.html')

if __name__ == '__main__':
    app.run(debug=True)