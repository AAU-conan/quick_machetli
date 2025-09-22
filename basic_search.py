from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint
from shutil import rmtree


from machetli import sas, search, environments


parser = ArgumentParser()
parser.add_argument("sas_file", type=Path)
parser.add_argument("evaluator_file", type=Path)
parser.add_argument("-D", "--no-delete", action="store_true", help="Do not delete eval folder")
args = parser.parse_args()

initial_state = sas.generate_initial_state(args.sas_file)

result = search(
    initial_state,
    [
        sas.MultiSuccessorGenerator([sas.RemoveOperators() for _ in range(5)]),
        sas.RemoveOperators(),
        sas.RemoveVariables(),
        sas.RemovePrePosts(),
        sas.SetUnspecifiedPreconditions(),
        sas.MergeOperators(),
        sas.RemoveGoals(),
        sas.RemoveVariableValues(), # May be buggy
    ],
    Path(__file__).parent / args.evaluator_file,
    environments.LocalEnvironment(exp_name=args.evaluator_file.stem),
    improving_successor_callback=lambda state: sas.write_file(state, "intermediate.sas")
)

sas.write_file(result, "result.sas")
pprint(result)
