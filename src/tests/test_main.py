from lifts.lifts import main


def test_prints_expected_message(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from lifts.py!"


def test_does_not_return_any_value():
    assert main() is None
