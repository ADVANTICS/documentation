#!/bin/bash

docker run -it --rm -v "`pwd`:/app" --name docsify -p 3000:3000 advantics/docsify $*
