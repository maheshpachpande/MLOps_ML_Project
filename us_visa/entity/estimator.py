class TargetValueMapping:
    def __init__(self):
        self.mapping = {
            "Certified": 0,
            "Denied": 1
        }

    def as_dict(self) -> dict:
        return self.mapping

    def reverse_mapping(self) -> dict:
        return {value: key for key, value in self.mapping.items()}
