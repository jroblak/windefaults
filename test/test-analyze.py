from pathlib import Path

from analyze import analyze


def test_processs():
    differences = analyze("processes", Path("test/testcases/process-test.csv"), "10")
    assert len(differences) == 1
    assert list(differences)[0] == "badthing"


def test_services():
    differences = analyze("services", Path("test/testcases/service-test.csv"), "2012")
    assert len(differences) == 1
    assert list(differences)[0] == "badservice"
