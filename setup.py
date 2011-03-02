from distutils.core import setup
import py2exe

setup(
    name = 'name',
    description = 'description',
    version = '1.0',

    data_files = [('.', ['./DLL/msvcp90.dll', './DLL/msvcr90.dll', './DLL/msvcm90.dll', '../database/databaze.db3',
    #'c:/windows/system32/user32.dll', 'c:/windows/system32/imm32.dll', 'c:/windows/system32/shell32.dll', 
    #'c:/windows/system32/ole32.dll', 'c:/windows/system32/winmm.dll', 'c:/windows/system32/wsock32.dll',
    #'c:/windows/system32/comdlg32.dll', 'c:/windows/system32/advapi32.dll', 'c:/windows/system32/ws2_32.dll', 
    #'c:/windows/system32/winspool.drv', 'c:/windows/system32/gdi32.dll', 'c:/windows/system32/kernel32.dll',
    ])],

    windows = [
                  {
                      'script': 'program.py',
                  }
              ],

    options = {
                  'py2exe': {
                      'includes': 'PyQt4, sip'
                            }
              }
)
