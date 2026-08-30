# Security policy

## Supported versions

This project is pre-alpha. Security fixes are applied to the current `main`
branch; no versioned support window is offered yet.

## Reporting a vulnerability or sensitive-data exposure

Please use GitHub's private vulnerability reporting for this repository. If
the report concerns accidentally committed sensitive material, do not quote or
reproduce that material in a public issue.

Include the affected component, reproduction steps using synthetic data, the
potential impact, and any suggested mitigation. Public disclosure should wait
until the issue has been assessed and a safe remediation path is available.

## Security boundary

The current implementation demonstrates deterministic manifest validation,
path containment, and role filtering. It is not a production identity or
authorization system and is not certified for classified, regulated, or
security-critical use.
