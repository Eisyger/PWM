import subprocess
import platform


def copy_to_clipboard(text) -> None:
    """
    Copy text to the clipboard.

    Args:
        text (str): The text to be copied.
    """

    system = platform.system()
    if system == 'Linux':
        subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode('utf-8'), check=True)
    elif system == 'Darwin':  # macOS
        subprocess.run(['pbcopy'], input=text.encode('utf-8'), check=True)
    elif system == 'Windows':
        subprocess.run(['clip'], input=text.encode('utf-16'), check=True)
    else:
        raise NotImplementedError(f'Unsupported platform: {system}')
