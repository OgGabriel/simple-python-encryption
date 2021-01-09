# Simple Python Encryption/Hiding tool
A simple script that hides and encodes a little bit your python code (not that strong)

## How to use
- Firstly you should have Python 3.x
- Then you should download ``secret.py`` and add it to the directory of your script
- Call its functions by importing the file.
- You should encode it then paste it in a hastebin/pastebin/... and pass the raw url version

## Functions
- secret._compile(url)

Compiles your encoded code, which is in a raw pastebin
```python
import secret
"""
url content:

print("hello world")
"""
secret._compile("https://hastebin.com/raw/vayosuqumi.py")
# output: hello world
```

- secret._hide(url)

Encodes your code which is in a raw pastebin
```python
import secret
secret._hide("https://hastebin.com/raw/vayosuqumi.py")
# output: b'cHJpbnQoImhlbGxvIHdvcmxkIik='
```

- secret.hide_and_compile(url)

Do both functions at once with detailed commentaries
```python
import secret
secret.hide_and_compile("https://hastebin.com/raw/vayosuqumi.py")

# full output:

# starts here
"""
Encoding...

Your code encoded looks like this:
b'cHJpbnQoImhlbGxvIHdvcmxkIik='

Executing it...
Output:

hello world
"""
# ends here
```

## Errors
- Whenever you don't use a raw pastebin, it exits with code -1
```python
import secret
secret.hide_and_compile("https://hastebin.com/vayosuqumi.py")
# output: Error: The url MUST be the raw version of a hastebin/pastebin/...
```