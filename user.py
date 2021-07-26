class User:
    def __init__(self, nickname, password, controller):
        self.nickname = nickname
        self.password = password
        self.messages = []
        self.controller = controller

    def send_message(self, nickname_to, text):
        self.controller.send_message(self.nickname, nickname_to, text)

    def print_messages(self):
        for message in self.messages:
            print(f'*    , {message.from_user} - {message.timestamp}')
            print(message.text)
            print()



