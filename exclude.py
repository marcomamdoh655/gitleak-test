with open("filestobeexcluded.txt", "r") as f:
    lines = [
        line.replace("\n", "").strip()
        for line in f.readlines()
        if line.replace("\n", "").strip()
    ]
    print("|".join(lines))
