import redis
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.UtilityExternal.Interface.ICacheRedisUti import ICacheRedisUti
from src.infradata.Connection.RedisConnection import RedisConnectionHandle

redis_connection = RedisConnectionHandle().connect()


class CacheRedisUti(ICacheRedisUti):

    def get_string_async_wrapper(cls, key: str) -> str:
        value = redis_connection.get(key)
        if value != None:
            return value.decode('utf-8')
        else:
            return value

    def remove_wrapper(cls, key: str) -> int:
        remove_value = redis_connection.delete(
            key)  # 1 removido, 0 não removido
        return remove_value

    def set_string_async_wrapper(cls, key: str, value: str) -> bool:
        result: bool = redis_connection.set(key, value)
        print(result)

    def set_string_async_wrapper_expiry(cls, key: str, value: str, expiry_seconds: int) -> bool:
        result: bool = redis_connection.set(key, value, expiry_seconds)
        return result
