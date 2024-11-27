#!/bin/bash

curl -X POST http://localhost:8080/v1/graphql \
-H "Content-Type: application/json" \
-d "{\"query\": \"{ Get { SimSearch(where: { path: [\\\"question\\\"], operator: Like, valueString: \\\"organ\\\" }) { question answer category } } }\"}"
