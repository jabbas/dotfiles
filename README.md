# dotfiles

dotfiles is simple wrapper over git to manage your home directory

## Installation

Just:

    pip install

## Configuration

Default configuration is held in `~/.config/dotfiles.ini` and it's generated automatically with first use

GIT_DIR (the git repository) is held in `~/.dotfiles`

## Usage

You need to explicitly add each file/directory with `dtf add` to get it tracked by dotfiles, but except of that usage of `dtf` is exactly the same as `git` command.
Shortly: `dtf` does not treat all files within `~` as untracked.

## TODO
- automatic branch creation for each machine

