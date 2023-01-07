import nox


@nox.session(python="3.11", reuse_venv=True)
def dev(session):
    """For creating a development virtual environment. Handy for setting interpreter in
    IDE.
    """
    session.install("-r", "test-requirements.txt")


@nox.session(python="3.11", reuse_venv=True)
def format(session):
    session.install("black")
    session.run("black", "src", "tests", *session.posargs)
