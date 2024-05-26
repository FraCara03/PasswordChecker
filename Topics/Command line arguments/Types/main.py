args = sys.argv


if len(args) == 5:
    print(sum([int(x) for x in sys.argv[1:]]))
