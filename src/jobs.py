from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        jobs_file = csv.DictReader(file)
        result = []
        for row in jobs_file:
            result.append(row)
    return result
