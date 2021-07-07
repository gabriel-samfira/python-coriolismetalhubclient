import sys
import os

from cliff.app import App
from cliff.commandmanager import CommandManager

from coriolismetalhub import client


class CoriolisMetalApp(App):

    def __init__(self):
        super(CoriolisMetalApp, self).__init__(
            description='Coriolis metal CLI',
            version='0.1',
            command_manager=CommandManager('coriolismetalhub.cli'),
            deferred_help=True)

    def _env(self, var_name, default=None):
        return os.environ.get(var_name, default)

    def build_option_parser(self, description, version, argparse_kwargs=None):
        parser = super(CoriolisMetalApp, self).build_option_parser(
            description, version, argparse_kwargs)
        
        parser.add_argument(
            '--endpoint', '-e',
            default=self._env("CORIOLIS_METAL_ENDPOINT"),
            help='Coriolis Metal hub endpoint.')
        parser.add_argument(
            '--ca-cert',
            default=self._env("CORIOLIS_METAL_CA_CERT"),
            help='CA certificate.')
        parser.add_argument(
            '--client-cert', '-c',
            default=self._env("CORIOLIS_METAL_CLIENT_CERT"),
            help='Client certificate.')
        parser.add_argument(
            '--client-key', '-k',
            default=self._env("CORIOLIS_METAL_CLIENT_KEY"),
            help='Client certificate private key.')
        return parser

    def prepare_to_run_command(self, cmd):
        cmd._cmd_options = self.options


def main(argv=sys.argv[1:]):
    myapp = CoriolisMetalApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))