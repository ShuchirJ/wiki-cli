# import subprocess

# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eu arcu congue, imperdiet tellus eget, vehicula odio. Praesent ipsum ex, placerat a tempor sed, venenatis quis nisi. Sed dignissim rutrum purus. Duis ac varius purus. Vivamus a est at velit tempus venenatis non non risus. Suspendisse ac elementum diam. Sed volutpat at dolor vel dictum. Sed eget congue neque, sollicitudin ultrices eros. Duis condimentum augue quis felis viverra, a sodales orci faucibus. Fusce aliquam nisi quam, sagittis vestibulum augue scelerisque vitae. Quisque a lacus massa. Etiam tempus mollis faucibus. Nullam rhoncus lacinia quam et blandit.

# Quisque condimentum massa sit amet diam porta, eu tempus ligula tempus. Etiam tristique velit a nibh tempus, a fermentum massa laoreet. Morbi vulputate quis lectus at ultricies. Integer non neque ut enim imperdiet commodo. Pellentesque feugiat libero in ex posuere tristique. Praesent finibus maximus sem, vitae congue sapien luctus et. Suspendisse quis vulputate odio, ut vehicula lacus. Morbi in turpis id ipsum accumsan imperdiet. Fusce quam nisl, hendrerit et varius ac, tristique vitae odio. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam vel placerat odio. Cras vehicula eu neque eget dictum. Nam consectetur posuere enim, sed ultricies ante mollis et.

# Donec auctor dictum velit. Sed ac tellus euismod, congue lacus ac, tincidunt ipsum. Praesent sit amet purus lorem. Sed varius purus at magna dignissim, imperdiet finibus nisi bibendum. Fusce tristique pharetra sapien id facilisis. Vestibulum aliquam, lacus et pulvinar viverra, diam nunc blandit ante, et dapibus massa dui quis odio. Aliquam malesuada ullamcorper scelerisque. Suspendisse malesuada diam metus, nec mattis tellus rhoncus in. Nam gravida ipsum eu dolor finibus maximus. Pellentesque quis luctus odio. Nam id tincidunt metus. Ut scelerisque metus neque, quis malesuada enim convallis vitae. Aliquam pharetra ex nec eleifend convallis. Aenean iaculis, tortor vitae varius luctus, erat sapien lobortis nisl, ullamcorper dictum metus risus vel sapien.

# Sed ac nibh laoreet, maximus nulla sit amet, consectetur ante. Aliquam luctus fermentum malesuada. Pellentesque suscipit metus in efficitur pharetra. Maecenas cursus enim nec ultrices ultrices. Nullam posuere felis ut volutpat fringilla. Aliquam tellus neque, suscipit in lectus ut, dictum tempor urna. Pellentesque pretium tempor ex eu ultricies. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus a quam eget velit fermentum posuere.

# Proin non gravida nulla. Cras sed sem eget est malesuada condimentum. Vestibulum elementum fermentum erat, ut malesuada ligula varius sed. In pulvinar leo a tellus vehicula tristique. Maecenas ac auctor justo, eget vulputate lorem. Etiam feugiat hendrerit ex sed porttitor. Nullam sed accumsan velit.

# Sed id massa vel lectus pretium tincidunt. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum finibus, nisl at pharetra imperdiet, ante dui congue turpis, at commodo sem sem sit amet tellus. Aenean sem justo, convallis ac ante rhoncus, sodales eleifend lorem. Ut posuere lobortis est eu convallis. In bibendum vel lorem ut sagittis. Nunc tristique ac ex nec venenatis. In mauris ante, elementum a est et, molestie vestibulum turpis. Praesent vel iaculis velit. Phasellus tincidunt pulvinar rutrum. Suspendisse potenti. Duis molestie lorem ipsum, quis fringilla ipsum scelerisque vel. Interdum et malesuada fames ac ante ipsum primis in faucibus.

# Nulla facilisi. Suspendisse posuere et sem ac semper. Quisque interdum aliquam felis, vitae pharetra leo convallis eu. Donec ac ligula vel risus maximus venenatis a non metus. Maecenas in volutpat dolor. Nam eget ornare turpis, ut placerat nisi. Praesent vitae est in lectus condimentum laoreet eget vitae diam. Nam sed turpis a ex commodo eleifend et vel lacus.

# Maecenas blandit lacinia elit in mollis. Sed dignissim aliquam ante, nec posuere sapien consequat id. In at tincidunt arcu, in aliquet ex. Integer efficitur dapibus ipsum vitae elementum. Phasellus iaculis ipsum et tortor pretium ultrices. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris ornare lorem at ex aliquam molestie.

# Nullam pharetra ut ante eget sodales. Aliquam eget neque dapibus nunc ornare pretium ut ut ante. In pharetra nec ante et dignissim. Praesent faucibus nisl nec magna malesuada ornare. Curabitur sed ipsum quis velit molestie efficitur eu ac lacus. Nam feugiat elit non nisl sodales fermentum. Nulla volutpat semper bibendum. Aliquam suscipit velit mollis, bibendum sem venenatis, porta ante. Etiam eu nisi nec arcu cursus tristique ac eu felis. Sed massa eros, vestibulum sit amet tellus ac, efficitur cursus libero. Cras blandit augue nibh, vitae auctor dolor mollis vitae. Nullam ultrices est quis maximus scelerisque. Curabitur sollicitudin diam non ex lobortis, non sagittis ex tincidunt. Vivamus maximus elementum orci sed convallis. Aliquam aliquam nec neque id sodales.

# Nullam elit felis, feugiat ut massa sed, fringilla maximus ante. Aenean eu lectus enim. Morbi lacinia sem sapien. Suspendisse pellentesque mi in augue hendrerit laoreet. Donec neque purus, tincidunt non enim eget, mollis elementum orci. Sed fermentum dui eu felis viverra fermentum. Aliquam id urna erat. Quisque volutpat turpis risus, in sollicitudin neque ultricies ac."""

# subprocess.run(['less'], input=text.encode(), check=True)


import curses

def main(stdscr):
    curses.curs_set(1)
    stdscr.clear()
    stdscr.refresh()

    height, width = stdscr.getmaxyx()

    stdscr.addstr(0, 0, "Welcome to wiki-cli! Press ESC to exit.")

    input_prompt = ">>> "
    user_input = ""

    while True:
        stdscr.move(height - 2, 0)
        stdscr.clrtoeol()
        stdscr.addstr(height - 2, 0, "Enter a search query: ")

        stdscr.move(height - 1, 0)
        stdscr.clrtoeol()
        stdscr.addstr(height - 1, 0, input_prompt + user_input)
        stdscr.refresh()

        key = stdscr.getch()

        if key == 27:
            break
        elif key in (10, 13):
            user_input = ""
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            user_input = user_input[:-1]
        elif 32 <= key <= 126:
            user_input += chr(key)

curses.wrapper(main)
