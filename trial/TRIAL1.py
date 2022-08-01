from typing import List


class Data:

    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip

class Server:
    COUNT = 0

    def __init__(self) -> None:
        self.ip = Server.COUNT + 1
        self.buffer = []
        self.router = None
        Server.COUNT += 1

    def get_ip(self) -> int:
        return self.ip

    def get_data(self) -> List:
        packets = self.buffer
        self.buffer = []
        return packets

    def send_data(self, data: Data) -> None:
        self.router.buffer.append(data)


class Router:


    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server: Server) -> None:
        server.router = self
        self.servers[server.ip] = server

    @staticmethod
    def unlink(server: Server) -> None:
        server.router = None

    def send_data(self):
        for packet in self.buffer:
            self.servers[packet.ip].buffer.append(packet)
            del packet


router = Router()
sv_from = Server()
router.link(sv_from)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
print(msg_lst_from)
msg_lst_to = sv_to.get_data()
print(msg_lst_to)





