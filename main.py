from controller import Controller

if __name__ == "__main__":
    controller = Controller()
    tomek = controller.add_user('Tomek', '12345')
    karolina = controller.add_user('Karolina', "56789")
    tomek.send_message('Karolina', 'Hej co tam słychać')
    karolina.print_messages()

