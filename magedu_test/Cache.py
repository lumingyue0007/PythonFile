# 实现一个cache装饰器，实现可以过期被清除的功能
# 思路：要缓存==》函数的输入参数和返回参数都相同==》定义一个函数（位置和关键字传参，缺省值），通过函数签名
# 拿到函数的位置参数，关键字参数，缺省值等，根据情况构建指定的输入条件，只要输入参数相同，则返回缓存区的值
import functools
import inspect
import time
import datetime

def logger(fn):
    @functools.wraps(fn)
    def _logger(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__, delta)
        return ret
    return _logger

def cache(fn):
    local_cache = {} # 不同的函数名是不同的cache
    @functools.wraps(fn)
    def _cache(*args, **kwargs):
        def _clear_cache():
            # cache清除===>调用时清除
            expire_key = []
            for k, (_, stamp) in local_cache.items():
                if datetime.datetime.now().timestamp() - stamp > 5:
                    expire_key.append(k)
            for k in expire_key:
                local_cache.pop(k)

        def _make_key(args, kwargs):
            # 函数签名
            sig = inspect.signature(fn)
            params = sig.parameters
            keys = tuple(params.keys())
            params_dict = {}
            # 传参
            params_dict.update(zip(keys, args))
            params_dict.update(kwargs)
            # 缺省值
            for k, v in params.items():
                if k not in params_dict:
                    params_dict[k] = v.default
            key = tuple(sorted(params_dict.items()))
            return key, params_dict

        _clear_cache()

        key, params_dict = _make_key(args, kwargs)

        if key not in local_cache.keys():
            local_cache[key] = fn(**params_dict), datetime.datetime.now().timestamp()
        print(local_cache)
        return local_cache[key][0]
    return _cache

@logger
@cache
def add(x=1, y=4):
    time.sleep(3)
    return x + y

print(add(y=4))
