#!/bin/bash

read X

[[ "$X" == "Y" || "$X" == "y" ]] && echo "YES" || echo "NO"