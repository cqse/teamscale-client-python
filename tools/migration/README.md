# Migration tools
Collection of tools which can be used to migrate data between to teamscale instances.
Up to now there are three scripts you can use:
- blacklist_migrator.py
- task_migratior.py
- batch_migrator.py

The first two scripts are pretty self-explanatory.
Use `config.template` to create your own configuration and give the path to the config file as a parameter
when calling either migrator (task or blacklist).
If there is any kind of `path (suffix) transformation` on necessary adjust the optional parameter
`path_prefix_transformation` for the new instance. This feature is not very in depth, so if you are coming up to 
an extreme example where both projects have multiple transformation you might need to extend it.

## Batch Migration
Both scripts only work for one project at a time. If you want to migrate the blacklist and the tasks of
a bunch of projects you can use the batch migrator script.
For the configuration use `batch_config.template`.
NOTE: The scripts assumes, that all "from" projects are on the "old instance" and all "to" projects are on
the new one.

## Running the scripts
As of now, if you want to run the scripts, you musn't install the `teamscale-client` with `pip`, but add the
root directory of the `teamscale-client-python` to the `PYTHONPATH`.
```bash
export PYTHONPATH="$PYTHONPATH:/home/<user>/workspace/teamscale-client-python"
```
or for windows
```bash
set PYTHONPATH=%PYTHONPATH%;/home/<user>/workspace/teamscale-client-python
```
