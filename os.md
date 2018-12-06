Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

FILE
    /usr/lib/python2.7/os.py

MODULE DOCS
    http://docs.python.org/library/os

DESCRIPTION
    This exports:
      - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
      - os.path is one of the modules posixpath, or ntpath
      - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator ('.' or '/')
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

CLASSES
    __builtin__.object
        posix.stat_result
        posix.statvfs_result
    exceptions.EnvironmentError(exceptions.StandardError)
        exceptions.OSError
    
    error = class OSError(EnvironmentError)
     |  OS system call failed.
     |  
     |  Method resolution order:
     |      OSError
     |      EnvironmentError
     |      StandardError
     |      Exception
     |      BaseException
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from EnvironmentError:
     |  
     |  __reduce__(...)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from EnvironmentError:
     |  
     |  errno
     |      exception errno
     |  
     |  filename
     |      exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __setstate__(...)
     |  
     |  __unicode__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __dict__
     |  
     |  args
     |  
     |  message
    
    class stat_result(__builtin__.object)
     |  stat_result: Result from stat or lstat.
     |  
     |  This object may be accessed either as a tuple of
     |    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
     |  or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
     |  
     |  Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
     |  or st_flags, they are available as attributes only.
     |  
     |  See os.stat for more information.
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __contains__(...)
     |      x.__contains__(y) <==> y in x
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __len__(...)
     |      x.__len__() <==> len(x)
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __mul__(...)
     |      x.__mul__(n) <==> x*n
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __reduce__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __rmul__(...)
     |      x.__rmul__(n) <==> n*x
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  st_atime
     |      time of last access
     |  
     |  st_blksize
     |      blocksize for filesystem I/O
     |  
     |  st_blocks
     |      number of blocks allocated
     |  
     |  st_ctime
     |      time of last change
     |  
     |  st_dev
     |      device
     |  
     |  st_gid
     |      group ID of owner
     |  
     |  st_ino
     |      inode
     |  
     |  st_mode
     |      protection bits
     |  
     |  st_mtime
     |      time of last modification
     |  
     |  st_nlink
     |      number of hard links
     |  
     |  st_rdev
     |      device type (if inode device)
     |  
     |  st_size
     |      total size, in bytes
     |  
     |  st_uid
     |      user ID of owner
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  n_fields = 16
     |  
     |  n_sequence_fields = 10
     |  
     |  n_unnamed_fields = 3
    
    class statvfs_result(__builtin__.object)
     |  statvfs_result: Result from statvfs or fstatvfs.
     |  
     |  This object may be accessed either as a tuple of
     |    (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
     |  or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
     |  
     |  See os.statvfs for more information.
     |  
     |  Methods defined here:
     |  
     |  __add__(...)
     |      x.__add__(y) <==> x+y
     |  
     |  __contains__(...)
     |      x.__contains__(y) <==> y in x
     |  
     |  __eq__(...)
     |      x.__eq__(y) <==> x==y
     |  
     |  __ge__(...)
     |      x.__ge__(y) <==> x>=y
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __gt__(...)
     |      x.__gt__(y) <==> x>y
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  __le__(...)
     |      x.__le__(y) <==> x<=y
     |  
     |  __len__(...)
     |      x.__len__() <==> len(x)
     |  
     |  __lt__(...)
     |      x.__lt__(y) <==> x<y
     |  
     |  __mul__(...)
     |      x.__mul__(n) <==> x*n
     |  
     |  __ne__(...)
     |      x.__ne__(y) <==> x!=y
     |  
     |  __reduce__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __rmul__(...)
     |      x.__rmul__(n) <==> n*x
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  f_bavail
     |  
     |  f_bfree
     |  
     |  f_blocks
     |  
     |  f_bsize
     |  
     |  f_favail
     |  
     |  f_ffree
     |  
     |  f_files
     |  
     |  f_flag
     |  
     |  f_frsize
     |  
     |  f_namemax
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  n_fields = 10
     |  
     |  n_sequence_fields = 10
     |  
     |  n_unnamed_fields = 0

FUNCTIONS
    WCOREDUMP(...)
        WCOREDUMP(status) -> bool
        
        Return True if the process returning 'status' was dumped to a core file.
    
    WEXITSTATUS(...)
        WEXITSTATUS(status) -> integer
        
        Return the process return code from 'status'.
    
    WIFCONTINUED(...)
        WIFCONTINUED(status) -> bool
        
        Return True if the process returning 'status' was continued from a
        job control stop.
    
    WIFEXITED(...)
        WIFEXITED(status) -> bool
        
        Return true if the process returning 'status' exited using the exit()
        system call.
    
    WIFSIGNALED(...)
        WIFSIGNALED(status) -> bool
        
        Return True if the process returning 'status' was terminated by a signal.
    
    WIFSTOPPED(...)
        WIFSTOPPED(status) -> bool
        
        Return True if the process returning 'status' was stopped.
    
    WSTOPSIG(...)
        WSTOPSIG(status) -> integer
        
        Return the signal that stopped the process that provided
        the 'status' value.
    
    WTERMSIG(...)
        WTERMSIG(status) -> integer
        
        Return the signal that terminated the process that provided the 'status'
        value.
    
    abort(...)
        abort() -> does not return!
        
        Abort the interpreter immediately.  This 'dumps core' or otherwise fails
        in the hardest way possible on the hosting operating system.
    
    access(...)
        access(path, mode) -> True if granted, False otherwise
        
        Use the real uid/gid to test for access to a path.  Note that most
        operations will use the effective uid/gid, therefore this routine can
        be used in a suid/sgid environment to test if the invoking user has the
        specified access to the path.  The mode argument can be F_OK to test
        existence, or the inclusive-OR of R_OK, W_OK, and X_OK.
    
    chdir(...)
        chdir(path)
        
        Change the current working directory to the specified path.
    
    chmod(...)
        chmod(path, mode)
        
        Change the access permissions of a file.
    
    chown(...)
        chown(path, uid, gid)
        
        Change the owner and group id of path to the numeric uid and gid.
    
    chroot(...)
        chroot(path)
        
        Change root directory to path.
    
    close(...)
        close(fd)
        
        Close a file descriptor (for low level IO).
    
    closerange(...)
        closerange(fd_low, fd_high)
        
        Closes all file descriptors in [fd_low, fd_high), ignoring errors.
    
    confstr(...)
        confstr(name) -> string
        
        Return a string-valued system configuration variable.
    
    ctermid(...)
        ctermid() -> string
        
        Return the name of the controlling terminal for this process.
    
    dup(...)
        dup(fd) -> fd2
        
        Return a duplicate of a file descriptor.
    
    dup2(...)
        dup2(old_fd, new_fd)
        
        Duplicate file descriptor.
    
    execl(file, *args)
        execl(file, *args)
        
        Execute the executable file with argument list args, replacing the
        current process.
    
    execle(file, *args)
        execle(file, *args, env)
        
        Execute the executable file with argument list args and
        environment env, replacing the current process.
    
    execlp(file, *args)
        execlp(file, *args)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
    
    execlpe(file, *args)
        execlpe(file, *args, env)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env, replacing the current
        process.
    
    execv(...)
        execv(path, args)
        
        Execute an executable path with arguments, replacing current process.
        
            path: path of executable file
            args: tuple or list of strings
    
    execve(...)
        execve(path, args, env)
        
        Execute a path with arguments and environment, replacing current process.
        
            path: path of executable file
            args: tuple or list of arguments
            env: dictionary of strings mapping to strings
    
    execvp(file, args)
        execvp(file, args)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
        args may be a list or tuple of strings.
    
    execvpe(file, args, env)
        execvpe(file, args, env)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env , replacing the
        current process.
        args may be a list or tuple of strings.
    
    fchdir(...)
        fchdir(fildes)
        
        Change to the directory of the given file descriptor.  fildes must be
        opened on a directory, not a file.
    
    fchmod(...)
        fchmod(fd, mode)
        
        Change the access permissions of the file given by file
        descriptor fd.
    
    fchown(...)
        fchown(fd, uid, gid)
        
        Change the owner and group id of the file given by file descriptor
        fd to the numeric uid and gid.
    
    fdatasync(...)
        fdatasync(fildes)
        
        force write of file with filedescriptor to disk.
         does not force update of metadata.
    
    fdopen(...)
        fdopen(fd [, mode='r' [, bufsize]]) -> file_object
        
        Return an open file object connected to a file descriptor.
    
    fork(...)
        fork() -> pid
        
        Fork a child process.
        Return 0 to child process and PID of child to parent process.
    
    forkpty(...)
        forkpty() -> (pid, master_fd)
        
        Fork a new process with a new pseudo-terminal as controlling tty.
        
        Like fork(), return 0 as pid to child process, and PID of child to parent.
        To both, return fd of newly opened pseudo-terminal.
    
    fpathconf(...)
        fpathconf(fd, name) -> integer
        
        Return the configuration limit name for the file descriptor fd.
        If there is no limit, return -1.
    
    fstat(...)
        fstat(fd) -> stat result
        
        Like stat(), but for an open file descriptor.
    
    fstatvfs(...)
        fstatvfs(fd) -> statvfs result
        
        Perform an fstatvfs system call on the given fd.
    
    fsync(...)
        fsync(fildes)
        
        force write of file with filedescriptor to disk.
    
    ftruncate(...)
        ftruncate(fd, length)
        
        Truncate a file to a specified length.
    
    getcwd(...)
        getcwd() -> path
        
        Return a string representing the current working directory.
    
    getcwdu(...)
        getcwdu() -> path
        
        Return a unicode string representing the current working directory.
    
    getegid(...)
        getegid() -> egid
        
        Return the current process's effective group id.
    
    getenv(key, default=None)
        Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
    
    geteuid(...)
        geteuid() -> euid
        
        Return the current process's effective user id.
    
    getgid(...)
        getgid() -> gid
        
        Return the current process's group id.
    
    getgroups(...)
        getgroups() -> list of group IDs
        
        Return list of supplemental group IDs for the process.
    
    getloadavg(...)
        getloadavg() -> (float, float, float)
        
        Return the number of processes in the system run queue averaged over
        the last 1, 5, and 15 minutes or raises OSError if the load average
        was unobtainable
    
    getlogin(...)
        getlogin() -> string
        
        Return the actual login name.
    
    getpgid(...)
        getpgid(pid) -> pgid
        
        Call the system call getpgid().
    
    getpgrp(...)
        getpgrp() -> pgrp
        
        Return the current process group id.
    
    getpid(...)
        getpid() -> pid
        
        Return the current process id
    
    getppid(...)
        getppid() -> ppid
        
        Return the parent's process id.
    
    getresgid(...)
        getresgid() -> (rgid, egid, sgid)
        
        Get tuple of the current process's real, effective, and saved group ids.
    
    getresuid(...)
        getresuid() -> (ruid, euid, suid)
        
        Get tuple of the current process's real, effective, and saved user ids.
    
    getsid(...)
        getsid(pid) -> sid
        
        Call the system call getsid().
    
    getuid(...)
        getuid() -> uid
        
        Return the current process's user id.
    
    initgroups(...)
        initgroups(username, gid) -> None
        
        Call the system initgroups() to initialize the group access list with all of
        the groups of which the specified username is a member, plus the specified
        group id.
    
    isatty(...)
        isatty(fd) -> bool
        
        Return True if the file descriptor 'fd' is an open file descriptor
        connected to the slave end of a terminal.
    
    kill(...)
        kill(pid, sig)
        
        Kill a process with a signal.
    
    killpg(...)
        killpg(pgid, sig)
        
        Kill a process group with a signal.
    
    lchown(...)
        lchown(path, uid, gid)
        
        Change the owner and group id of path to the numeric uid and gid.
        This function will not follow symbolic links.
    
    link(...)
        link(src, dst)
        
        Create a hard link to a file.
    
    listdir(...)
        listdir(path) -> list_of_strings
        
        Return a list containing the names of the entries in the directory.
        
            path: path of directory to list
        
        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.
    
    lseek(...)
        lseek(fd, pos, how) -> newpos
        
        Set the current position of a file descriptor.
        Return the new cursor position in bytes, starting from the beginning.
    
    lstat(...)
        lstat(path) -> stat result
        
        Like stat(path), but do not follow symbolic links.
    
    major(...)
        major(device) -> major number
        Extracts a device major number from a raw device number.
    
    makedev(...)
        makedev(major, minor) -> device number
        Composes a raw device number from the major and minor device numbers.
    
    makedirs(name, mode=511)
        makedirs(path [, mode=0777])
        
        Super-mkdir; create a leaf directory and all intermediate ones.
        Works like mkdir, except that any intermediate path segment (not
        just the rightmost) will be created if it does not exist.  This is
        recursive.
    
    minor(...)
        minor(device) -> minor number
        Extracts a device minor number from a raw device number.
    
    mkdir(...)
        mkdir(path [, mode=0777])
        
        Create a directory.
    
    mkfifo(...)
        mkfifo(filename [, mode=0666])
        
        Create a FIFO (a POSIX named pipe).
    
    mknod(...)
        mknod(filename [, mode=0600, device])
        
        Create a filesystem node (file, device special file or named pipe)
        named filename. mode specifies both the permissions to use and the
        type of node to be created, being combined (bitwise OR) with one of
        S_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO. For S_IFCHR and S_IFBLK,
        device defines the newly created device special file (probably using
        os.makedev()), otherwise it is ignored.
    
    nice(...)
        nice(inc) -> new_priority
        
        Decrease the priority of process by inc and return the new priority.
    
    open(...)
        open(filename, flag [, mode=0777]) -> fd
        
        Open a file (for low level IO).
    
    openpty(...)
        openpty() -> (master_fd, slave_fd)
        
        Open a pseudo-terminal, returning open fd's for both master and slave end.
    
    pathconf(...)
        pathconf(path, name) -> integer
        
        Return the configuration limit name for the file or directory path.
        If there is no limit, return -1.
    
    pipe(...)
        pipe() -> (read_end, write_end)
        
        Create a pipe.
    
    popen(...)
        popen(command [, mode='r' [, bufsize]]) -> pipe
        
        Open a pipe to/from a command returning a file object.
    
    popen2(cmd, mode='t', bufsize=-1)
        Execute the shell command 'cmd' in a sub-process.  On UNIX, 'cmd'
        may be a sequence, in which case arguments will be passed directly to
        the program without shell intervention (as with os.spawnv()).  If 'cmd'
        is a string it will be passed to the shell (as with os.system()). If
        'bufsize' is specified, it sets the buffer size for the I/O pipes.  The
        file objects (child_stdin, child_stdout) are returned.
    
    popen3(cmd, mode='t', bufsize=-1)
        Execute the shell command 'cmd' in a sub-process.  On UNIX, 'cmd'
        may be a sequence, in which case arguments will be passed directly to
        the program without shell intervention (as with os.spawnv()).  If 'cmd'
        is a string it will be passed to the shell (as with os.system()). If
        'bufsize' is specified, it sets the buffer size for the I/O pipes.  The
        file objects (child_stdin, child_stdout, child_stderr) are returned.
    
    popen4(cmd, mode='t', bufsize=-1)
        Execute the shell command 'cmd' in a sub-process.  On UNIX, 'cmd'
        may be a sequence, in which case arguments will be passed directly to
        the program without shell intervention (as with os.spawnv()).  If 'cmd'
        is a string it will be passed to the shell (as with os.system()). If
        'bufsize' is specified, it sets the buffer size for the I/O pipes.  The
        file objects (child_stdin, child_stdout_stderr) are returned.
    
    putenv(...)
        putenv(key, value)
        
        Change or add an environment variable.
    
    read(...)
        read(fd, buffersize) -> string
        
        Read a file descriptor.
    
    readlink(...)
        readlink(path) -> path
        
        Return a string representing the path to which the symbolic link points.
    
    remove(...)
        remove(path)
        
        Remove a file (same as unlink(path)).
    
    removedirs(name)
        removedirs(path)
        
        Super-rmdir; remove a leaf directory and all empty intermediate
        ones.  Works like rmdir except that, if the leaf directory is
        successfully removed, directories corresponding to rightmost path
        segments will be pruned away until either the whole path is
        consumed or an error occurs.  Errors during this latter phase are
        ignored -- they generally mean that a directory was not empty.
    
    rename(...)
        rename(old, new)
        
        Rename a file or directory.
    
    renames(old, new)
        renames(old, new)
        
        Super-rename; create directories as necessary and delete any left
        empty.  Works like rename, except creation of any intermediate
        directories needed to make the new pathname good is attempted
        first.  After the rename, directories corresponding to rightmost
        path segments of the old name will be pruned until either the
        whole path is consumed or a nonempty directory is found.
        
        Note: this function can fail with the new directory structure made
        if you lack permissions needed to unlink the leaf directory or
        file.
    
    rmdir(...)
        rmdir(path)
        
        Remove a directory.
    
    setegid(...)
        setegid(gid)
        
        Set the current process's effective group id.
    
    seteuid(...)
        seteuid(uid)
        
        Set the current process's effective user id.
    
    setgid(...)
        setgid(gid)
        
        Set the current process's group id.
    
    setgroups(...)
        setgroups(list)
        
        Set the groups of the current process to list.
    
    setpgid(...)
        setpgid(pid, pgrp)
        
        Call the system call setpgid().
    
    setpgrp(...)
        setpgrp()
        
        Make this process the process group leader.
    
    setregid(...)
        setregid(rgid, egid)
        
        Set the current process's real and effective group ids.
    
    setresgid(...)
        setresgid(rgid, egid, sgid)
        
        Set the current process's real, effective, and saved group ids.
    
    setresuid(...)
        setresuid(ruid, euid, suid)
        
        Set the current process's real, effective, and saved user ids.
    
    setreuid(...)
        setreuid(ruid, euid)
        
        Set the current process's real and effective user ids.
    
    setsid(...)
        setsid()
        
        Call the system call setsid().
    
    setuid(...)
        setuid(uid)
        
        Set the current process's user id.
    
    spawnl(mode, file, *args)
        spawnl(mode, file, *args) -> integer
        
        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnle(mode, file, *args)
        spawnle(mode, file, *args, env) -> integer
        
        Execute file with arguments from args in a subprocess with the
        supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnlp(mode, file, *args)
        spawnlp(mode, file, *args) -> integer
        
        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnlpe(mode, file, *args)
        spawnlpe(mode, file, *args, env) -> integer
        
        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnv(mode, file, args)
        spawnv(mode, file, args) -> integer
        
        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnve(mode, file, args, env)
        spawnve(mode, file, args, env) -> integer
        
        Execute file with arguments from args in a subprocess with the
        specified environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnvp(mode, file, args)
        spawnvp(mode, file, args) -> integer
        
        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnvpe(mode, file, args, env)
        spawnvpe(mode, file, args, env) -> integer
        
        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    stat(...)
        stat(path) -> stat result
        
        Perform a stat system call on the given path.
    
    stat_float_times(...)
        stat_float_times([newval]) -> oldval
        
        Determine whether os.[lf]stat represents time stamps as float objects.
        If newval is True, future calls to stat() return floats, if it is False,
        future calls return ints. 
        If newval is omitted, return the current setting.
    
    statvfs(...)
        statvfs(path) -> statvfs result
        
        Perform a statvfs system call on the given path.
    
    strerror(...)
        strerror(code) -> string
        
        Translate an error code to a message string.
    
    symlink(...)
        symlink(src, dst)
        
        Create a symbolic link pointing to src named dst.
    
    sysconf(...)
        sysconf(name) -> integer
        
        Return an integer-valued system configuration variable.
    
    system(...)
        system(command) -> exit_status
        
        Execute the command (a string) in a subshell.
    
    tcgetpgrp(...)
        tcgetpgrp(fd) -> pgid
        
        Return the process group associated with the terminal given by a fd.
    
    tcsetpgrp(...)
        tcsetpgrp(fd, pgid)
        
        Set the process group associated with the terminal given by a fd.
    
    tempnam(...)
        tempnam([dir[, prefix]]) -> string
        
        Return a unique name for a temporary file.
        The directory and a prefix may be specified as strings; they may be omitted
        or None if not needed.
    
    times(...)
        times() -> (utime, stime, cutime, cstime, elapsed_time)
        
        Return a tuple of floating point numbers indicating process times.
    
    tmpfile(...)
        tmpfile() -> file object
        
        Create a temporary file with no directory entries.
    
    tmpnam(...)
        tmpnam() -> string
        
        Return a unique name for a temporary file.
    
    ttyname(...)
        ttyname(fd) -> string
        
        Return the name of the terminal device connected to 'fd'.
    
    umask(...)
        umask(new_mask) -> old_mask
        
        Set the current numeric umask and return the previous umask.
    
    uname(...)
        uname() -> (sysname, nodename, release, version, machine)
        
        Return a tuple identifying the current operating system.
    
    unlink(...)
        unlink(path)
        
        Remove a file (same as remove(path)).
    
    unsetenv(...)
        unsetenv(key)
        
        Delete an environment variable.
    
    urandom(...)
        urandom(n) -> str
        
        Return n random bytes suitable for cryptographic use.
    
    utime(...)
        utime(path, (atime, mtime))
        utime(path, None)
        
        Set the access and modified time of the file to the given values.  If the
        second form is used, set the access and modified times to the current time.
    
    wait(...)
        wait() -> (pid, status)
        
        Wait for completion of a child process.
    
    wait3(...)
        wait3(options) -> (pid, status, rusage)
        
        Wait for completion of a child process.
    
    wait4(...)
        wait4(pid, options) -> (pid, status, rusage)
        
        Wait for completion of a given child process.
    
    waitpid(...)
        waitpid(pid, options) -> (pid, status)
        
        Wait for completion of a given child process.
    
    walk(top, topdown=True, onerror=None, followlinks=False)
        Directory tree generator.
        
        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple
        
            dirpath, dirnames, filenames
        
        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).
        
        If optional arg 'topdown' is true or not specified, the triple for a
        directory is generated before the triples for any of its subdirectories
        (directories are generated top down).  If topdown is false, the triple
        for a directory is generated after the triples for all of its
        subdirectories (directories are generated bottom up).
        
        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment), and walk will only recurse into the
        subdirectories whose names remain in dirnames; this can be used to prune the
        search, or to impose a specific order of visiting.  Modifying dirnames when
        topdown is false is ineffective, since the directories in dirnames have
        already been generated by the time dirnames itself is generated. No matter
        the value of topdown, the list of subdirectories is retrieved before the
        tuples for the directory and its subdirectories are generated.
        
        By default errors from the os.listdir() call are ignored.  If
        optional arg 'onerror' is specified, it should be a function; it
        will be called with one argument, an os.error instance.  It can
        report the error to continue with the walk, or raise the exception
        to abort the walk.  Note that the filename is available as the
        filename attribute of the exception object.
        
        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.
        
        Caution:  if you pass a relative pathname for top, don't change the
        current working directory between resumptions of walk.  walk never
        changes the current directory, and assumes that the client doesn't
        either.
        
        Example:
        
        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print root, "consumes",
            print sum([getsize(join(root, name)) for name in files]),
            print "bytes in", len(files), "non-directory files"
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories
    
    write(...)
        write(fd, string) -> byteswritten
        
        Write a string to a file descriptor.

