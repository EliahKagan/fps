# fps - Failed Password Stats

This is a small Python script that examines a log file, such as `auth.log`, and
reports approximate frequencies of password failures for each username
attempted.

**NOTE:** This is not very robust, it's just a tool to help in an otherwise
interactive examination of logs.

Also, if a line reports that an event happened some number of times other than
1, this tool does not distinguish that from it happening 1 time. This really is
just doing a textual search and frequency count that one might otherwise do
with a hand-rolled `awk` one-liner.

**This software is licensed under [0BSD](https://opensource.org/licenses/0BSD)**,
which is a
[&ldquo;public-domain equivalent&rdquo;](https://en.wikipedia.org/wiki/Public-domain-equivalent_license)
license.
