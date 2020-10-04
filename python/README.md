# Python task

Histogram generator using Pandas.

## Installation
1. ``cd`` in ``./python`` directory.
2. Create and activate virtual enviroment with ``venv`` package.
```
$ python -m venv venv_env
 	
$ source venv_env/bin/activate
```
More info about ``venv`` https://docs.python.org/3/library/venv.html#creating-virtual-environments

3. Install dependencies via ``requirements.txt``.
```
$ pip install -r requirements.txt
```

## Usage
```
$ python main.py
```

Script will look for ``pr.json`` file in the same directory as script itself. Histogram will be saved as ``.png`` file. For changing histogram resolution you can change ``dpi`` parametre in:

```
figure.savefig('histogram.png', dpi=300)
```