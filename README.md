# initial steps
`pip install -r requirements.txt`

In vscode, install 
* "Python Refactoring" by Yotam Alon
* "Pyrefact" by Olle Lindgren

# run once
``` bash
cd fibonacci
python3 *.test.py
```
# run continuously
``` bash
cd fibonacci
inotifywait -m -e close_write --format '%w%f' *.py | while read MODFILE;  do py *.test.py; don
```