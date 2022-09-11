.. _python_interactivo:

Inmersión al modo interactivo
-----------------------------

La *inmersión al modo interactivo* le permite a cualquier usuario el cual **NUNCA** 
ha trabajando con el interprete de `Python`_ pueda tener un primer acercamiento 
**SIN PROGRAMAR**, solamente con conocer el uso del interprete y sus comandos básicos 
usando la técnica de introspección.

.. _python_introspeccion:

Introspección en Python
.......................

En Python como usted lo ira entendiendo **todo en Python es un objeto**, y la 
técnica de introspección, no es más que código el cual examina como objetos 
otros módulos y funciones en memoria, obtiene información sobre ellos y los 
que los maneja.

De paso, usted podrá definir las funciones sin nombre, las llamará a
funciones con argumentos sin orden, y podrá hacer referencia a funciones
cuyos nombres desconocemos.


Python a través de su interprete
................................

Es importante conocer Python a través de su interprete debido a varios
factores:

- Conocer las clases, sus funciones y atributos propios, a través de la
  introspección del lenguaje.

- Disponibilidad de consultar la documentación del lenguaje desde el
  interprete, por mucho tiempo no estaba disponible documentación tipo 
  `Javadoc`_ o `diagramas de clases`_ del propio lenguaje por lo cual
  muchas programadores **Python** se acostumbraron a estudiar su código de
  esta forma, así que le recomiendo que use el interprete ``python`` para
  eso.

- Hoy en día existente herramientas que te permiten generar
  documentación desde los códigos fuentes Python como `Sphinx`_.

La forma mas fácil es iniciar tu relación con Python simplemente ejecutando
el comando ``python`` de la siguiente forma: 

.. code-block:: python

    python3
    Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
    [GCC 6.3.0 20170516] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


Puede solicitar la ayudar del interprete de Python, ejecutando:

.. code-block:: python

    >>> help
    Type help() for interactive help, or help(object) for help about object.
    >>> help()

    Welcome to Python 3.5's help utility!

    If this is your first time using Python, you should definitely check out
    the tutorial on the Internet at http://docs.python.org/3.5/tutorial/.

    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available modules, keywords, symbols, or topics, type
    "modules", "keywords", "symbols", or "topics".  Each module also comes
    with a one-line summary of what it does; to list the modules whose name
    or summary contain a given string such as "spam", type "modules spam".

    help> 


Para ejecutar la ayuda disponible sobre la sintaxis Python ejecute el
siguiente comando:

.. code-block:: python

    help> modules

    Please wait a moment while I gather a list of all available modules...

    CDROM               alabaster           idna                selectors
    DLFCN               antigravity         imagesize           setuptools
    IN                  argparse            imaplib             shelve
    TYPES               array               imghdr              shlex
    __future__          ast                 imp                 shutil
    _ast                asynchat            importlib           signal
    _bisect             asyncio             inspect             site
    _bootlocale         asyncore            io                  sitecustomize
    _bz2                atexit              ipaddress           six
    _codecs             audioop             itertools           smtpd
    _codecs_cn          babel               jinja2              smtplib
    _codecs_hk          base64              json                sndhdr
    _codecs_iso2022     bdb                 keyword             snowballstemmer
    _codecs_jp          binascii            lib2to3             socket
    _codecs_kr          binhex              linecache           socketserver
    _codecs_tw          bisect              locale              sphinx
    _collections        builtins            logging             spwd
    _collections_abc    bz2                 lzma                sqlite3
    _compat_pickle      cProfile            macpath             sre_compile
    _compression        calendar            macurl2path         sre_constants
    _crypt              certifi             mailbox             sre_parse
    _csv                cgi                 mailcap             ssl
    _ctypes             cgitb               markupsafe          stat
    _ctypes_test        chardet             marshal             statistics
    _curses             chunk               math                string
    _curses_panel       cmath               mimetypes           stringprep
    _datetime           cmd                 mmap                struct
    _dbm                code                modulefinder        subprocess
    _decimal            codecs              multiprocessing     sunau
    _dummy_thread       codeop              netrc               symbol
    _elementtree        collections         nis                 symtable
    _functools          colorsys            nntplib             sys
    _hashlib            compileall          ntpath              sysconfig
    _heapq              concurrent          nturl2path          syslog
    _imp                configparser        numbers             tabnanny
    _io                 contextlib          opcode              tarfile
    _json               copy                operator            telnetlib
    _locale             copyreg             optparse            tempfile
    _lsprof             crypt               os                  termios
    _lzma               csv                 ossaudiodev         test
    _markupbase         ctypes              packaging           textwrap
    _md5                curses              parser              this
    _multibytecodec     datetime            pathlib             threading
    _multiprocessing    dbm                 pdb                 time
    _opcode             decimal             pickle              timeit
    _operator           difflib             pickletools         tkinter
    _osx_support        dis                 pip                 token
    _pickle             distutils           pipes               tokenize
    _posixsubprocess    doctest             pkg_resources       trace
    _pydecimal          docutils            pkgutil             traceback
    _pyio               dummy_threading     platform            tracemalloc
    _random             easy_install        plistlib            tty
    _sha1               email               poplib              turtle
    _sha256             encodings           posix               types
    _sha512             enum                posixpath           typing
    _signal             errno               pprint              unicodedata
    _sitebuiltins       faulthandler        profile             unittest
    _socket             fcntl               pstats              urllib
    _sqlite3            filecmp             pty                 urllib3
    _sre                fileinput           pwd                 uu
    _ssl                fnmatch             py_compile          uuid
    _stat               formatter           pyclbr              venv
    _string             fpectl              pydoc               warnings
    _strptime           fractions           pydoc_data          wave
    _struct             ftplib              pyexpat             weakref
    _symtable           functools           pygments            webbrowser
    _sysconfigdata      gc                  pyparsing           wheel
    _sysconfigdata_m    genericpath         pytz                wsgiref
    _testbuffer         getopt              queue               xdrlib
    _testcapi           getpass             quopri              xml
    _testimportmultiple gettext             random              xmlrpc
    _testmultiphase     glob                re                  xxlimited
    _thread             grp                 readline            xxsubtype
    _threading_local    gzip                reprlib             zipapp
    _tracemalloc        hashlib             requests            zipfile
    _warnings           heapq               resource            zipimport
    _weakref            hmac                rlcompleter         zlib
    _weakrefset         html                runpy
    abc                 http                sched
    aifc                idlelib             select

    Enter any module name to get more help.  Or, type "modules spam" to search
    for modules whose name or summary contain the string "spam".


