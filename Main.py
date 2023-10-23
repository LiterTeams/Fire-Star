from modules.app.App import App


def main():
    app = App()
    app.start()

    app.moviepy.auto_search()


if __name__ == "__main__":
    main()
