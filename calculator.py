from flask import Flask, render_template, request
app = Flask(__name__)

# To Do List:
# Memory
# Clear Data
# More advanced math function (natural log, pi, euler's number)

def calcEval(equation):

  characters = list(equation)

  allowedInputs = ['0','1','2','3','4','5','6','7','8','9',
  '+','-','*','/','^', ' ', '(', ')']

  checkSet = set(characters + allowedInputs)

  if len(checkSet) != len(allowedInputs):
    return "Error: Unknown input character."

  else:
    try:
      equation = equation.replace('^','**')
      return (eval(equation))
    except Exception as e:
      return 'Unknown error occured.'
      # return 'Error: {}'.format(e)    


@app.route('/', methods=['GET', 'POST'])
def frontPage():

  if request.method == 'GET':
    # Show the basic HTML page
    return render_template('index.html')
    
  elif request.method == 'POST':
    # Calculate request
    expression = request.form.get('calc')
    result = str(calcEval(expression))

    return render_template('index.html', result=result, expression=expression)
