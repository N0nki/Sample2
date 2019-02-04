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
