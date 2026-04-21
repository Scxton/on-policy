from onpolicy.runner.shared.base_runner import Runner


class MECDAGRunner(Runner):
    """Shared-policy runner placeholder for the future MEC-DAG task."""

    def run(self):
        raise NotImplementedError(
            "Implement shared MEC-DAG rollout logic in onpolicy/runner/shared/mec_dag_runner.py."
        )

    def warmup(self):
        raise NotImplementedError

    def collect(self, step):
        raise NotImplementedError

    def insert(self, data):
        raise NotImplementedError
