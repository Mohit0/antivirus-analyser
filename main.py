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
