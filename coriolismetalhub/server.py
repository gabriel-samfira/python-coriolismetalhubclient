from cliff.lister import Lister
from cliff.show import ShowOne

from coriolismetalhub import client


class Servers(Lister):

    def get_parser(self, prog_name):
        parser = super(Servers, self).get_parser(prog_name)
        return parser

    def take_action(self, args):
        cli = client.get_client_from_options(
            self._cmd_options)
        servers = cli.list_servers()
        ret = [
            ["ID", "Hostname", "API Endpoint", "Alive"]
        ]

        items = []
        for server in servers:
            item = [
                server["id"],
                server["hostname"],
                server["api_endpoint"],
                server["active"],
            ]
            items.append(item)

        ret.append(items)
        return ret


class ShowServer(ShowOne):

    def get_parser(self, prog_name):
        parser = super(ShowServer, self).get_parser(prog_name)
        parser.add_argument("id", help="The ID of the server")
        return parser
    
    def take_action(self, args):
        cli = client.get_client_from_options(
            self._cmd_options)
        server = cli.get_server(args.id)
        columns = ('ID',
                   'Hostname',
                   "API Endpoint",
                   "Physical Cores",
                   "Memory",
                   "Alive")
        data = (server["id"],
                server["hostname"],
                server["api_endpoint"],
                server["physical_cores"],
                server["memory"],
                server["active"])
        return (columns, data)


class CreateServer(ShowOne):

    def get_parser(self, prog_name):
        parser = super(CreateServer, self).get_parser(prog_name)
        parser.add_argument("endpoint", help="The endpoint of the server.")
        return parser
    
    def take_action(self, args):
        cli = client.get_client_from_options(
            self._cmd_options)
        server = cli.add_server(args.endpoint)
        columns = ('ID',
                   'Hostname',
                   "API Endpoint",
                   "Physical Cores",
                   "Memory",
                   "Alive")
        data = (server["id"],
                server["hostname"],
                server["api_endpoint"],
                server["physical_cores"],
                server["memory"],
                server["active"])
        return (columns, data)
