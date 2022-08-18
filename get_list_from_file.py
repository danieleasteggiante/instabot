
def get_list_from_file(file):
    lines = []
    with open(file) as f:
        lines = f.read().splitlines()
    
    return lines