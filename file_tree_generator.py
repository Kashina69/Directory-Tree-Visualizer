import os

def generate_tree(directory, depth=0, max_depth=5):
    prefix = ""
    if depth > max_depth:
        return
    if depth != 0:
        prefix = '│   '*depth 
    
    if os.path.basename(directory) == "node_modules" or os.path.basename(directory) == ".next":
        return
    else:
        dirname = os.path.basename(os.getcwd())+"_structure.txt"
        f = open(dirname,"a",encoding='utf-8')
        lines = str(prefix + '├── ' + os.path.basename(directory) + "/"+'\n')
        f.write(lines)
        f.close()
    
    try:
        entries = os.listdir(directory)
    except OSError:
        return
    
    subdirectories = [entry for entry in entries if os.path.isdir(os.path.join(directory, entry))]
    #subdirectories = [entry for entry in entries]
    
    for subdirectory in subdirectories:
        generate_tree(os.path.join(directory, subdirectory), depth + 1, max_depth)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dirname = os.path.basename(os.getcwd())+"_structure.txt"
    f = open(dirname,"w",encoding='utf-8')
    f.write("")
    f.close()
    generate_tree(current_dir)
