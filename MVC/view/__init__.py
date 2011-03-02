if __package__ is None:
    import sys
    sys.path.insert(1, "../../")
    sys.path.insert(1, "../")
    import MVC
    __package__ = "MVC.view"

__all__ = ['qt']

import qt