# API worker queue
A push to `main` that changes `native-api-queue/<lane>.json` starts `native-api-worker.yml` with that task (the lead does this; ≤ 2 lanes: a, b).
`{"task": "native/tasks/api-NN.md", "base": "native/lead-0111", "branch": "native/api-N"}` — the task file lives in the private repo.
