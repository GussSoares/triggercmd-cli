# TriggerCMD CLI client

[![Build Status](https://app.travis-ci.com/GussSoares/triggercmd-cli.svg?branch=main)](https://app.travis-ci.com/GussSoares/triggercmd-cli)
[![CodeQL](https://github.com/GussSoares/triggercmd-cli/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/GussSoares/triggercmd-cli/actions/workflows/codeql-analysis.yml)
[![Publish package](https://github.com/GussSoares/triggercmd-cli/actions/workflows/publish-package-on-release.yaml/badge.svg)](https://github.com/GussSoares/triggercmd-cli/actions/workflows/publish-package-on-release.yaml)
![GitHub](https://img.shields.io/github/license/GussSoares/triggercmd-cli.svg)
[![PyPI](https://img.shields.io/pypi/v/triggercmd.svg)](http://pypi.org/project/triggercmd/)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/w/GussSoares/triggercmd-cli.svg)](https://github.com/GussSoares/triggercmd/pulse)
[![GitHub last commit](https://img.shields.io/github/last-commit/GussSoares/triggercmd-cli.svg)](https://github.com/GussSoares/triggercmd-cli/commit/main)
[![Downloads](https://pepy.tech/badge/triggercmd)](https://pepy.tech/project/triggercmd)

<!-- <img src='triggerCMD_CLI_logo.png' style='display: block; margin-left: auto; margin-right: auto; width: 100%;'>
<br> -->
<p align="center">
    <img src="assets/trigger.gif" width="600" alt="TRIGGERcmd CLI">
</p>

`triggercmd` is a CLI client for the [TRIGGERcmd][1] cloud service.

## dependencies
you need install `gobject-introspection` if you use Arch Linux.

## installation
the `triggercmd` package is available in [PyPI](https://pypi.org/project/triggercmd/). to install, simply type the following command:
```
pip install triggercmd
```
Or using the [pipx](https://github.com/pypa/pipx) for a safer installation.

After install, you can use the triggercmd CLI client to manipulate commands on the TRIGGERcmd agent.

## commands

You can read the [CLI.md](https://github.com/GussSoares/triggercmd-cli/blob/main/CLI.md) file for more information about the list of commands.


## contributing and support

this project is open for contributions. here are some of the ways for you to contribute:
 - bug reports/fix
 - features requests
 - use-case demonstrations

please open an [issue](https://github.com/GussSoares/triggercmd-cli/issues) with enough information for us to reproduce your problem. A [minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) would be very helpful.

to make a contribution, just fork this repository, push the changes in your fork, open up an issue, and make a pull request!


---
\* My contribuction its only the CLI client. All credit by develop [triggerCMD][1] agent is to [Russell VanderMey](https://github.com/rvmey/).


[1]: https://www.triggercmd.com/
