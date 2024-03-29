import re
import pynvim

@pynvim.plugin
class Sample2(object):

    def __init__(self, nvim):
        self.nvim = nvim

    def _echo(self, msg):
        self.nvim.command("echo '" + str(msg) + "'")

    @pynvim.command('Tanomu')
    def echo_message(self):
        current_bufnr = self.nvim.call("bufnr", "%")
        self._echo(current_bufnr)

    def get_headers(self):
        headers = {}
        for i in range(1, self.nvim.call("line", "$")):
            line = self.nvim.call("getline", i)
            match = re.match(r"^(#+)(.+)$", line)
            if match:
                headers[match.group(2)] = match.group(1)
        return headers

    @pynvim.command('ShowHeader')
    def show_headers(self):
        headers = self.get_headers()
        self.nvim.command("setlocal splitright")
        self.nvim.command("vnew")
        self.nvim.command("setlocal buftype=nofile bufhidden=hide nolist nonumber nomodifiable wrap")
        self.nvim.command('setlocal modifiable')
        for text, header in headers.items():
            self.nvim.current.buffer.append("{}, level{}".format(text, len(header)), 0)
