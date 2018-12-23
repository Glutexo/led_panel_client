from graphics import init, draw_progress, flash
from images import cycle
from wlan import connect


def main():
    display = init()

    draw_progress(display, connect())
    flash(display)

    cycle(display)


if __name__ == "__main__":
    main()
