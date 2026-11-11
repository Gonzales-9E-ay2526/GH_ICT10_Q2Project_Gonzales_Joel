# 2nd Quarter project
from pyscript import document

def candidate_checker(e):
    club_members = ['Chester Roxas', 'Joel Gonzales', 'Joseph Co', 'Ezekiel Bacay', 'Franco Maglaqui', 'Joald Calpo', 'Joshua Ortiz'] # List of Club members
    
    first_name = document.getElementById('first_name').value.strip().title() 
    last_name = document.getElementById('last_name').value.strip().title()
    
    applicant = first_name + ' ' + last_name
    member_checker = applicant in club_members

    messages = (f'Sorry {applicant}, your name is not on the list', f'Congratulations {applicant}! You are now part of the gaming club') # Returns message

    document.getElementById('result').innerHTML = messages[member_checker]


from pyscript import document, display

    # List of non-metal elements with (Name, Atomic Number, Mass)
non_metals = {
        "Ar": ("Argon", 18, 39.90),
        "Br": ("Bromine", 35, 79.904),
        "C": ("Carbon", 6, 12.011),
        "Cl": ("Chlorine", 17, 35.45),
        "F": ("Fluorine", 9, 18.998),
        "H": ("Hydrogen", 1, 1.008),
        "He": ("Helium", 2, 4.0026),
        "I": ("Iodine", 53, 126.904),
        "Kr": ("Krypton", 36, 83.798),
        "N": ("Nitrogen", 7, 14.007),
        "Ne": ("Neon", 10, 20.180),
        "O": ("Oxygen", 8, 15.999),
        "P": ("Phosphorus", 15, 30.974),
        "Rn": ("Radon", 86, 222),
        "S": ("Sulfur", 16, 32.07),
        "Se": ("Selenium", 34, 78.96),
        "Xe": ("Xenon", 54, 131.293),
    }


# Function to check the typed symbol
def element_checker(e):
        document.getElementById('output').innerHTML = ""
        element1 = document.getElementById('element_name').value.strip().title()

    # Search for the symbol in the dict, give error values if missing
        result = non_metals.get(
        element1,
    ("Element does not exist", "-", "-")
        )

    # Output the details directly to the HTML page
        document.getElementById('output').innerHTML = f"""
        <b>Symbol:</b> {element1}<br>
        <b>Element:</b> {result[0]}<br>
        <b>Atomic Number:</b> {result[1]}<br>
        <b>Atomic Mass:</b> {result[2]}
    """


def result_checker(e):
    document.getElementById('output').innerHTML = ""

    # Define sets for each grade level
    grade7 = {'Moka Sakai', 'Anthony Edwards', 'Hawas Kobra'}
    grade8 = {'Joshua Ortiz', 'Taranbir Singh', 'Bonnie Nubla', 'Alexa Agnote'}
    grade9 = {'Lebron James', 'Alejandro Alanano', 'Joald Gonzales'}
    grade10 = {'Georgina Sarmiento', 'Franco Maglaqui', 'Chester Roxas', 'Joseph Co'}

    # User input value for first and last name
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value

    # Combine first and last name 
    new_member = f_name + " " + l_name

    new_member_set = {new_member}        

    # | combines all the grade levels including the new member of club
    set_members = grade7 | grade8 | grade9 | grade10 | new_member_set
    total_members = len(grade7 | grade8 | grade9 | grade10 | new_member_set)

    # Joins them all together with a line break
    members_list = "<br>".join(set_members)

    # Display output
    document.getElementById('result').innerHTML = f'All members:<br> {members_list}'
    display(f'Total members: {total_members}', target='result') 