from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    link = request.form.get('link')
    if link:
        # Implement your download logic here
        # For example, you can use the 'requests' library:
        response = requests.get(link)
        with open('downloaded_file.mp4', 'wb') as file:
            file.write(response.content)
        return redirect(url_for('home'))
    else:
        return "Invalid link provided."

if __name__ == '__main__':
    app.run(debug=True)
