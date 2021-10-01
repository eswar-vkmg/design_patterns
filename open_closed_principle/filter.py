from specification import Specification


class Filter:
    def filter(self, items, spec):
        pass


class ItemFilter(Filter):
    def filter(self, items, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item
