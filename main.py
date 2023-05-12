import my_analyzer
import os


def one_by_one(file_path):
    path = os.listdir(str(os.path.dirname(os.path.realpath(__file__))))
    for bin_file in path:
        if ".bin" in str(bin_file):
            # print(bin_file)
            try:
                ANALYZER = my_analyzer.YaraFileAnalyzer(str(bin_file))
                NUM_YARA_RULES = ANALYZER.num_rules
                # print(NUM_YARA_RULES)
                result = ANALYZER.analyze(file_path)
                if result:
                    print(result)
                    return "Malicious"
            except Exception as e:
                print(e)
    return "Clean"


def scan_bulk_files():
    print("Scanning all files in payload folder.")
    files = os.listdir("payloads")
    for filename in files:
        path = str(os.path.join("payloads", filename))
        if str(one_by_one(path)) == "Clean":
            print(path)


# scan_bulk_files()
