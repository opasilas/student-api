#!/bin/bash

# Define the target node
TARGET_NODE="dependency"

# Get a list of all deployments in the argocd namespace
DEPLOYMENTS=$(kubectl get deployments -n argocd -o jsonpath='{.items[*].metadata.name}')

# Loop through each deployment and patch it with the node selector
for DEPLOYMENT in $DEPLOYMENTS; do
  kubectl patch deployment $DEPLOYMENT -n argocd --type='json' -p="[
    {
      \"op\": \"add\",
      \"path\": \"/spec/template/spec/nodeSelector\",
      \"value\": {
        \"name\": \"$TARGET_NODE\"
      }
    }
  ]"
done

echo "All deployments in the argocd namespace have been patched with the node selector."
