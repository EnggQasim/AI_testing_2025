The error you're seeing is because the -k option requires an argument to specify which tests to run. However, if you want to see verbose output from pytest, you should use the -v or -vv flag. Here's how you can run the tests with verbose output:
v
Or for even more verbose output:
```cmd
 uv run pytest ./tests/test_human.py -vv
```
The -v flag will show:
The name of each test being run
Whether it passed or failed
More detailed information about any failures
The -vv flag provides even more detail in the output.
If you want to combine this with test selection using -k, you would need to provide a pattern, like:
uv run pytest ./tests/test_human.py -v -k "test_human_initialization"
This would run only the tests matching "test_human_initialization" with verbose output.