#!/usr/bin/env python
from livereload.task import Task
from livereload.compiler import shell

# You may have a different path, e.g. _source/
Task.add('source/', shell('make html'))

