import argparse
import csv
from collections import defaultdict, namedtuple
from typing import Dict, List

TeamPointTotal = namedtuple(
    'TeamPointTotal',
    ['team', 'point_total']
)


def _team_points_from_file(file_: str) -> Dict[str, int]:
    TeamScore = namedtuple(
        'TeamScore',
        ['team', 'score']
    )

    def _team_score_from_entry(entry: str) -> TeamScore:
        entry_list = entry.split()
        score = entry_list[-1]
        team = ' '.join(entry_list[:-1])
        return TeamScore(team, int(score))

    team_points: Dict[str, int] = defaultdict(int)

    with open(file_, 'r') as fp:

        reader = csv.DictReader(fp, fieldnames=['left', 'right'])
        for row in reader:
            left: TeamScore = _team_score_from_entry(row['left'])
            right: TeamScore = _team_score_from_entry(row['right'])

            if left.score > right.score:
                team_points[left.team] += 3
                team_points[right.team]
            elif left.score < right.score:
                team_points[left.team]
                team_points[right.team] += 3
            else:
                team_points[left.team] += 1
                team_points[right.team] += 1

    return team_points


def _generate_ranking_lines(tpt_list: List[TeamPointTotal]) -> List[str]:
    prev_point_total = None
    current_rank = 0
    ranks_skipped = 0
    ranking_lines = []
    for tpt in tpt_list:
        if (
            prev_point_total is None or tpt.point_total != prev_point_total
        ):
            current_rank += 1 + ranks_skipped
        else:
            ranks_skipped += 1

        suffix = 'pt' if tpt.point_total == 1 else 'pts'
        ranking_line = (
            f'{current_rank}. {tpt.team}, {tpt.point_total} {suffix}'
        )
        ranking_lines.append(ranking_line)

        prev_point_total = tpt.point_total

    return ranking_lines


def main(input_file: str) -> List[str]:

    # Get team points for every game
    team_points = _team_points_from_file(input_file)

    # Sorts teams by points descending, then by team name ascending
    team_point_total_list: List[TeamPointTotal] = [
        TeamPointTotal(x[0], x[1])
        for x in sorted(
            team_points.items(),
            key=lambda item: (-item[1], item[0]),
        )
    ]

    # Build up list for output
    return _generate_ranking_lines(team_point_total_list)


def cli():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--input-file',
        required=False,
        default='./sample-input.txt',
        dest='input_file',
    )
    args = arg_parser.parse_args()

    result = main(**vars(args))
    print('\n'.join(result))


if __name__ == '__main__':
    cli()
