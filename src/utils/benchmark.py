import time
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)

class Benchmark:
    time_units = {
        'seconds': 1e9,
        'milliseconds': 1e6,
        'microseconds': 1e3,
        'nanoseconds': 1,
    }

    def __new__(cls, func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter_ns()
            result = func(*args, **kwargs)
            end_time = time.perf_counter_ns()

            elapsed_time = (end_time - start_time)
            for unit, factor in cls.time_units.items():
                if elapsed_time >= factor:
                    logging.info(f"Function {func.__name__} - {elapsed_time / factor:.2f} {unit}")
                    break
            return result
        return wrapper
