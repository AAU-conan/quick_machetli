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

if not args.no_delete:
    # Delete the eval folder if it exists
    eval_folder = Path(__file__).parent / f"{args.evaluator_file.stem}-eval"
    if eval_folder.exists():
        rmtree(eval_folder)


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
        sas.RemoveVariableValues(),
    ],
    Path(__file__).parent / args.evaluator_file,
    environments.LocalEnvironment(exp_name=args.evaluator_file.stem),
)

sas.write_file(result, "result.sas")
pprint(result)
