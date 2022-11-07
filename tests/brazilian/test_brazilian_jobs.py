from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    response = read_brazilian_file(path)
    assert response[0] == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
    assert response[1] == {
        "title": "Motorista",
        "salary": "3000",
        "type": "full time",
    }
    assert response[2] == {
        "title": "Analista de Software",
        "salary": "4000",
        "type": "full time",
    }
