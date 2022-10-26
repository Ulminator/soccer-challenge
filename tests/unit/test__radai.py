import argparse

import pytest


def test__cli_default_args(mocker, capsys):
    from radai import cli

    # GIVEN default args for the cli
    main_patch = mocker.patch('radai.__main__.main')
    result = ['1. Tarantulas, 6 pts', '2. Lions, 5 pts']
    main_patch.side_effect = [result]

    # WHEN invoking the cli
    cli()

    # THEN the main function is called with the default args
    main_patch.assert_called_once()

    _, kwargs = main_patch.call_args

    assert len(kwargs) == 1
    assert kwargs['input_file'] == './sample-input.txt'

    # AND the result is printed to stdout
    out, err = capsys.readouterr()

    assert out == '\n'.join(result) + '\n'
    assert err == ''


def test__cli_non_default_args(mocker):
    from radai import cli

    # GIVEN non default arguments for the cli
    input_file = 'dummy'

    arg_patch = mocker.patch('argparse.ArgumentParser.parse_args')
    arg_patch.return_value = argparse.Namespace(input_file=input_file)
    main_patch = mocker.patch('radai.__main__.main')

    # WHEN invoking the cli
    cli()

    # THEN the main function is called with the provided args
    main_patch.assert_called_once()

    _, kwargs = main_patch.call_args

    assert len(kwargs) == 1
    assert kwargs['input_file'] == input_file


def test__team_score_from_entry():
    from radai.__main__ import _team_score_from_entry

    team = 'Lions'
    score = 3
    entry = f'{team} {str(score)}'

    ts = _team_score_from_entry(entry)

    assert ts.team == 'Lions'
    assert ts.score == 3


@pytest.mark.parametrize('line, lions_pts, snakes_pts', [
    ('Lions 1, Snakes 1', 1, 1),
    ('Lions 1, Snakes 0', 3, 0),
    ('Lions 0, Snakes 1', 0, 3),
])
def test__team_points_from_file_cases(mocker, line, lions_pts, snakes_pts):
    from radai.__main__ import _team_points_from_file

    # GIVEN valid input file
    mock_open = mocker.mock_open(read_data=line)
    mocker.patch('builtins.open', mock_open)

    # WHEN retrieving team points from file
    team_points = _team_points_from_file('dummy')

    # THEN the teams have appropriate points
    assert len(team_points) == 2
    assert team_points['Lions'] == lions_pts
    assert team_points['Snakes'] == snakes_pts


def test__team_points_from_file(mocker):
    from radai.__main__ import _team_points_from_file

    # GIVEN valid input file
    input_file_lines = [
        'Lions 3, Snakes 3',
        'Tarantulas 1, FC Awesome 0',
        'Lions 1, FC Awesome 1',
        'Tarantulas 3, Snakes 1',
        'Lions 4, Grouches 0',
    ]
    input_file_content = '\n'.join(input_file_lines)

    mock_open = mocker.mock_open(read_data=input_file_content)
    mocker.patch('builtins.open', mock_open)

    # WHEN retrieving team points from file
    team_points = _team_points_from_file('dummy')

    # THEN the teams have appropriate points
    assert len(team_points) == 5
    assert team_points['Lions'] == 5
    assert team_points['Snakes'] == 1
    assert team_points['Tarantulas'] == 6
    assert team_points['FC Awesome'] == 1
    assert team_points['Grouches'] == 0


def test__generate_ranking_lines():
    pass


def test__main():
    pass
