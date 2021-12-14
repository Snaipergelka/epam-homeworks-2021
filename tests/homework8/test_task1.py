from homework8.task1 import Reader


def test_check_load_from_file():
    storage = Reader('correct.txt')
    assert storage.a == 342 and storage['sdd'] == 'hurma' and storage.key == "value234"


def test_invalid_key(capsys):
    try:
        storage = Reader('wrong.txt')
    except Exception as e:
        assert type(e) is ValueError


# TODO add tests for consisntence
