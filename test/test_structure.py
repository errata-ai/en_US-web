from conftest import file_io


@file_io
def test_structure(dic):
    lines = dic.readlines()
    count = int(lines.pop(0).strip())

    assert len(lines) == count
    assert sorted(lines, key=str.lower) == lines
