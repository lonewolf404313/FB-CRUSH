import uir


def main():
    try:
        uir.main()
    except KeyboardInterrupt:
        print(ui.RESET + "\n[ MARUF ] ATTACK STOPPED" + uir.RESET)


if __name__ == "__main__":
    main()
