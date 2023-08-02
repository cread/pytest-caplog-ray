# pytest-caplog-ray

This is a small example showing how just doing `import ray` can break logging
when using `pytest` and Ray 2.6.1. Ray 2.5.1 did not have this problem.

If importing Ray is enough to break this simple case, it's also breaking other
parts of logging your code depends on.

## Environment setup

This example uses `conda`. Create your environments with the command:

```
conda env create -f env-ray-2.5.1.yml
conda env create -f env-ray-2.6.1.yml
```

## Showing the problem

When run with Ray 2.5.1 the test passes:

```
$ conda activate pytest-caplog-ray-2.5.1
$ pytest
...
=== 1 passed, 7 warnings in 0.26s ===
```

When run with Ray 2.6.1 the test fails:

```
$ conda activate pytest-caplog-ray-2.6.1
$ pytest
...
=== 1 failed, 7 warnings in 0.27s ===
```
