#!/usr/bin/bash
if [ $(grep x testfile -o | wc -l) -eq $(grep y testfile -o | wc -l) ]; then
	echo "Equal"
else
	echo "Not Equal"
fi
