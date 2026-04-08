# Phase 02 - Kubernetes Probes

## Goal
Understand how Kubernetes checks whether an application is alive, ready for traffic, and still starting up.

## Probe types

### Liveness Probe
Checks whether the container is still healthy.
If it fails repeatedly, Kubernetes restarts the container.

### Readiness Probe
Checks whether the application is ready to receive traffic.
If it fails, the Pod stays running but is removed from Service endpoints.

### Startup Probe
Gives slow-starting applications time to boot.
Until it succeeds, Kubernetes delays normal liveness/readiness behavior.

## Implementation
The Deployment uses:
- `/healthz` for liveness
- `/readyz` for readiness
- `/healthz` for startup validation

## Validation steps
1. Deploy the application with probes enabled
2. Confirm Pods become `1/1 Ready`
3. Set `APP_READY=false`
4. Restart the Deployment
5. Confirm Pods are `Running` but `0/1 Ready`
6. Check `kubectl describe pod`
7. Verify the Service does not route traffic to unready Pods

## Key takeaway
A running Pod is not necessarily a ready Pod.
Readiness controls traffic.
Liveness controls restarts.
Startup prevents premature failure during boot.
