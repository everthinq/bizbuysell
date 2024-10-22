from scrapy.cmdline import execute


def main():
    # execute(['scrapy', 'crawl', 'bizbuysell', '--nolog'])
    execute(['scrapy', 'crawl', 'bizbuysell'])


if __name__ == '__main__':
    main()
