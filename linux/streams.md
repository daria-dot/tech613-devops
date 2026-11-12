# Streams

**What are streams**

A stream is a channel that data flows through, into or out of a program. Each command is like having three pipes attached to it. By default all three are connect to the terminal, there input from keyboard and output on the screen.

Number	|Name	|Default	|Used for
|------|------|----------|----------
0	|stdin |standard input|	keyboard data going into a command
1	|stdout |standard output|	screen	normal results
2	|stderr |standard error|	screen	error messages


when runnning `ls` on touch new.txt and missing_dir, two outputs were produced

- new.txt, the success, sent to stdout (1)
- ls: cannot access 'missing_directory'..., the failure, sent to stderr (2)

### Re-directing one steam at a time
`ls missing_directory new.txt > out.txt`

 redirected only stdout into the file. The error still appeared on screen, and out.txt held only new.txt.

 `ls missing_directory new.txt 2> err.txt`

 2> redirected only stderr. Now new.txt stayed on screen, and the error went into err.txt.

 ### Re directing both streams to separate files

 `ls missing_directory new.txt > out2.txt 2> err2.txt`

 Uses both re-directs at once, result went to one file and errors to the other - to log them separately

 ### Which stream does `> `redirect by default?
 stdout(1) 
 ### How can we direct both output streams to a file in one command?
 `ls missing_directory new.txt > both2.txt 2>&1`

 `> file 2>&1` means take output, then send stream 2 to wherever stream 1 is going