from flask import Flask, render_template

app = Flask(__name__)

# Sample data for blog posts
posts = [
    {
        'author': 'Sany Das',
        'title': 'First Blog Post',
        'content': 'This is the content of the first blog post.',
        'date_posted': 'September 1, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Blog Post',
        'content': 'This is the content of the second blog post.',
        'date_posted': 'September 2, 2024'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post=posts[post_id])

if __name__ == '__main__':
    app.run(debug=True)
