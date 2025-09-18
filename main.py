# working with integers
from pyscript import display, document

# functions & variables
def printing_data(e): # 'e' is null
    document.getElementById('div2').innerHTML = "" # so that when you click submit multiple times, output will only appear once.
    num1 = float(document.getElementById('num1').value)
    num2 = float(document.getElementById('num2').value)
    height = float(document.getElementById('height').value)

    display(f'The area is {((num1 + num2)/ 2) * height}', target='div2')
    # display(f'The area of a trapezoid is {1/2 * height * number 1 + number2}', target='div2')

    # display(f'The area of a trapezoid is : {1/2 * number 1 + number 2 * height}', target='div2')








