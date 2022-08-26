from typing import List

import wikipedia


class Wiki:

    def __init__(self) -> None:
        self.w = wikipedia
        self.w.set_lang('pt')
        self.results = dict()

    def search(self, query) -> List[str]:
        self.results[query] = self.w.search(query)
        return self.results
