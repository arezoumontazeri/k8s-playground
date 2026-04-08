# Phase 2 - Kubernetes Probes

## Goal
Learn how Kubernetes determines whether an application is:
- alive
- ready to receive traffic
- still starting up

## Topics
- livenessProbe
- readinessProbe
- startupProbe

## Validation
- Pod can be running but not Ready
- Service should not send traffic to unready Pods
- Observe probe events with kubectl describe


## Final validation result

After fixing the readiness endpoint to return HTTP 503:

- New Pods remained `Running` but stayed `0/1 Ready`
- The Deployment rollout did not complete
- Old Pods remained active to serve traffic
- Readiness probe failures were observed in `kubectl describe pod`

This confirms that:
- readinessProbe is working correctly
- Kubernetes does not route traffic to unready Pods
- rolling updates are blocked when new Pods are not ready

## What I learned
- Minimal containers often do not include debugging tools like curl
- Readiness probe failure keeps Pods running but removes them from traffic
- Rolling updates stop when new Pods are not ready
- Old Pods are preserved to maintain availability
- Kubernetes relies on HTTP status codes (503) for readiness failure



## Common mistakes
- Trying to use curl inside minimal containers without installing it
- Assuming readiness failure will stop the container (it does not)
- Ignoring the READY column and focusing only on STATUS

