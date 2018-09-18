
class Colors:
  HEADER = '\033[95m'
  BLACK = '\033[30m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


class Backgrounds:
  BLACK  = "\033[0;100m"   # Black
  RED    = "\033[0;101m"     # Red
  GREEN  = "\033[0;102m"   # Green
  YELLOW = "\033[0;103m"  # Yellow
  BLUE   = "\033[0;104m"    # Blue
  PURPLE = "\033[10;95m"  # Purple
  CYAN   = "\033[0;106m"    # Cyan
  WHITE  = "\033[0;107m"   # White


def print_header(text):
  print(
    Backgrounds.WHITE,
    Colors.BLACK,
    text,
    Colors.ENDC
  )


def print_selected(text):
  print(
    Backgrounds.YELLOW,
    Colors.OKBLUE,
    text,
    Colors.ENDC
  )


def print_regular(text):
  print(
    ' ',
    text
  )
