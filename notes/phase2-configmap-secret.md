# Phase: ConfigMap and Secret

## Goal
Separate application configuration from the container image and deployment logic.

## Key ideas
- ConfigMap stores non-sensitive configuration.
- Secret stores sensitive values such as API keys or tokens.
- Secrets are not strong encryption by default; they are base64-encoded unless cluster-level encryption is enabled.
- Applications should not hardcode environment-specific or sensitive values.

## What changed
- Added `configmap.yaml` for runtime settings.
- Added `secret.yaml` for sensitive configuration.
- Updated Deployment to consume both via `envFrom`.

## Why this matters
This makes the application more portable, reusable, and safer to operate across environments.
