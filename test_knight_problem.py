from knight_problem import search, print_results
def test_knight_problem(board_size):
    print_results(board_size)

def test_5(capsys):
    expected_5 = '\n'.join((
            '4 4 2 8',
            '4 2 4 4',
            '2 4 -1 -1',
            '8 4 -1 1\n'))
    captured = capsys.readouterr()
    print_results(5)
    captured = capsys.readouterr()
    print("Output:")
    print(captured.out)
    assert expected_5 == captured.out

def test_6(capsys):
    expected_6 = '\n'.join((
            '5 4 3 2 5',
            '4 -1 2 -1 -1',
            '3 2 -1 -1 -1',
            '2 -1 -1 -1 -1',
            '5 -1 -1 -1 1\n'))
    captured = capsys.readouterr()
    print_results(6)
    captured = capsys.readouterr()
    print("Output:")
    print(captured.out)
    assert expected_6 == captured.out
