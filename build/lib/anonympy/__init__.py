'''
Package for data anonymization of different data types 
such as tabular, text, images and sound. 
'''

__version__ =  "0.1.0"

# Check if all dependencies have been installed

hard_dependencies = ("faker", "cape_privacy", "pandas", "numpy")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f"{dependency}: {e}")

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies


from anonympy import tabular
from anonympy import images
from anonympy import sound 
from anonympy import text
from anonympy.tabular.core import dfAnonymizer

__all__ = ["tabular", "tabular", "sound", "text", "dfAnonymizer"]
