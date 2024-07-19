# Basic Task Worker

This template contains a minimal example of a Task Worker in Python. You can copy this template and edit the `greet()` function to do whatever you want.

## Running the Worker

This section assumes that you've gotten access to an LH Server according to the [root README](../../../README.md). If you need to set any client configurations to access LittleHorse (you do NOT need to do this if using the local docker image), then you should set those configurations as environment variables.

### Setting up Python

To run this task worker, you only need one dependency: `littlehorse-client`. You can install it in two ways:


First, using `pip`:
```
pip install littlehorse-client
```

Alternatively, you can use `poetry`:

```
poetry install
poetry shell
```

Once you have set up Python properly, you should be able to import `littlehorse` in a python shell:

```
-> python
Python 3.12.4 (main, Jun  6 2024, 18:26:44) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import littlehorse
>>> 
```

### Running the Code

Running the code is simple! Just type:

```
python basic_worker.py
```

This will do two things:

1. Register the `greet` `TaskDef` in the LH Cluster.
2. Start a process which polls the LH Server asking to be notified of when to execute the `greet` tas.

Open the LittleHorse dashboard (if using the local docker image, it is at [`http://localhost:8080/](http://localhost:8080/)), click the `TaskDef`s tab, and click on `greet` and you'll see your `TaskDef`!

## Next Steps

Now that you've gotten your first `TaskDef` registered, it's time to take a look at using it in some workflows!
