from agents.scanner  import ScannerAgent

scanner = ScannerAgent("./agents")
files = scanner.scan()

for f in files:
    print(f)
