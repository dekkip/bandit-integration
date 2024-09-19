# bandit-integration
I'm practicing on how to integrate bandit onto my CI / CD.

## CI/CD Pipeline
The CI/CD pipeline is configured to run Bandit on every push and pull request. If high-severity vulnerabilities are detected, the build will fail.

### How to Fix Vulnerabilities
1. Check the Actions tab for the workflow run details.
2. Review the Bandit output to identify high-severity vulnerabilities.
3. Fix the issues in your code.
4. Commit and push the changes to trigger the workflow again.

### Running Bandit Locally
To run Bandit locally, use the following command:
```bash
bandit -r src/ -f json -o bandit_output.json --severity-level high
