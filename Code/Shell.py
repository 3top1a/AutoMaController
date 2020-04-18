from cmd import Cmd

class Prompt(Cmd):

    def do_hello(self, args):
        pass

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit

