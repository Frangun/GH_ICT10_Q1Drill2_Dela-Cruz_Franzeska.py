# Collecting and Displaying data
from pyscript import display, document

def collecting_data(e):
    document.getElementById("div2").innerHTML=""

    name = document.getElementById("name").value

    age = document.getElementById("age").value

    school = document.getElementById("school").value

    message = f"""👤Student Profile:
        
        \tName   : "{name}\"
        
        \tAge    : {age}
        
        \tSchool : "{school}\" 

        ✏️ Notes:
        At {age}, {name} currently studies at {school}.
        This information was gathered through input fields and displayed using
        a multiline string in Python via PyScript.
        """

    display(message, target="div2")

# DATA & NOTES FROM EX5

# def collecting_data(e):
#     document.getElementById("div1").innerHTML=''

#     first_name = document.getElementById("Franzeska").value
#     last_name = document.getElementById("DC").value
#     section = document.getElementById("dropdown").value

#     display(f"My name is {first_name} {last_name} from {section}", target="div1")

# # outside collecting_data(e)

# multiline_strings = '''
#     Good Day! kdwjdqw
#     ijweijijefjwjefjwefj;
#     jfowejfijwijfdn
#         ewoijfiiwjefw
#             jpjpw
# '''

# sample_string = 'Dela Cruz\'s Book' # backlash is needed to avoid errors

# directory = 'C:\\Desktop\\Ict2526' # need two backslashes in a directory variable

# laugh = 'ha'

# longest = 'pneumonoultramicroscopicsilicovolcanoconiosis'

# print(multiline_strings) # only shows in inspect>console

# display(sample_string)

# display(directory)

# display(laugh * 5) # ha x 5 = hahahahaha

# display(longest[-7]) #if 10: displays the 11th letter or the letter after the 10th letter. If you replace it with a number that exceeds the amount of letters = error (cant do 45 cus the word is only 45 letters). If -7: display 'o' in the word since it counts backwards (45-7=38th letter)
# display(len(longest)) #display amount of letters.

# # functioning = parenthesis
# # indexing = brackets

# #STRIPPING SPACES

# sample_string2 = '     DC     '

# #print = console
# #display = webpage itself

# print(sample_string2.strip()) # method name - no spaces in console

# # print (sample_string2) # has spaces in console

# # print(sample_string2.lstrip()) # lstrip removes spaces on the left in console
# display(sample_string2)

# #SPLIT METHOD

# sample_string3 = 'blue'
# display(sample_string3.split()) # it convers it to a list 
# print(sample_string3.split())

# #REPLACE METHOD

# sample_string4 = 'I like Python'
# display(sample_string4.replace('Python', 'Javascript')) #replaces python with javascript

# # - casing

# sample_string5 = 'What you are looking for is in the Library'

# display(sample_string5.capitalize()) # capitalizes first letter of first word 
# display(sample_string5.title()) # capitalizes first letter of every word
# display(sample_string5.lower()) # lowercase on every word
# display(sample_string5.upper()) # uppercase on every word
# display(sample_string5.swapcase()) # swapcases 

