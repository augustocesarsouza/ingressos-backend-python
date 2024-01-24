from abc import ABC, abstractmethod


class ICacheRedisUti(ABC):

    @abstractmethod
    def get_string_async_wrapper(cls, key: str) -> str:
        pass

    @abstractmethod
    def remove_wrapper(cls, key: str) -> int:
        pass

    @abstractmethod
    def set_string_async_wrapper(cls, key: str, value: str) -> bool:
        pass

    @abstractmethod
    def set_string_async_wrapper_expiry(cls, key: str, value: str, expiry_seconds: int) -> bool:
        pass
