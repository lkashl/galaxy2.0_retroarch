# galaxy2.0_retroarch

## Contents

- [galaxy2.0_retroarch](#galaxy20retroarch)
  - [Contents](#contents)
  - [Description](#description)
  - [Currently supported functionality:](#currently-supported-functionality)
  - [Installation Instructions](#installation-instructions)
    - [Installing dependencies](#installing-dependencies)
    - [Configuration](#configuration)
  - [Known issues](#known-issues)


## Description

This repo contains a plugin that can generically load files from a file system into Galaxy 2.0 for launch later

Currently it integrates with Retroarch playlist files to integrate GOG 2.0 but it will be updated in the future to support any generic file manifests

![image](https://user-images.githubusercontent.com/13351116/67159839-b989c000-f395-11e9-8f9d-6e644822b1a9.png)

SNES is configured as the default platform as an example, however this can easily be changed. See [Configuration](#configuration) for more instructions

## Currently supported functionality:

| Platform  | Tested | Known Issues | Library | Achievements |
| ------------- | ------------- |-------------|------------- | -------------|
| SNES  | :white_check_mark: | :negative_squared_cross_mark: | :white_check_mark:  | :negative_squared_cross_mark: |
| SMS  | :white_check_mark: | :negative_squared_cross_mark: | :white_check_mark:  | :negative_squared_cross_mark: |

- User libraries

## Installation Instructions

### Installing dependencies

You need python 3.7 to install this plugin. A compiled version will be availabe shortly.

In the mean time, if you have python you can use pip to install dependencies within this directory using:

``` bash
pip install galaxy.plugin.api --target . --python-version 37 --only-binary=:all:
```

Afterwards copy this directory to:

macOS:

``` bash
~/Library/Application Support/GOG.com/Galaxy/plugins/installed
```

Windows:

``` bash
%localappdata%\GOG.com\Galaxy\plugins\installed
```

More instructions can be found in [GOG's developer documentation](https://galaxy-integrations-python-api.readthedocs.io/en/latest/overview.html)
### Configuration

Coming soon

## Known issues

- Plugin must be reconnected on GOG reboot
- ' characters are currently not supported causing data mappings to not work for certain games