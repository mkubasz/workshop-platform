from dataclasses import dataclass


@dataclass
class Result:
    error: str = None
    data: object = None

    def is_ok(self) -> bool:
        return self.data is not None and self.error is None

    def then(self, func: callable) -> 'Result':
        if self.is_ok():
            return Result(data=func(self.data))
        else:
            return Result(error=self.error)
