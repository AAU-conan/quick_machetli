import sys
from pathlib import Path
from subprocess import CompletedProcess

from machetli import tools

class RunEnvironment:
    def run_planner(self, sas_file: Path, configuration: str) -> CompletedProcess[str]:
        raise NotImplementedError()

class LocalRunEnvironment(RunEnvironment):
    def __init__(self, planner: Path):
        self.planner = planner

    def run_planner(self, sas_file: Path, configuration: str) -> CompletedProcess[str]:
        cmd = [str(self.planner), "--search", configuration]
        print(cmd)
        result = tools.run(
            cmd, input_filename=sas_file, cpu_time_limit=30, memory_limit=1024, text=True
        )
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return result


class MCCCplexRunEnvironment(RunEnvironment):
    LP_SOLVER_PATH = Path("/nfs/home/cs.aau.dk/bx56lg/bin/CPLEX_Studio2211/cplex")
    def __init__(self, planner: Path):
        self.planner = planner # Path to singularity image

    def run_planner(self, sas_file: Path, configuration: str) -> CompletedProcess[str]:
        cmd = ["../../../../run-singularity.sh", self.planner, self.LP_SOLVER_PATH, str(sas_file), "--search", configuration]
        print(cmd)
        result = tools.run(
            cmd, cpu_time_limit=15*60, memory_limit=32000, text=True
        )
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return result

class LocalProbfdRunEnvironment(RunEnvironment):
    def __init__(self, planner: Path, time_limit=30):
        self.planner = planner
        self.time_limit = time_limit

    def run_planner(self, sas_file: Path, configuration: str) -> CompletedProcess[str]:
        cmd = [str(self.planner), "search", configuration, str(sas_file)]
        print(cmd)
        result = tools.run(
            cmd, cpu_time_limit=self.time_limit, memory_limit=1024, text=True
        )
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return result

class LocalPyperplanRunEnvironment(RunEnvironment):
    def __init__(self, planner: Path):
        self.planner = planner

    def run_planner(self, sas_file: Path, configuration: str) -> CompletedProcess[str]:
        cmd = ["./.venv/bin/python", "pyperplan", str(sas_file)] + configuration.split(" ")
        print(cmd)
        result = tools.run(
            cmd, cpu_time_limit=30, memory_limit=1024, text=True, cwd=self.planner
        )
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return result