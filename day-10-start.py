#Functions with Outputs

def format_name(f_name, l_name):
    # docstrings to define functions
    '''Take a first and last name and format it to return the title case version of the  name.'''
    return f"{f_name.title()} {l_name.title()}"

print(format_name("liz", "skert"))