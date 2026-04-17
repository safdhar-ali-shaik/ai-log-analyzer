from analyzer.basic_analyzer import analyze_log

with open("logs.txt") as f:
    for line in f:
        result = analyze_log(line)
        print(result)
