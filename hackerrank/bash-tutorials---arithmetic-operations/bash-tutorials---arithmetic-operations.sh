#!/bin/bash

read X
printf "%.3f\n" $(echo $X | bc -l)