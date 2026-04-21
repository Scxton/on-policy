class MECDAGEnv:
    """Replacement point for the custom MEC-DAG simulation environment."""

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "Implement the MEC-DAG simulator in onpolicy/envs/mec_dag/mec_dag_env.py."
        )
