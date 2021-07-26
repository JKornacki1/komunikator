class User:
    def __init__(self, nickname, password, controller):
        self.nickname = nickname
        self.password = password
        self.message = []
        self.controller = controller

    def send_message(self, nickname_to, text):
        pass

    def print_messages(self):
        for message in self.message:
            print(f'*    , {message.from_user} - {message.timestamp}')
            print(message.text)
            print()



