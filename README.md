# Meshroom ShutDown Node

A custom node for Meshroom used to shut down your PC after a specified delay.

## Installation

### Option 1: Directly to Meshroom Nodes Directory

1. You can either:
   - Copy/clone the entire repository to `lib/meshroom/nodes`, ensuring that the `__init__.py` and `ShutDown.py` files are inside a subdirectory.
   - Or create a new subdirectory within `lib/meshroom/nodes` and place the `__init__.py` and `ShutDown.py` files there.

### Option 2: Custom Nodes Directory

1. You can either:
   - Copy/clone the entire repository to a directory of your choice, making sure the `__init__.py` and `ShutDown.py` files are within a subdirectory.
   - Or create a new subdirectory and copy `__init__.py` and `ShutDown.py` files into it.
2. Set the `MESHROOM_NODES_PATH` environment variable to the parent directory of the subdirectory you created.

_The `.py` files need to be placed inside a subdirectory in either the `lib/meshroom/nodes` directory or your custom `MESHROOM_NODES_PATH` directory._

## Usage
1. Start Meshroom.
2. Add the `ShutDown` node to the graph editor.
3. Connect your final node to any of the `Trigger` inputs on the `ShutDown` node.
4. Optionally configure the node’s attributes, or connect to their inputs:
   - **Delay:** _Time in seconds before the PC shuts down._ **Default:** `30 seconds`
   - **Shutdown Enabled:** _Determines whether to initiate the shutdown._ **Default:** `Enabled`
   - **Verbose Level:** _Sets the logging level._ **Default:** `info`

_**Note:** The node will activate when connected to **ANY** input. Trigger inputs ignore the values they receive._

## Useful Links

- [Meshroom GitHub Repository](https://github.com/alicevision/Meshroom)
- [Meshroom Nodes API Documentation](https://meshroom-manual.readthedocs.io/en/latest/feature-documentation/core/nodes.html#api)