Entonces consulte la ayuda del módulo ``os``, ejecutando:

::

    help> os
    Help on module os:

    NAME
        os - OS routines for NT or Posix depending on what system we're on.

    MODULE REFERENCE
        https://docs.python.org/3.5/library/os

        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.

    DESCRIPTION
        This exports:
          - all functions from posix, nt or ce, e.g. unlink, stat, etc.
          - os.path is either posixpath or ntpath
          - os.name is either 'posix', 'nt' or 'ce'.
          - os.curdir is a string representing the current directory ('.' or ':')
          - os.pardir is a string representing the parent directory ('..' or '::')
          - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
          - os.extsep is the extension separator (always '.')
          - os.altsep is the alternate pathname separator (None or '/')
          - os.pathsep is the component separator used in $PATH etc
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
          - os.defpath is the default search path for executables
          - os.devnull is the file path of the null device ('/dev/null', etc.)
        
        Programs that import and use 'os' stand a better chance of being
        portable between different platforms.  Of course, they must then
        only use functions that are defined by all platforms (e.g., unlink
        and opendir), and leave all pathname manipulation to os.path
        (e.g., split and join).
    :

.. tip:: Presione la tecla ``q`` para salir de la ayuda del módulo ``os``.

Seguidamente presione la combinación de tecla **Crtl+d** para salir de la ayuda.

Luego realice la importación de la `librería del estándar`_ Python llamada
``os``, con el siguiente comando:

.. code-block:: python

    >>> import os
    >>>


Previamente importada la librería usted puede usar la función ``dir()`` para
listar o descubrir que atributos, métodos de la clase están disponibles con
la importación

