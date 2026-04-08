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
