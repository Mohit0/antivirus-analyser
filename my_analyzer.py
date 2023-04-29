import yara


class YaraFileAnalyzer:
    def __init__(self, compiled_rules_file: str) -> None:
        self._rules = yara.load(compiled_rules_file)
        self._compiled_rules_file = compiled_rules_file

    @property
    def num_rules(self) -> int:
        return sum(1 for _ in self._rules)

    def analyze(self, target_file: str):
        raw_yara_matches = self._rules.match(target_file)
        # print(raw_yara_matches)
        return raw_yara_matches
