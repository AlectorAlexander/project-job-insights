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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
