from src import jobs


def get_unique_job_types(path):
    all_jobs = jobs.read(path)
    jobs_categories = []
    for job in all_jobs:
        if job["job_type"] in jobs_categories:
            pass
        else:
            jobs_categories.append(job["job_type"])

    return jobs_categories


def filter_by_job_type(jobs, job_type):
    result = [job for job in jobs if job["job_type"] == job_type]
    return result


def get_unique_industries(path):
    all_jobs = jobs.read(path)
    industries_list = []
    for job in all_jobs:
        if job["industry"] in industries_list:
            pass
        elif job["industry"] == "":
            pass
        else:
            industries_list.append(job["industry"])

    return industries_list


def filter_by_industry(jobs, industry):
    result = [job for job in jobs if job["industry"] == industry]
    return result


def get_max_salary(path):
    all_jobs = jobs.read(path)
    salairies_list = []
    for job in all_jobs:
        if job["max_salary"]:
            try:
                salairies_list.append(int(job["max_salary"]))
            except ValueError:
                continue
    return max(salairies_list)


def get_min_salary(path):
    all_jobs = jobs.read(path)
    salairies_list = []
    for job in all_jobs:
        if job["min_salary"]:
            try:
                salairies_list.append(int(job["min_salary"]))
            except ValueError:
                continue
    return min(salairies_list)
    pass


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Houston...")
    if (
        type(job["max_salary"]) is not int
        or type(job["min_salary"]) is not int
    ):
        raise ValueError("...we Have...")
    if job["max_salary"] < job["min_salary"]:
        raise ValueError("...A...")
    if type(salary) is not int:
        raise ValueError('PROBLEM')
    result = job["min_salary"] <= salary <= job["max_salary"]
    return result


def filter_by_salary_range(jobs, salary):
    list_salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_salaries.append(job)
        except ValueError:
            pass
    return list_salaries
