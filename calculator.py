from flask import Flask, render_template, request
import re
app = Flask(__name__)

def calcEval(equation):
  '''

  calcEval() uses eval(), which is normally a dangerous thing to do.
  To combat this, a list of allowed inputs are made so eval() only gets called if the 
  "equation" given contains only allowed inputs.
  
  '''

  characters = list(equation)

  allowedInputs = ['0','1','2','3','4','5','6','7','8','9',
  '+','-','*','/','^', ' ', '(', ')','.']

  checkSet = set(characters + allowedInputs)

  if len(checkSet) != len(allowedInputs):
    return "Error: Unknown input character."

  else:
    try:
      equation = re.sub('(?<=\d|\))(\()', '*(', equation)
      equation = equation.replace('^','**')
      return (eval(equation))
    except:
      return 'Unknown error occured.'  


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
