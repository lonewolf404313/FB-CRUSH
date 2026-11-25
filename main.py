import ui


def main():
    try:
        ui.main()
    except KeyboardInterrupt:
        print(ui.RESET + "\n[ MARUF ] ATTACK STOPPED" + ui.RESET)


if __name__ == "__main__":
    main()
