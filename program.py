import service


def main():
    print("Welcome to the Talk Python info downloader.")
    print()

    service.download_info()

    for show_id in range(100, 130):
        info = service.get_episode(show_id)
        print("{} {}".format(info.title, info.link))


if __name__ == '__main__':
    main()
