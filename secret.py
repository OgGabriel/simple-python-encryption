# make sure you already read how to use this encryption/hiding tool before using it
import requests;import base64

class hide_and_compile():
    def __init__(self, url):
        if not "raw" in url:
            print("Error: The url MUST be the raw version of a hastebin/pastebin/...")
            exit(-1)
        self.code = requests.get(url).text
        self.execute(self.code)
    def hide(self, code):
        return base64.b64encode(code.encode())
    def show(self, code):
        return base64.b64decode(code).decode()
    def execute(self, code):
        print("Encoding...\n")
        hidden = self.hide(self.code)
        print("Your code encoded looks like this: \n"+str(hidden))
        print("\nExecuting it...")
        print("Output: \n")
        eval(compile(self.show(hidden),'<string>','exec'))

class __hide__():
    def __init__(self, url):
        if not "raw" in url:
            print("Error: The url MUST be the raw version of a hastebin/pastebin/...")
            exit(-1)
        self.code = requests.get(url).text
        print(str(self.hide(self.code)))
    def hide(self, code):
        return base64.b64encode(code.encode())

class __compile__():
    def __init__(self, url):
        if not "raw" in url:
            print("Error: The url MUST be the raw version of a hastebin/pastebin/...")
            exit(-1)
        self.code = requests.get(url).text
        self.execute(self.code)
    def hide(self, code):
        return base64.b64encode(code.encode())
    def show(self, code):
        return base64.b64decode(code).decode()
    def execute(self, code):
        hidden = self.hide(self.code)
        eval(compile(self.show(hidden),'<string>','exec'))

