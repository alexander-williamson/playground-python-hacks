import tarfile;
import sys;
import os;
import importlib;
from os import listdir

uploaded_file_path = 'hello-world-py.tar.gz'
extract_path = './output-hello-world-py'
with tarfile.open(uploaded_file_path, 'r:gz') as tar:
     tar.extractall(path=extract_path)
sys.path.append(extract_path);

file_path = "output-hello-world-py/hello-world-py-1.0/hello/Hello.py"

temp_module = {}

with open(file_path, "r") as file: 
    exec(file.read(), temp_module)

# print(mf.keys());
print(temp_module['Hello']());

