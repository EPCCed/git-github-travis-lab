MSc Programming Skills - Git, GitHub, Travis lab
================================================

A lab session, using Git, GitHub and Travis CI to write and run tests using a shared repository.

In the following text:

* Replace `USERNAME` with your GitHub user name.
* Replace `INSTRUCTOR` with the GitHub user name of your instructor (they'll tell you what this is).

Sign in to GitHub
-----------------

If you do not already have an account, then visit [GitHub](https://github.com) and create a free account.

If you already have an account, then visit [GitHub](https://github.com) and sign in.

Fork this repository on GitHub
------------------------------

On the page for the instructor's repository, https://github.com/INSTRUCTOR/git-github-travis-lab, click Fork.

If asked "Where should we fork this repository?", select your account.

Clone your fork locally
-----------------------

Within a terminal window, clone your fork:

```
$ git clone https://github.com/USERNAME/git-github-travis-lab
$ cd git-github-travis-lab
$ ls
```

Run the ROT-13 code
-------------------

`msc/rot13.py` holds an implementation of ROT-13, a substitution cipher. The code originates from [Literate Programs](http://en.literateprograms.org/Rot13_(Python)). For more on ROT-13 substitution cipher, see [Wikipedia](https://en.wikipedia.org/wiki/ROT13).

To encrypt a word, run the code as follows:

```
$ python msc/rot13.py hello
uryyb
```

Look at the `.travis.yml` job file
----------------------------------

Travis CI looks for a file called `.travis.yml` in a Git repository. This file tells Travis CI how to build and test your software. In addition, this file can be used to specify any dependencies you need installed before building or testing your software. 

Look at the one in this repository:

```
$ cat .travis.yml
```

```
language: python
```

The `language` section tells Travis CI which build environment it should use. 

```
python:
  - "2.7"
  - "3.4"
```

Depending on the language selected, a language-specific section (e.g. `jdk`, `php` or `python`) can then be used to specify which versions of the language the job is to be run under. Travis CI will run the job for each of these versions.Here, we request that Travis CI runs the job twice, once under Python 2.7 and once under Python 3.4:

```
before_install:
  - pip install pytest-cov
```

An optional `before_install` section lists the steps that need to be executed before we can build, run or test our code. For certain languages, we also need to download, build and install additional dependencies. Here, the Python [pytest-cov](https://pypi.python.org/pypi/pytest-cov) package is installed, using the Python `pip` package installer, so we can generate a code coverage report, a report on the lines of code executed by our tests.

```
script: 
  - py.test -v --cov=msc
```

Python needs a `script` entry to specify what to run e.g. how to run our tests and what tests to run. We use `py.test`, the test runner from Python's [pytest](https://docs.pytest.org/en/latest/) test framework. The `-v` and `--cov=msc` flags request `py.test` to print out information about the tests being run and a code coverage report for the code in the `msc` module.

Note that we don't need to install `py.test` as it is already provided by Travis CI.

Sign in to Travis CI
--------------------

Once you have an account on GitHub, you can use this to sign in to Travis CI.

Visit [Travis CI](https://travis-ci.com).

Click on Sign in with GitHub.

Enable your repository on Travis CI
-----------------------------------

Now, you need to tell Travis CI to check for changes in your repository, so click on your name on the top-right of the Travis CI page and select **Settings**.

This will take you to a page, https://travis-ci.com/account/repositories, which shows a list of your GitHub repositories that Travis CI knows about.

If you cannot see `USERNAME/git-gitlab-travis-lab`, then click the **Sync account** button which tells Travis CI to check your current repositories on GitHub.

When you can see `USERNAME/git-github-travis-lab`, then click on the button next to it to instruct Travis CI to monitor that repository for changes. The X icon should change to a check/tick icon.

Write a test
------------

In the directory `msc/tests`, create a test file called `test_USERNAME.py`.

Add the following imports, to import the functions in `msc/rot13.py`, into your test file:

```
from msc.rot13 import rot13
from msc.rot13 import rot13_char
```

Look at the `msc/rot13.py` source code and write a test for one of the two functions:

```
def rot13_char(ch):
def rot13(s):
```

For example, a test for `rot13_char(ch)` is:

```
def test_rot13_char_a():
    assert "n" == rot13_char("a"), "Unexpected character"
```

To run your tests, do:

```
$ py.test
```

When your test passes, add and commit it to your Git repository:

```
$ git add msc/tests/test_USERNAME.py
$ git commit -m "USERNAME's first test for ROT13" .
```

Push to trigger a new build
---------------------------

These changes are to our local repository only. Once we push them to GitHub, they will trigger the running of our Travis CI job. So, let's push these changes to our repository on GitHub, denoted by the `remote`, `origin`, into its default, `master`, branch:

```
$ git push origin master
```

Visit https://travis-ci.com/USERNAME/git-github-travis-lab.

You should shortly see a single job with two sub-jobs, one for each version of these languages we are testing under.

Jobs should be coloured green with a tick, indicating that they passed.

Click on one of the jobs.

You should see that your test ran and passed.

Submit a pull request
---------------------

Now, submit your code for inclusion in the instructor's repository, the original repository that you forked. GitHub calls this a "pull request" - a request that the repository's owner pull in your changes.

Visit https://github.com/USERNAME/git-github-travis-lab.

Click Pull Requests 

Click New Pull Request

Set base fork: `INSTRUCTOR/git-github-travis-lab`

Set head fork: `USERNAME/git-github-travis-lab`

Click Create pull request

Enter a title for your pull request, if one hasn't been entered already.

Click Create pull request

Look at the Travis CI
---------------------

The instructor will merge in your pull request. 

Once they have done so, you should see your tests being run as part of their Travis CI jobs at https://travis-ci.com/INSTRUCTOR/git-github-travis-lab.

Write another test
------------------

Add another test to `msc/tests/test_USERNAME.py`.

When it passes, commit your changes to this file.

Push your changes to GitHub.

Create a pull request.

Get updates from `INSTRUCTOR/git-github-travis-lab`
---------------------------------------------------

If you want to update your repository with the changes that have been made to `INSTRUCTOR/git-github-travis-lab` since you first forked it (i.e. tests commited and pushed by other students), you can pull these into your repository.

Add the original repository that you forked as a `remote`. This is a short-hand, or nick-name, of the location of that repository:

```
$ git remote add upstream https://github.com/INSTRUCTOR/git-github-travis-lab
```

Pull in the current version of the `master` branch of the repository represented by the `upstream` remote:

```
git pull upstream master
```

We now have the changes in our local repository, and can now push these into our repository on GitHub:

```
git pull origin master
```

Copyright and licence
---------------------

Copyright (c) 2015-2017 The University of Edinburgh.

Code is licensed under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html) licence. The licence text is also in [LICENSE.md](./LICENSE.md).

Documents are licensed under the Creative Commons [Attribution-NonCommercial 2.5 UK: Scotland (CC BY-NC 2.5 SCOTLAND)](http://creativecommons.org/licenses/by-nc/2.5/scotland/).

This directory includes code based on public domain software. Please see [msc/rot13.py](./msc/rot13.py).
