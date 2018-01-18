from knight import print_results, knight_factory, Searcher
def test_print_results(request):
    n = request.config.getoption("--board_size")
    print(f"n: {n} type(n): {type(n)}")
    print(f"{80*'*'}\nNow on n = {n}\n{80*'*'}\n")
    print_results(n)
    print(f"Instance count: {Searcher.instance_count}")

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

def test_6_1_2():
    K = knight_factory(6)
    result = K(1,2).search()
    print(f"Result for K(1,2) is: {result}")
    assert result == 4
    print(f"Instance count: {Searcher.instance_count}")


def test_param(request):
    n = request.config.getoption("--board_size")
    param = request.config.getoption("--param")
    print(f"n: {n} type(n): {type(n)}")
    print(f"{80*'*'}\nNow on n = {n}, param=({param[0]},{param[1]})\n{80*'*'}\n")
    K = knight_factory(n)
    result = K(*param).search()
    print(f"Result: {result}")
    print(f"Instance count: {Searcher.instance_count}")

