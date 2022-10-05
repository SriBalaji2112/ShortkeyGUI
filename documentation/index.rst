
Welcome to ShortcutKeyGUI documentation!
=====================================

shortkeygui is an easy-to-use tool that can press a shortcut key. For Windows, macOS, and Linux, on Python 3 and 2.

To install with pip, run ``pip install shortkeygui``. See the :doc:`install` page for more details.

The source code is available on: https://github.com/SriBalajiSMVEC/shortkeygui/

shortkeygui has several features:

* Presses shortcut keys when you call a function name --> Like: ('copy', 'cut')
* It have all application shortcut key --> Like:('MS Excel', 'MS Word', 'MS Office', etc...,)
* shortkeygui will Press a Shortcut Keys Directly.

Here's `a YouTube video of a shortkeygui <https://www.youtube.com/watch?v=lfk_T6VKhTE>`_.

.. code:: python

    >>> from shortkeygui import mainShotcut as key
    
        >>> key.copy()  # It presses shortcut key for Copy ( ctrl+c )
        // It presses shortcut key for Copy ( ctrl + c )
    
        >>> key.cut()
        // It presses shortcut key for cut ( ctrl + x )
    
        >>> key.delete_permanently()
        // It presses shortcut key for delete permanently ( shift + delete )
    
        >>> key.delete()
        // It presses shortcut key for delete ( del )
    
        >>> key.end()
        // It presses shortcut key for Go to the end of the current line. ( end )
    
        >>> key.file_menu()
        // It presses shortcut key for File menu options in the current program. ( alt + f )
    
        // It has many more shortcut key like this...

    >>> key.copy()  # It presses shortcut key for Copy ( ctrl+c )
    // It presses shortcut key for Copy ( ctrl + c )

    >>> key.cut()
    // It presses shortcut key for cut ( ctrl + x )

    >>> key.delete_permanently()
    // It presses shortcut key for delete permanently ( shift + delete )

    >>> key.delete()
    // It presses shortcut key for delete ( del )

    >>> key.end()
    // It presses shortcut key for Go to the end of the current line. ( end )

    >>> key.file_menu()
    // It presses shortcut key for File menu options in the current program. ( alt + f )

    // It has many more shortcut key like this...


Requirement modul
=================

shortkeygui install the modules it depends on, including uiaction.

<-- thank you !!! -->
==========

.. _SriBalaji: https://github.com/SriBalajiSMVEC