import sys
from pathlib import Path
from subprocess import CompletedProcess

from machetli import tools

def run_planner(sas_file: Path, planner: Path, configuration: str) -> CompletedProcess[str]:
    cmd = [str(planner), "--search", configuration]
    print(cmd)
    result = tools.run(
        cmd, input_filename=sas_file, cpu_time_limit=30, memory_limit=1024, text=True
    )
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    return result
