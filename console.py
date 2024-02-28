import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True
    
    def do_help(self, arg):
        return super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()