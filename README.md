# playground-python-hacks
Python Snowflake Hacks

It is possible to upload your own files outside of python, extract them in a function and make them available.

Snowflake say they use `zipimport` for their imports https://docs.snowflake.com/en/developer-guide/udf/python/udf-python-limitations

Steps to reproduce:
1) Download the Python package you want to run manually and upload it into your Snowflake Notebook file system using the web editor
2) Extract the .tar.gz file and find the entry point
3) Use Python's `exec()` functionality to call the repo. I expect that `importlib` has similar issues.

Given a downloaded Python package called `hello-world-py` which has the following structure:

```
/hello
  __init__.py
  __main__.py
  Hello.py
```

```python
import tarfile;
import sys;
import os;
import importlib;
from os import listdir

uploaded_file_path = 'hello-world-py-1.0.tar.gz'
extract_path = 'tmp/appRoot/hello-world-py-1.0'

with tarfile.open(uploaded_file_path, 'r:gz') as tar:
     tar.extractall(path=extract_path)

sys.path.append(extract_path);

listdir('tmp/appRoot/hello-world-py-1.0/hello-world-py-1.0/hello')
file_path = "tmp/appRoot/hello-world-py-1.0/hello-world-py-1.0/hello/Hello.py"

mf = {}

with open(file_path, "r") as file: 
    exec(file.read(), mf)

# print(mf.keys());
print(mf['Hello']());
```

When executed in a Notebook, it return:

```
<Hello object at 0xffff7fc471c0>
```
