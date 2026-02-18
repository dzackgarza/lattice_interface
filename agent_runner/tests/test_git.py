from agent_runner import git


def test_parse_numstat():
    output = "3\t1\tsrc/a.py\n2\t0\tsrc/b.py\n"
    files, insertions, deletions = git.parse_numstat(output)
    assert files == ["src/a.py", "src/b.py"]
    assert insertions == 5
    assert deletions == 1
