## Slirm -- Slurm SLiM Runner

This dispatches Slim jobs on a Slurm cluster very efficiently. I tore this code
out from an existing project -- I will come back to clean this up later, but it
may be useful to some now. I don't have much time to fix bugs, etc, but please
feel free to submit pull requests etc.

If you end up using this in a project, do email to let me know!

## Example Run

    python  slurm_slim_runner.py --slim '~/src/SLiM_build/slim' --secs-per-job 10 --batch-size 150 --seed 3 config.json

`config.json` is a JSON file with the parameters to simulate under. Currently
grids work best, but you can also randomly sample parameters (see
`slirm/samplers.py` for options). `--batch-size` is how many simulation
commands (jobs) to combine into a batch. For short running simulations, this
should be many to ease the load of the cluster. `--secs-per-job` is how many
seconds it takes (approximately) for each simulation to complete; this is used
for time allocation (and is multiplied by the batch size per job, times some
factor).

## Things that should be changed

 - Set a more unique name for jobs to prevent clashes, etc

