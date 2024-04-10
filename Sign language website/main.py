from flask import Flask, render_template, request

app = Flask(__name__)

letter_to_image = {
    'A': 'a.jpg',
    'B': 'b.jpg',
    'C': 'c.jpg',
    'D': 'd.jpg',
    'E': 'e.jpg',
    'F': 'f.jpg',
    'G': 'g.jpg',
    'H': 'h.jpg',
    'I': 'i.jpg',
    'J': 'j.jpg',
    'K': 'k.jpg',
    'L': 'l.jpg',
    'M': 'm.jpg',
    'N': 'n.jpg',
    'O': 'o.jpg',
    'P': 'p.jpg',
    'Q': 'q.jpg',
    'R': 'r.jpg',
    'S': 's.jpg',
    'T': 't.jpg',
    'U': 'u.jpg',
    'V': 'v.jpg',
    'W': 'w.jpg',
    'X': 'x.jpg',
    'Y': 'y.jpg',
    'Z': 'z.jpg',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_text = request.form['text'].upper()
    converted_images = []
    for letter in input_text:
        if letter in letter_to_image:
            converted_images.append(letter_to_image[letter])
    return render_template('convert.html', images=converted_images)

if __name__ == '__main__':
    app.run(debug=True)
