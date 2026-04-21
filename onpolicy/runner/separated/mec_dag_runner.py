from onpolicy.runner.separated.base_runner import Runner


class MECDAGRunner(Runner):
    """Separated-policy runner placeholder for the future MEC-DAG task."""

    def run(self):
        raise NotImplementedError(
            "Implement separated MEC-DAG rollout logic in onpolicy/runner/separated/mec_dag_runner.py."
        )

    def warmup(self):
        raise NotImplementedError

    def collect(self, step):
        raise NotImplementedError

    def insert(self, data):
        raise NotImplementedError
