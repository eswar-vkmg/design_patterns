class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class OSSpecification(Specification):
    def __init__(self, os):
        self.os = os

    def is_satisfied(self, item):
        return item.os == self.os


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class ProcessorSpecification(Specification):
    def __init__(self, processor):
        self.processor = processor

    def is_satisfied(self, item):
        return item.processor == self.processor


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(
            map(
                lambda spec: spec.is_satisfied(item),
                self.args
            )
        )


class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return any(
            map(
                lambda spec: spec.is_satisfied(item),
                self.args
            )
        )