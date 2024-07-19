# LittleHorse Templates

This is a repository of useful, self-contained examples that you can use to kick-start development of your LittleHorse applications. Made with love by the LittleHorse Knights.

## Running the Templates

All of these examples are runnable. Some of them require that you run multiple templates together in order to create a cohesive application; however, each example 

### Install LittleHorse

These are LittleHorse examples, so to run a LittleHorse Server you can use the following command:

```
docker run --name littlehorse -d -p 2023:2023 -p 8080:8080 ghcr.io/littlehorse-enterprises/littlehorse/lh-standalone:0.10.1
```

You can install `lhctl` as follows:

```
brew install littlehorse-enterprises/lh/lhctl
```

Alternatively, you can download `lhctl` from the [Releases](https://github.com/littlehorse-enterprises/littlehorse/releases) page on our GitHub.

## Contents

Over time, we will develop 

### Task Workers

The [`task-workers`](./task-workers/) directory contains implementations of Task Workers in Python, Go, and Java.

### `WfSpec`s

Coming soon.

## Index by Concepts

Coming soon.
