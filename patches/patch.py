# CEF Python patches to Chromium and CEF.
# See upstream cef/patch/patch.cfg for how patching works in CEF.
# Current working directory is cef_build_dir/chromium/cef/ .
# See also docs/Build-instructions.md and tools/automate.py .

import platform

OS_POSTFIX = ("win" if platform.system() == "Windows" else
              "linux" if platform.system() == "Linux" else
              "mac" if platform.system() == "Darwin" else "unknown")

# ALL PLATFORMS
patches.append(
    {
        # Fixes HTTPS cache problems with private certificates
        'name': 'issue125',
        'path': '../net/http/',
    },
)

# LINUX
if OS_POSTFIX == "linux":
    patches.append(
        {
            # Fix compile error on Ubuntu 12:
            #   cc1plus: error: unrecognized command line option '-std=gnu++11'
            'name': 'CMakeLists.txt.in_linux',
            'path': './',
        },
    )
