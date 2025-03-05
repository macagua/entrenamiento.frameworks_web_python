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

La forma más fácil es iniciar tu relación con Python simplemente ejecutando
el comando ``python`` de la siguiente forma:

.. code-block:: console

    python3

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Python 3.11.2 (main, Nov 30 2024, 21:22:50) [GCC 12.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


Puede solicitar la ayuda del interprete de Python, ejecutando:

.. code-block:: pycon

    >>> help

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    >>> help
    Type help() for interactive help, or help(object) for help about object.
    >>>

Puede entrar en la ayuda interactiva de Python, ejecutando:

.. code-block:: pycon

    >>> help()

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Welcome to Python 3.11's help utility!

    If this is your first time using Python, you should definitely check out
    the tutorial on the internet at https://docs.python.org/3.11/tutorial/.

    Enter the name of any module, keyword, or topic to get help on writing
    Python programs and using Python modules.  To quit this help utility and
    return to the interpreter, just type "quit".

    To get a list of available modules, keywords, symbols, or topics, type
    "modules", "keywords", "symbols", or "topics".  Each module also comes
    with a one-line summary of what it does; to list the modules whose name
    or summary contain a given string such as "spam", type "modules spam".

    help>

Para ejecutar la ayuda disponible sobre la sintaxis de los diversos Python
ejecute el siguiente comando:

.. code-block:: pycon

    help> modules

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Please wait a moment while I gather a list of all available modules...

    IPython             _xxtestfuzz         imagesize           selectors
    __future__          _yaml               imaplib             setuptools
    __hello__           _zoneinfo           imghdr              shelve
    __phello__          abc                 imp                 shlex
    _abc                aifc                importlib           shutil
    _aix_support        alabaster           importlib_metadata  signal
    _ast                antigravity         inflect             site
    _asyncio            appdirs             inspect             sitecustomize
    _bisect             argparse            io                  smtpd
    _blake2             array               ipaddress           smtplib
    _bootsubprocess     ast                 itertools           sndhdr
    _bz2                asttokens           jedi                snowballstemmer
    _codecs             asynchat            jinja2              socket
    _codecs_cn          asyncio             json                socketserver
    _codecs_hk          asyncore            keyword             sphinx
    _codecs_iso2022     atexit              lib2to3             sphinx_contributors
    _codecs_jp          audioop             linecache           sphinx_disqus
    _codecs_kr          autocommand         locale              sphinx_immaterial
    _codecs_tw          babel               logging             sphinx_tabs
    _collections        backcall            lxml                sphinxlint
    _collections_abc    backports           lzma                spwd
    _compat_pickle      base64              mailbox             sqlite3
    _compression        bdb                 mailcap             sre_compile
    _contextvars        binascii            markdown            sre_constants
    _crypt              bisect              markupsafe          sre_parse
    _csv                builtins            marshal             ssl
    _ctypes             bz2                 math                stack_data
    _ctypes_test        cProfile            matplotlib_inline   stat
    _curses             calendar            mimetypes           statistics
    _curses_panel       certifi             mmap                string
    _datetime           cfgv                modulefinder        stringprep
    _dbm                cgi                 more_itertools      struct
    _decimal            cgitb               multiprocessing     subprocess
    _distutils_hack     charset_normalizer  netrc               sunau
    _distutils_system_mod chunk               nis                 symtable
    _elementtree        cmath               nntplib             sys
    _functools          cmd                 nodeenv             sysconfig
    _gdbm               code                ntpath              syslog
    _hashlib            codecs              nturl2path          tabnanny
    _heapq              codeop              numbers             tarfile
    _imp                collections         opcode              telnetlib
    _io                 colorsys            operator            tempfile
    _json               compileall          optparse            termios
    _locale             concurrent          os                  test
    _lsprof             configparser        ossaudiodev         textwrap
    _lzma               contextlib          packaging           this
    _markupbase         contextvars         parso               threading
    _md5                copy                pathlib             time
    _multibytecodec     copyreg             pdb                 timeit
    _multiprocessing    crypt               pexpect             tkinter
    _opcode             cssselect           pickle              token
    _operator           csv                 pickleshare         tokenize
    _osx_support        ctypes              pickletools         tokenize_rt
    _pickle             curses              pip                 toml
    _posixshmem         dataclasses         pipes               tomli
    _posixsubprocess    datetime            pkg_resources       tomllib
    _py_abc             dbm                 pkgutil             trace
    _pydecimal          decimal             platform            traceback
    _pyio               decorator           platformdirs        tracemalloc
    _queue              difflib             plistlib            traitlets
    _random             dis                 poplib              tty
    _sha1               distlib             posix               turtle
    _sha256             distutils           posixpath           turtledemo
    _sha3               doctest             pprint              typeguard
    _sha512             docutils            pre_commit          types
    _signal             email               profile             typing
    _sitebuiltins       encodings           prompt_toolkit      typing_extensions
    _socket             ensurepip           pstats              unicodedata
    _sqlite3            enum                pty                 unittest
    _sre                errno               ptyprocess          urllib
    _ssl                executing           pure_eval           urllib3
    _stat               faulthandler        pwd                 uu
    _statistics         fcntl               py_compile          uuid
    _string             filecmp             pyclbr              venv
    _strptime           fileinput           pydantic            virtualenv
    _struct             filelock            pydoc               warnings
    _symtable           fnmatch             pydoc_data          wave
    _sysconfigdata__linux_x86_64-linux-gnu fractions           pyexpat             wcwidth
    _sysconfigdata__x86_64-linux-gnu ftplib              pygments            weakref
    _testbuffer         functools           pymdownx            webbrowser
    _testcapi           gc                  pyparsing           wheel
    _testclinic         genericpath         pyquery             wsgiref
    _testimportmultiple getopt              pytz                xdrlib
    _testinternalcapi   getpass             pyupgrade           xml
    _testmultiphase     gettext             queue               xmlrpc
    _thread             glob                quopri              xxlimited
    _threading_local    graphlib            random              xxlimited_35
    _tkinter            grp                 re                  xxsubtype
    _tokenize           gzip                readline            yaml
    _tracemalloc        hashlib             reprlib             yasfb
    _typing             heapq               requests            zipapp
    _uuid               hmac                resource            zipfile
    _virtualenv         html                rlcompleter         zipimport
    _warnings           http                runpy               zipp
    _weakref            identify            sched               zlib
    _weakrefset         idlelib             secrets             zoneinfo
    _xxsubinterpreters  idna                select

    Enter any module name to get more help.  Or, type "modules spam" to search
    for modules whose name or summary contain the string "spam".

Entonces consulte la ayuda del módulo ``os``, ejecutando:

.. code-block:: pycon

    help> os

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Help on module os:

    NAME
        os - OS routines for NT or Posix depending on what system we're on.

    MODULE REFERENCE
        https://docs.python.org/3.11/library/os.html

        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.

    DESCRIPTION
        This exports:
          - all functions from posix or nt, e.g. unlink, stat, etc.
          - os.path is either posixpath or ntpath
          - os.name is either 'posix' or 'nt'
          - os.curdir is a string representing the current directory (always '.')
          - os.pardir is a string representing the parent directory (always '..')
          - os.sep is the (or a most common) pathname separator ('/' or '\\')
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

.. tip:: Presione la tecla :keys:`q` para salir de la ayuda del módulo ``os``.

Seguidamente presione la combinación de tecla :keys:`Crtl+d` para salir de la ayuda.

Luego realice la importación de la `librería del estándar`_ Python llamada
``os``, con el siguiente comando:

.. code-block:: pycon

    >>> import os
    >>>


Previamente importada la librería usted puede usar la función ``dir()`` para
listar o descubrir que atributos, métodos de la clase están disponibles con
la importación:

.. code-block:: pycon

    >>> dir(os)

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    ['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_KILLED', 'CLD_STOPPED',
    'CLD_TRAPPED', 'DirEntry', 'EFD_CLOEXEC', 'EFD_NONBLOCK', 'EFD_SEMAPHORE',
    'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT',
    'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL',
    'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK',
    'F_TEST', 'F_TLOCK', 'F_ULOCK', 'GRND_NONBLOCK', 'GRND_RANDOM', 'GenericAlias',
    'MFD_ALLOW_SEALING', 'MFD_CLOEXEC', 'MFD_HUGETLB', 'MFD_HUGE_16GB', 'MFD_HUGE_16MB',
    'MFD_HUGE_1GB', 'MFD_HUGE_1MB', 'MFD_HUGE_256MB', 'MFD_HUGE_2GB', 'MFD_HUGE_2MB',
    'MFD_HUGE_32MB', 'MFD_HUGE_512KB', 'MFD_HUGE_512MB', 'MFD_HUGE_64KB', 'MFD_HUGE_8MB',
    'MFD_HUGE_MASK', 'MFD_HUGE_SHIFT', 'Mapping', 'MutableMapping', 'NGROUPS_MAX',
    'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY',
    'O_DSYNC', 'O_EXCL', 'O_FSYNC', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY',
    'O_NOFOLLOW', 'O_NONBLOCK', 'O_PATH', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC',
    'O_TMPFILE', 'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE',
    'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL', 'POSIX_FADV_WILLNEED',
    'POSIX_SPAWN_CLOSE', 'POSIX_SPAWN_DUP2', 'POSIX_SPAWN_OPEN', 'PRIO_PGRP', 'PRIO_PROCESS',
    'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_PIDFD', 'P_WAIT',
    'PathLike', 'RTLD_DEEPBIND', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE',
    'RTLD_NOLOAD', 'RTLD_NOW', 'RWF_APPEND', 'RWF_DSYNC', 'RWF_HIPRI', 'RWF_NOWAIT',
    'RWF_SYNC', 'R_OK', 'SCHED_BATCH', 'SCHED_FIFO', 'SCHED_IDLE', 'SCHED_OTHER',
    'SCHED_RESET_ON_FORK', 'SCHED_RR', 'SEEK_CUR', 'SEEK_DATA', 'SEEK_END', 'SEEK_HOLE',
    'SEEK_SET', 'SPLICE_F_MORE', 'SPLICE_F_MOVE', 'SPLICE_F_NONBLOCK', 'ST_APPEND',
    'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID',
    'ST_RDONLY', 'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'WCONTINUED',
    'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED',
    'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED',
    'W_OK', 'XATTR_CREATE', 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK', '_Environ',
    '__all__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__',
    '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit',
    '_fspath', '_fwalk', '_get_exports_list', '_spawnvef', '_walk', '_wrap_close', 'abc',
    'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown', 'chroot', 'close',
    'closerange', 'confstr', 'confstr_names', 'copy_file_range', 'cpu_count', 'ctermid',
    'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ',
    'environb', 'error', 'eventfd', 'eventfd_read', 'eventfd_write', 'execl', 'execle',
    'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir',
    'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode',
    'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk',
    'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd',
    'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist',
    'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid',
    'getpriority', 'getrandom', 'getresgid', 'getresuid', 'getsid', 'getuid', 'getxattr',
    'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 'linesep', 'link', 'listdir',
    'listxattr', 'lockf', 'login_tty', 'lseek', 'lstat', 'major', 'makedev', 'makedirs',
    'memfd_create', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty',
    'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pidfd_open', 'pipe', 'pipe2',
    'popen', 'posix_fadvise', 'posix_fallocate', 'posix_spawn', 'posix_spawnp', 'pread',
    'preadv', 'putenv', 'pwrite', 'pwritev', 'read', 'readlink', 'readv', 'register_at_fork',
    'remove', 'removedirs', 'removexattr', 'rename', 'renames', 'replace', 'rmdir', 'scandir',
    'sched_get_priority_max', 'sched_get_priority_min', 'sched_getaffinity', 'sched_getparam',
    'sched_getscheduler', 'sched_param', 'sched_rr_get_interval', 'sched_setaffinity',
    'sched_setparam', 'sched_setscheduler', 'sched_yield', 'sendfile', 'sep', 'set_blocking',
    'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp',
    'setpriority', 'setregid', 'setresgid', 'setresuid', 'setreuid', 'setsid', 'setuid',
    'setxattr', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp',
    'spawnvpe', 'splice', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result', 'strerror',
    'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd',
    'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system',
    'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname',
    'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3',
    'wait4', 'waitid', 'waitid_result', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write',
    'writev']
    >>>


Otro ejemplo de uso, es poder usar el método ``file`` para determinar la
ubicación de la librería importada de la siguiente forma:

.. code-block:: pycon

    >>> os.__file__

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    '/usr/lib/python3.11/os.py'
    >>>

También puede consultar la documentación de la librería ``os`` ejecutando el
siguiente comando:

.. code-block:: pycon

    >>> print(os.__doc__)

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
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

.. code-block:: pycon

    >>> exit()


Asi pudo salir de la sesión del interprete interactivo ``python3``.

De esta forma aprendio nociones basicas con el interprete interactivo ``ipython``.


----


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

.. tabs::

   .. group-tab:: PIP

      .. code-block:: console

          pip3 install ipython

   .. group-tab:: Ubuntu/Debian Linux

      .. code-block:: console

          sudo apt install -y ipython

   .. group-tab:: Windows

      .. code-block:: console

          pip3 install ipython

Sustituya el comando ``python3`` por ``ipython3`` de la siguiente forma:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

          ipython3

     Si ejecuto el comando anterior, este da como resultado lo siguiente:

      .. code-block:: console
          :class: no-copy

          Python 3.11.2 (main, Nov 30 2024, 21:22:50) [GCC 12.2.0]
          Type 'copyright', 'credits' or 'license' for more information
          IPython 8.10.0 -- An enhanced Interactive Python. Type '?' for help.

              In [1]:

   .. group-tab:: Windows

      .. code-block:: console

          ipython3

     Si ejecuto el comando anterior, este da como resultado lo siguiente:

      .. code-block:: console
          :class: no-copy

          Python 3.11.5 (default, Sep 11 2023, 13:26:23)
          Type 'copyright', 'credits' or 'license' for more information
          IPython 7.34.0 -- An enhanced Interactive Python. Type '?' for help.

              In [1]:


Un ejemplo de uso del comando ``help`` es consultar la ayuda del comando
``dir`` y se ejecuta de la siguiente forma:

.. code-block:: pycon

    In [1]: help(dir)

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

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


Entonces presione la tecla :keys:`q` para salir de la ayuda de la función ``dir()``.

De nuevo realice la importación de la librería del estándar Python llamada ``os``.

.. code-block:: pycon

    In [2]: import os


También consultar los detalles acerca del 'objeto' para esto use como ejemplo
la librería ``os`` ejecutando el siguiente comando:

.. code-block:: pycon

    In [2]: os?

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Type:        module
    String form: <module 'os' (frozen)>
    File:        /usr/lib/python3.11/os.py
    Docstring:
    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
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


Escriba la librería ``os.`` y luego escribe dos **underscore** y presione *dos
veces la tecla tabular* :keys:`Tab` para usar la completado automático del interprete al
`estilo de completación de lineas de comandos`_ en el shell UNIX/Linux para
ayudar a la introspección del lenguaje y sus librerías.

.. code-block:: pycon

    In [3]: os.__
    __all__      __file__     __package__
    __builtins__ __loader__   __spec__
    __doc__      __name__
    instance


De nuevo ejecute el método ``file`` para determinar la ubicación de la
librería importada:

.. code-block:: pycon

    In [4]: os.__file__

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Out[4]: '/usr/lib/python3.11/os.py'

También puede consultar la documentación de la librería ``os`` de la
siguiente forma:

.. code-block:: pycon

    In [5]: print(os.__doc__)

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    OS routines for NT or Posix depending on what system we're on.

    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
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

.. code-block:: pycon

    In[6]: os.__name__

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Out[6]: "os"


Y otra forma de consultar la documentación de la librería ``os`` es
ejecutando el siguiente comando:

.. code-block:: pycon

    In [7]: help(os)

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Help on module os:

    NAME
        os - OS routines for NT or Posix depending on what system we're on.

    MODULE REFERENCE
        https://docs.python.org/3.11/library/os.html

        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.

    DESCRIPTION
        This exports:
          - all functions from posix or nt, e.g. unlink, stat, etc.
          - os.path is either posixpath or ntpath
          - os.name is either 'posix' or 'nt'
          - os.curdir is a string representing the current directory (always '.')
          - os.pardir is a string representing the parent directory (always '..')
          - os.sep is the (or a most common) pathname separator ('/' or '\\')
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

Entonces presione la tecla :keys:`q` para salir de la ayuda del módulo ``os``.

Y para cerrar la sesión con el ``ipython`` ejecute el siguiente comando:

.. code-block:: pycon

    In [8]: exit()

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    Do you really want to exit ([y]/n)? y

Entonces presione la tecla :keys:`y` para salir de interprete interactivo ``ipython``.

De esta forma aprendio nociones basicas con el interprete interactivo ``ipython``.


----


.. _python_modulo_bpython:

Interprete bpython
..................

Alternativamente puedes usar el paquete ``bpython`` que mejora aun más la experiencia
de trabajo con el paquete :ref:`ipython <python_interprete_interactivo>`.

Para mayor información visite su página principal de `interprete bpython`_ y si necesita
instalar este programa ejecute el siguiente comando:

..
    .. code-block:: console

        sudo apt install -y python-pip

.. code-block:: console

    pip3 install bpython

Luego cierra sesión de **root** y vuelve al usuario y sustituya el comando
``python`` por ``bpython`` de la siguiente forma:

.. code-block:: console

    bpython

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: console
    :class: no-copy

    bpython version 0.25 on top of Python 3.11.2 /usr/bin/python
    >>>

Dentro de interprete Python puede apreciar que ofrece otra forma de presentar
la documentación y la estructura del lenguaje, con los siguientes comandos de ejemplos:

.. code-block:: console

    >>> print('Hola Mundo')

Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: console
    :class: no-copy

    Hola Mundo

.. code-block:: console
    :class: no-copy

    >>> for item in range(
    ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
    │ range: (stop)                                                                        │
    │ stop=                                                                                │
    │ range(stop) -> range object                                                          │
    │ range(start, stop[, step]) -> range object                                           │
    │                                                                                      │
    │ Return an object that produces a sequence of integers from start (inclusive)         │
    │ to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.            │
    │ start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.             │
    │ These are exactly the valid indices for a list of 4 elements.                        │
    │ When step is given, it specifies the increment (or decrement).                       │
    └──────────────────────────────────────────────────────────────────────────────────────────────┘

Y para cerrar la sesión con el ``bpython`` ejecute el siguiente comando:

.. code-block:: pycon

    >>> exit()


Si ejecuto el comando anterior, este da como resultado lo siguiente:

.. code-block:: pycon
    :class: no-copy

    (None,)

Asi pudo salir de la sesión del interprete interactivo ``bpython``.

De esta forma, ha aprendió nociones básicas con el interprete interactivo ``bpython``.


----


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


.. raw:: html
   :file: ../_templates/partials/soporte_profesional.html


..
  .. disqus::


.. _`Python`: https://www.python.org/
.. _`Javadoc`: https://es.wikipedia.org/wiki/Javadoc
.. _`diagramas de clases`: https://es.wikipedia.org/wiki/Diagrama_de_clases
.. _`Sphinx`: https://en.wikipedia.org/wiki/Sphinx_%28documentation_generator%29
.. _`librería del estándar`: https://docs.python.org/es/3.11/library/index.html
.. _`modo interactivo`: https://es.wikipedia.org/wiki/Python#Modo_interactivo
.. _`SciPy`: https://en.wikipedia.org/wiki/SciPy
.. _`ipython`: https://ipython.readthedocs.io/en/stable/
.. _`bpython`: https://pypi.org/project/bpython/
.. _`interprete bpython`: https://bpython-interpreter.org/
.. _`estilo de completación de lineas de comandos`: https://en.wikipedia.org/wiki/Command_line_completion
