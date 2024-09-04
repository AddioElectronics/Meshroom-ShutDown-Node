__version__ = "1.0"

from meshroom.core import desc
# from meshroom.core.utils import VERBOSE_LEVEL # Causing crash?

import os
import platform

VERBOSE_LEVEL = ['error', 'info', 'debug']

class ShutDown(desc.Node):
    nodeName = 'ShutDown'
    category = 'Utils'
    documentation = '''
    This node shuts down the PC after a specified number of seconds. 
    '''
    inputs = [
        desc.File(
            name='triggerFile',
            label='Trigger (File)',
            description='File that will trigger the shutdown when received. (Value is ignored)',
            value='',
            advanced=True,
            group='trigger',
            uid=[0]
        ),
        desc.StringParam(
            name='triggerString',
            label='Trigger (String)',
            description='String that will trigger the shutdown when received. (Value is ignored)',
            value='',
            advanced=True,
            group='trigger',
            uid=[1]
        ),
        desc.BoolParam(
            name='triggerBool',
            label='Trigger (Bool)',
            description='Bool that will trigger the shutdown when received. (Value is ignored)',
            value=False, 
            advanced=True,
            group='trigger',
            uid=[2]
        ),
        desc.IntParam(
            name='triggerInt',
            label='Trigger (Int)',
            description='Int that will trigger the shutdown when received. (Value is ignored)',
            value=0,
            range=(0, 0, 1),
            advanced=True,
            group='trigger',
            uid=[3]
        ),
        desc.BoolParam(
            name='isEnabled',
            label='Shutdown Enabled',
            description='Set to True to enable shutdown.',
            value=True,
            uid=[4]
        ),
        desc.IntParam(
            name='delay',
            label='Delay (seconds)',
            description='Time in seconds before the shutdown.',
            value=3, 
            range=(0, 3600, 1), 
            uid=[5]
            ),
        desc.ChoiceParam(
            name="verboseLevel",
            label="Verbose Level",
            description="Verbosity level (fatal, error, warning, info, debug, trace).",
            values=VERBOSE_LEVEL,
            value="info",
            exclusive=True,
            uid=[6]
        ),
    ]
    outputs = []

    def processChunk(self, chunk):
    
        try:
            chunk.logManager.start(chunk.node.verboseLevel.value)
            
            delay = chunk.node.delay.value
            isEnabled = chunk.node.isEnabled.value
            system = platform.system()
            
            chunk.logger.debug(f"Detected system: {system}")
            chunk.logger.debug(f"Delay: {delay}")
            chunk.logger.debug(f"Is Enabled: {isEnabled}")
            
            if isEnabled:           
                chunk.logger.info(f"Scheduling shutdown in {delay} seconds...")            
                if system == 'Windows':
                    #chunk.logger.debug(f"Command: shutdown /s /t {delay}")
                    os.system(f'shutdown /s /t {delay}')
                elif system == 'Linux':
                    #chunk.logger.debug(f"Command: shutdown -h +{delay//60}")
                    os.system(f'shutdown -h +{delay//60}')  # Delay in minutes on Linux
                elif system == 'Darwin':  # macOS
                    #chunk.logger.debug(f"Command: shutdown -h +{delay // 60}")
                    os.system(f'shutdown -h +{delay // 60}')  # Delay in minutes on macOS
                else:
                    raise NotImplementedError(f"Shutdown is not implemented for this OS: {system}")
            else:
                chunk.logger.info("Shutdown was not enabled.")

        except Exception as e:
            chunk.logger.error(e)
            raise RuntimeError()
        finally:
            # required to unlock log file so that it can be deleted if required
            chunk.logManager.end()