.. code-block:: python

    >>> dir(os)
    ['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'EX_CANTCREAT', 
    'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 
    'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 
    'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 
    'F_TLOCK', 'F_ULOCK', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 
    'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 
    'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 
    'O_NONBLOCK', 'O_PATH', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC', 'O_TMPFILE', 
    'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE', 
    'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL', 
    'POSIX_FADV_WILLNEED', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 
    'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'RTLD_DEEPBIND', 
    'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 
    'RTLD_NOW', 'R_OK', 'SCHED_BATCH', 'SCHED_FIFO', 'SCHED_IDLE', 'SCHED_OTHER', 
    'SCHED_RESET_ON_FORK', 'SCHED_RR', 'SEEK_CUR', 'SEEK_DATA', 'SEEK_END', 
    'SEEK_HOLE', 'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 
    'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME', 
    'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 
    'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 
    'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 
    'XATTR_CREATE', 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK', '_DummyDirEntry', 
    '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
    '__loader__', '__name__', '__package__', '__spec__', '_dummy_scandir', 
    '_execvpe', '_exists', '_exit', '_fwalk', '_get_exports_list', '_putenv', 
    '_spawnvef', '_unsetenv', '_wrap_close', 'abort', 'access', 'altsep', 'chdir', 
    'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 
    'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 
    'dup', 'dup2', 'environ', 'environb', 'errno', 'error', 'execl', 'execle', 
    'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 
    'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork', 'forkpty', 'fpathconf', 
    'fsdecode', 'fsencode', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk', 
    'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 
    'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 
    'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 
    'getpriority', 'getresgid', 'getresuid', 'getsid', 'getuid', 'getxattr', 
    'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 'linesep', 'link', 'listdir', 
    'listxattr', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 
    'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 
    'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'pipe2', 'popen', 'posix_fadvise', 
    'posix_fallocate', 'pread', 'putenv', 'pwrite', 'read', 'readlink', 'readv', 
    'remove', 'removedirs', 'removexattr', 'rename', 'renames', 'replace', 'rmdir', 
    'scandir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_getaffinity', 
    'sched_getparam', 'sched_getscheduler', 'sched_param', 'sched_rr_get_interval', 
    'sched_setaffinity', 'sched_setparam', 'sched_setscheduler', 'sched_yield', 
    'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 
    'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setresgid', 
    'setresuid', 'setreuid', 'setsid', 'setuid', 'setxattr', 'spawnl', 'spawnle', 
    'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 
    'stat_float_times', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 
    'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 
    'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 
    'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 
    'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 
    'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitid', 'waitid_result', 'waitpid', 
    'walk', 'write', 'writev']
    >>>


Otro ejemplo de uso, es poder usar el método ``file`` para determinar la
ubicación de la librería importada de la siguiente forma:

.. code-block:: python

    >>> os.__file__
    '/usr/lib/python3.5/os.py'
    >>>

También puede consultar la documentación de la librería ``os`` ejecutando el
siguiente comando:

.. code-block:: python

    >>> print(os.__doc__)
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix, nt or ce, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix', 'nt' or 'ce'.
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).

    >>> 

Ejecute el comando exit() para salir del interprete...

.. code-block:: python

    >>> exit()


.. _python_interprete_interactivo:

Interprete ipython
..................

Para mejorar la experiencia con el interprete Python le sugerimos instalar el
paquete ``ipython``, según su documentación:

