# repository searching
from pyscript import display, document

def name_finder(e):
    document.getElementById('result').innerHTML = ' '
    first_name = document.getElementById('firstname').value.capitalize().strip()
    last_name = document.getElementById('surname').value.capitalize().strip()


    fullname = first_name + " " + last_name
    members = ['Carlos Contemplacion', 'Dodong Torre', 'Enrique Manalo', 'Sylvia Yolanda']
    member_checker = fullname in members
    
    
    display_message = (f'Sorry, {fullname} does not exist in the list', f'{fullname} is in the list')

    display(display_message[member_checker], target='result')

