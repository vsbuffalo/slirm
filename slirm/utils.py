import os
import tqdm
import numpy as np
SEED_MAX = 2**32-1

def get_files(dir, suffix):
    """

    Recursively get files from directories in dir with suffix, e.g. used for
    getting all .tree files across seed subdirectories.
    """
    all_files = set()
    for root, dirs, files in os.walk(dir):
        for file in files:
            if suffix is not None:
                if not file.endswith(suffix):
                    continue
            all_files.add(os.path.join(root, *dirs, file))
    return all_files

def param_grid(params, add_seed=False, rng=None):
    """
    Generate a Cartesian product parameter grid from a
    dict of grids per parameter, optionally adding the seed.
    """
    grid = []
    for param, values in params.items():
        if len(values):
            grid.append([(param, v) for v in values])
        else:
            grid.append([(param, '')])
    def convert_to_dict(x):
        # and package seed if needed
        x = dict(x)
        if add_seed:
            x['seed'] = random_seed(rng)
        return x
    return map(convert_to_dict, itertools.product(*grid))

def signif(x, digits=4):
    if x == 0:
        return 0.
    if np.isnan(x):
        return np.nan
    return np.round(x, digits-int(floor(log10(abs(x))))-1)

def make_dirs(*args):
    "Make directory if necessary"
    dir = os.path.join(*args)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def random_seed(rng=None):
    if rng is None:
        return np.random.randint(0, SEED_MAX)
    return rng.integers(0, SEED_MAX)

