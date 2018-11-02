from flask import Flask, render_template, request
app = Flask(__name__)

# To Do List:
# Link calcEval to user requests.
# Memory
# Clear Data
# More advanced math function (natural log, pi, euler's number)

def calcEval(equation):

  characters = list(equation)

  allowedInputs = ['0','1','2','3','4','5','6','7','8','9',
  '+','-','*','/','^', ' ', '(', ')']

  checkSet = set(characters + allowedInputs)

  if len(checkSet) != len(allowedInputs):
    return "Error"

  else:
    try:
      return (eval(equation))
    except Exception as e:
      return 'Error: {}'.format(e)    

# askedEquation = input()

# print(calcEval(askedEquation))    

@app.route('/')
def frontPage():
    
    # Need to use request for I/O
    # calc = request.args.get('calc')
    
    return render_template('index.html')
