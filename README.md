# MEC-DAG PPO Skeleton

This repository is now trimmed into a PPO-centered training skeleton for the future multi-user, multi-server MEC-DAG offloading task.

## Project Rule

Before every Python command, training script, or test script, activate the project environment first:

```bash
conda activate dl
```

## What Remains

- `onpolicy/algorithms/r_mappo/`: PPO updater, policy wrapper, actor, critic
- `onpolicy/utils/shared_buffer.py`: shared rollout buffer and GAE
- `onpolicy/utils/separated_buffer.py`: separated rollout buffer and GAE
- `onpolicy/runner/shared/base_runner.py`: shared-policy runner framework
- `onpolicy/runner/separated/base_runner.py`: separated-policy runner framework
- `onpolicy/envs/env_wrappers.py`: vectorized environment wrappers

## Removed Legacy Content

- MPE wrappers and training scripts
- SMAC/StarCraft wrappers and training scripts
- Hanabi wrappers and evaluation scripts
- Football task-specific wrappers and scripts
- HAPPO, HATRPO, MAT and their helper scripts

## MEC-DAG Replacement Points

The following files are the intended integration points for the new MEC-DAG simulator:

- `onpolicy/envs/mec_dag/mec_dag_env.py`: implement the MEC-DAG environment class here
- `onpolicy/runner/shared/mec_dag_runner.py`: implement shared-policy rollout logic here
- `onpolicy/runner/separated/mec_dag_runner.py`: implement separated-policy rollout logic here
- `onpolicy/scripts/train/train_mec_dag.py`: wire parser, environment creation, and runner selection here

## Installation

```bash
conda activate dl
pip install -e .
```

