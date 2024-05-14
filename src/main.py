import os
import json
from graphviz import Digraph

def list_folders(path):
    folders = []
    for dirpath, dirnames, filenames in os.walk(path):
        for directory in dirnames:
            folders.append(os.path.join(dirpath, directory))
    return folders

def create_dot_edges(dot, paths, existing_edges):
    if len(paths) >= 2:
        for i in range(len(paths) - 1):
            edge = (paths[i], paths[i + 1])
            if edge not in existing_edges:
                dot.edge(paths[i], paths[i + 1])
                existing_edges.add(edge)

def main():
    dot = Digraph(comment='Skills Roadmap')
    path = 'roadmap_content'
    existing_edges = set()

    for dirpath, dirnames, filenames in os.walk(path):
        for directory in dirnames:
            # create nodes for dir
            dot.node(directory, directory)

            # search for json file
            folder_path = os.path.join(dirpath, directory)
            for file in os.listdir(folder_path):
                if file.endswith('.json'):
                    file_path = os.path.join(folder_path, file)
                    with open(file_path) as f:
                        nodes_skills_data = json.load(f)
                    # create edges for json file
                    for skill_node in nodes_skills_data:
                        create_dot_edges(dot, [directory, skill_node['name']], existing_edges)

        # create edges for folder
        nodes_list = dirpath.split("/")
        nodes_list.pop(0)
        create_dot_edges(dot, nodes_list, existing_edges)

    dot.render('roadmap_render/course_roadmap', format='png', cleanup=True)

if __name__ == '__main__':
    main()
