from src.sorting import sort_by

jobs = [
    {
        "min_salary": 10000,
        "max_salary": 24000,
        "date_posted": "2022-01-12",
    },
    {
        "min_salary": 28000,
        "max_salary": 42000,
        "date_posted": "2024-07-31",
    },
    {
        "min_salary": 15000,
        "max_salary": 23000,
        "date_posted": "2021-06-06",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 10000

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 42000

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2024-07-31"
