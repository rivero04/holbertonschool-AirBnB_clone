import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def quit(self):
        print("quit")



if __name__ == '__main__':
    HBNBCommand().cmdloop()