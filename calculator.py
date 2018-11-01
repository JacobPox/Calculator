from flask import Flask, render_template, request
app = Flask(__name__)

# To Do List:
# Take input and produce output
# Arithmetic
# Memory
# Clear Data

@app.route('/')
def frontPage():
    
    # Need to use request for I/O
    # calc = request.args.get('calc')
    
    return render_template('index.html')
