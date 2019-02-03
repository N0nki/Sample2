import pynvim

@pynvim.Plugin
class Sample2(object):

    def __init__(self, nvim):
        self.nvim = nvim

    def _echo(self, msg):
        self.nvim.command("echo '" + msg + "'")

    @pynvim.command('Tanomu')
    def echo_message(self):
        self._echo('naiteru')
