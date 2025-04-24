from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint

from machetli import sas, search, environments


parser = ArgumentParser()
parser.add_argument("sas_file", type=Path)
parser.add_argument("evaluator_file", type=Path)
args = parser.parse_args()

initial_state = sas.generate_initial_state(args.sas_file)

result = search(
    initial_state,
    [
        sas.RemoveOperators(),
        sas.RemoveVariables(),
        sas.RemovePrePosts(),
        sas.SetUnspecifiedPreconditions(),
        sas.MergeOperators(),
        sas.RemoveGoals(),
    ],
    Path(__file__).parent / args.evaluator_file,
    # environments.SlurmEnvironment(exp_name=args.evaluator_file.stem, partition=args.partition, memory_per_cpu="32000M"),
    environments.LocalEnvironment(exp_name=args.evaluator_file.stem),
)

sas.write_file(result, "result.sas")
pprint(result)
