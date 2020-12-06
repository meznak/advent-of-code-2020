from ..shared import parse_input, run_solvers
from . import parse_data, solve_1, solve_2, SAMPLE_SOLUTIONS

if __name__ == '__main__':
    samples, data = parse_input(__file__, parse_data)

    run_solvers(samples, data, [solve_1, solve_2], SAMPLE_SOLUTIONS)
