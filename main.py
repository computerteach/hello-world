def on_forever():
    basic.show_string("Hello! World  ")
    basic.show_icon(IconNames.GHOST)
    basic.clear_screen()
    basic.pause(500)
basic.forever(on_forever)