Según Wikipedia

  "``ipython`` es un shell interactivo que añade funcionalidades extra al `modo
  interactivo`_ incluido con Python, como resaltado de líneas y errores
  mediante colores, una sintaxis adicional para el shell, completado automático
  mediante tabulador de variables, módulos y atributos; entre otras
  funcionalidades. Es un componente del paquete `SciPy`_."

Para mayor información visite su página principal de `ipython`_ y si necesita instalar
este programa ejecute el siguiente comando:

.. code-block:: sh

    $ sudo apt-get install ipython3


Sustituya el comando ``python3`` por ``ipython3`` de la siguiente forma:

.. code-block:: sh

    $ ipython3 
    Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
    Type "copyright", "credits" or "license" for more information.

    IPython 5.1.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: 

Un ejemplo de uso del comando ``help`` es consultar la ayuda del comando
``dir`` y se ejecuta de la siguiente forma:

.. code-block:: python

    In [1]: help(dir)
    Help on built-in function dir in module builtins:

    dir(...)
        dir([object]) -> list of strings
        
        If called without an argument, return the names in the current scope.
        Else, return an alphabetized list of names comprising (some of) the attributes
        of the given object, and of attributes reachable from it.
        If the object supplies a method named __dir__, it will be used; otherwise
        the default dir() logic is used and returns:
        for a module object: the module's attributes.
        for a class object:  its attributes, and recursively the attributes
        of its bases.
        for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.


Entonces presione la tecla **q** para salir de la ayuda de la función ``dir()``.

De nuevo realice la importación de la librería del estándar Python llamada
``os``.

.. code-block:: python

    In [2]: import os


También consultar los detalles acerca del 'objeto' para esto use como ejemplo
la librería ``os`` ejecutando el siguiente comando:

.. code-block:: ipython

    In [3]: os?
    Type:        module
    String form: <module 'os' from '/usr/lib/python3.5/os.py'>
    File:        /usr/lib/python3.5/os.py
    Docstring:  
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix, nt or ce, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix', 'nt' or 'ce'.
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).


Escriba la librería *os.* y luego escribe dos **underscore** y presione *dos
veces la tecla tabular* para usar la completado automático del interprete al 
`estilo de completación de lineas de comandos`_ en el shell UNIX/Linux para
ayudar a la introspección del lenguaje y sus librerías.

.. code-block:: python

    In [4]: os.__
    os.__all__      os.__doc__      os.__name__
    os.__builtins__ os.__file__     os.__package__                                           
    os.__cached__   os.__loader__   os.__spec__

De nuevo ejecute el método ``file`` para determinar la ubicación de la
librería importada

.. code-block:: python

    In [5]: os.__file__
    Out[5]: '/usr/lib/python3.5/os.py'



También puede consultar la documentación de la librería ``os`` de la
siguiente forma:

.. code-block:: ipython

    In [5]: print(os.__doc__)
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix, nt or ce, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix', 'nt' or 'ce'.
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).


Otro ejemplo es imprimir el **nombre de la clase** con el siguiente comando:

.. code-block:: python

    In [7]: os.__name__
    Out[7]: 'os'

Y otra forma de consultar la documentación de la librería ``os`` es
ejecutando el siguiente comando:

.. code-block:: ipython

    In [8]: help(os)
    Help on module os:

    NAME
        os - OS routines for NT or Posix depending on what system we're on.

    MODULE REFERENCE
        https://docs.python.org/3.5/library/os
        
        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.

    DESCRIPTION
        This exports:
          - all functions from posix, nt or ce, e.g. unlink, stat, etc.
          - os.path is either posixpath or ntpath
          - os.name is either 'posix', 'nt' or 'ce'.
          - os.curdir is a string representing the current directory ('.' or ':')
          - os.pardir is a string representing the parent directory ('..' or '::')
          - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
          - os.extsep is the extension separator (always '.')
          - os.altsep is the alternate pathname separator (None or '/')
          - os.pathsep is the component separator used in $PATH etc
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
          - os.defpath is the default search path for executables
          - os.devnull is the file path of the null device ('/dev/null', etc.)

        Programs that import and use 'os' stand a better chance of being
        portable between different platforms.  Of course, they must then
        only use functions that are defined by all platforms (e.g., unlink
        and opendir), and leave all pathname manipulation to os.path
        (e.g., split and join).
    :

Entonces presione la tecla ``q`` para salir de la ayuda del módulo ``os``.

Y para cerrar la sesión con el ``ipython`` ejecute el siguiente comando:

.. code-block:: ipython

    In [8]: exit()
    Do you really want to exit ([y]/n)? y


Interprete bpython
..................

Alternativamente puedes usar el paquete `bpython` que mejora aun mas la experiencia 
de trabajo con el paquete `ipython`.

Para mayor información visite su página principal de `interprete bpython`_ y si necesita instalar
este programa ejecute el siguiente comando:

.. code-block:: sh

    sudo pip3 install bpython

Luego cierra sesión de **root** y vuelve al usuario y sustituya el comando
``python`` por ``ipython`` de la siguiente forma:

.. code-block:: sh

    bpython


Dentro de interprete Python puede apreciar que ofrece otra forma de presentar 
la documentación y la estructura del lenguaje, con los siguientes comandos de ejemplos:

.. code-block:: python

    >>> print 'Hola Mundo'
    Hola Mundo
    >>> for item in xrange(
    +───────────────────────────────────────────────────────────────────────+
    │ xrange: ([start, ] stop[, step])                                      │
    │ xrange([start,] stop[, step]) -> xrange object                        │
    │                                                                       │
    │ Like range(), but instead of returning a list, returns an object that │
    │ generates the numbers in the range on demand.  For looping, this is   │
    │ slightly faster than range() and more memory efficient.               │
    +───────────────────────────────────────────────────────────────────────+

     <C-r> Rewind  <C-s> Save  <F8> Pastebin  <F9> Pager  <F2> Show Source


Conclusiones
............

Como puede apreciar este tutorial no le enseña a programar sino a simplemente
aprender a conocer como manejarse en shell de Python y en el modo interactivo 
usando el paquete ``ipython`` y otros adicionales como ``bpython``, con el fin 
de conocer a través de la introspección del lenguaje, las librerías estándar y 
módulos propios escritos en Python que tienes instalado en tu sistema.


----

.. seealso::

    Consulte la sección de :ref:`lecturas suplementarias <lecturas_extras_leccion1>` 
    del entrenamiento para ampliar su conocimiento en esta temática.


.. _`Python`: https://www.python.org/ 
.. _`Javadoc`: https://es.wikipedia.org/wiki/Javadoc
.. _`diagramas de clases`: https://es.wikipedia.org/wiki/Diagrama_de_clases
.. _`Sphinx`: https://en.wikipedia.org/wiki/Sphinx_%28documentation_generator%29
.. _`librería del estándar`: https://docs.python.org/2/library/index.html
.. _`modo interactivo`: https://es.wikipedia.org/wiki/Python#Modo_interactivo
.. _`SciPy`: https://en.wikipedia.org/wiki/SciPy
.. _`ipython`: https://ipython.readthedocs.io/
.. _`bpython`: https://pypi.org/project/bpython/
.. _`interprete bpython`: https://bpython-interpreter.org/
.. _`estilo de completación de lineas de comandos`: https://en.wikipedia.org/wiki/Command_line_completion
