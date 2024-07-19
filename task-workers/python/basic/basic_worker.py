import asyncio
import logging
from time import sleep

import littlehorse
from littlehorse.config import LHConfig
from littlehorse.worker import WorkerContext, LHTaskWorker

logging.basicConfig(level=logging.INFO)


# This is a Task Function! Whenever your WfSpec says "execute the 'greet'
# Task", this function is called with appropriate inputs.
async def greeting(name: str, ctx: WorkerContext) -> str:
    msg = f"Hello {name}!. WfRun {ctx.wf_run_id}"
    print(msg, flush=True)
    return msg


async def main() -> None:
    logging.info("Starting Task Worker!")
    
    # Configuration loaded from environment variables
    config = LHConfig()

    # register the TaskDef
    littlehorse.create_task_def(greeting, "greet", config)

    # Wait a small amount of time for the metadata to propagate in the LH Server
    sleep(0.5)

    # Start the Task Worker
    await littlehorse.start(LHTaskWorker(greeting, "greet", config))


if __name__ == '__main__':
    asyncio.run(main())
