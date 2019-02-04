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
        matched_list = []
        for i in range(1, self.nvim.call("line", "$")):
            line = self.nvim.call("getline", i)
            match = re.match(r"^(#+)(.+)$", line)
            matched_list.append(line)
            if match:
                headers[match.group(2)] = match.group(1)
        return matched_list

    @pynvim.command('ShowHeader')
    def show_headers(self):
        self.nvim.command("setlocal splitright")
        self.nvim.command("vnew")
        self.nvim.command("setlocal buftype=nofile bufhidden=hide nolist nonumber nomodifiable wrap")
        self.nvim.command('setlocal modifiable')
        matched_list = self.get_headers()
        for matched in matched_list:
            self.nvim.current.buffer.append(matched, 0)
        # headers = self.get_headers()
        # for text, header in headers:
        #     self.nvim.current.buffer.append("{}, level{}".format(text, len(header)), 0)
