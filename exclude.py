with open('filestobeexcluded.txt', 'r') as f:
    lines = [i.replace('\n', '') for i in f.readlines()]
    print("|".join(lines))