DATA
    EX_CANTCREAT = 73
    EX_CONFIG = 78
    EX_DATAERR = 65
    EX_IOERR = 74
    EX_NOHOST = 68
    EX_NOINPUT = 66
    EX_NOPERM = 77
    EX_NOUSER = 67
    EX_OK = 0
    EX_OSERR = 71
    EX_OSFILE = 72
    EX_PROTOCOL = 76
    EX_SOFTWARE = 70
    EX_TEMPFAIL = 75
    EX_UNAVAILABLE = 69
    EX_USAGE = 64
    F_OK = 0
    NGROUPS_MAX = 65536
    O_APPEND = 1024
    O_ASYNC = 8192
    O_CREAT = 64
    O_DIRECT = 16384
    O_DIRECTORY = 65536
    O_DSYNC = 4096
    O_EXCL = 128
    O_LARGEFILE = 0
    O_NDELAY = 2048
    O_NOATIME = 262144
    O_NOCTTY = 256
    O_NOFOLLOW = 131072
    O_NONBLOCK = 2048
    O_RDONLY = 0
    O_RDWR = 2
    O_RSYNC = 1052672
    O_SYNC = 1052672
    O_TRUNC = 512
    O_WRONLY = 1
    R_OK = 4
    SEEK_CUR = 1
    SEEK_END = 2
    SEEK_SET = 0
    ST_APPEND = 256
    ST_MANDLOCK = 64
    ST_NOATIME = 1024
    ST_NODEV = 4
    ST_NODIRATIME = 2048
    ST_NOEXEC = 8
    ST_NOSUID = 2
    ST_RDONLY = 1
    ST_RELATIME = 4096
    ST_SYNCHRONOUS = 16
    ST_WRITE = 128
    TMP_MAX = 238328
    WCONTINUED = 8
    WNOHANG = 1
    WUNTRACED = 2
    W_OK = 2
    X_OK = 1
    __all__ = ['altsep', 'curdir', 'pardir', 'sep', 'extsep', 'pathsep', '...
    altsep = None
    confstr_names = {'CS_LFS64_CFLAGS': 1004, 'CS_LFS64_LDFLAGS': 1005, 'C...
    curdir = '.'
    defpath = ':/bin:/usr/bin'
    devnull = '/dev/null'
    environ = {'LANG': 'en_US.UTF-8', 'TERM': 'xterm-256color'...NECTION':...
    extsep = '.'
    linesep = '\n'
    name = 'posix'
    pardir = '..'
    pathconf_names = {'PC_ASYNC_IO': 10, 'PC_CHOWN_RESTRICTED': 6, 'PC_FIL...
    pathsep = ':'
    sep = '/'
    sysconf_names = {'SC_2_CHAR_TERM': 95, 'SC_2_C_BIND': 47, 'SC_2_C_DEV'...


