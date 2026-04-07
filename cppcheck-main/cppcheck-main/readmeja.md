# Cppcheck

| Linux Build Status | Windows Build Status | Coverity Scan Build Status |
|:--:|:--:|:--:|
| [![Linux Build Status](https://img.shields.io/travis/danmar/cppcheck/master.svg?label=Linux%20build)](https://travis-ci.org/danmar/cppcheck) | [![Windows Build Status](https://img.shields.io/appveyor/ci/danmar/cppcheck/master.svg?label=Windows%20build)](https://ci.appveyor.com/project/danmar/cppcheck/branch/master) | [![Coverity Scan Build Status](https://img.shields.io/coverity/scan/512.svg)](https://scan.coverity.com/projects/512) |

## About the name

This program was originally named "C++check", but was later renamed to "Cppcheck".

Despite the name, Cppcheck is designed for both C and C++.

## Manual

The manual is available [online](https://cppcheck.sourceforge.io/manual.pdf).

## Build

You can use a compiler with C++11 support. A compiler with partial C++11 support may also work. If your compiler supports the C++11 features available in Visual Studio 2013 or GCC 4.8, it may be usable.

If you want to use the GUI, the Qt library is required.

When building the command-line tool, [PCRE](http://www.pcre.org/) is optional. It is used for rules.

There are several compilation options:
* cmake - cross-platform build tool
* Windows: Visual Studio (VS 2013 or later)
* Windows: Qt Creator + mingw
* gnu make
* g++ 4.8 (or later)
* clang++

### cmake

Example of compiling Cppcheck with cmake:

```shell
mkdir build
cd build
cmake ..
cmake --build .
```

If you need to specify the C++ standard, use:
-DCMAKE_CXX_STANDARD=11

If you need the Cppcheck GUI, use:
-DBUILD_GUI=ON

If you need regular-expression rules support (requires pcre), use:
-DHAVE_RULES=ON

### Visual Studio

The cppcheck.sln file is available. It is configured for Visual Studio 2019, but the platform toolset can be changed to newer or older versions. The solution contains x86 and x64 platform targets.

To compile with rules, select the "Release-PCRE" or "Debug-PCRE" configuration. Copy pcre.lib (or pcre64.lib for x64 builds) and pcre.h to /externals. The latest PCRE version for Visual Studio can be obtained from [vcpkg](https://github.com/microsoft/vcpkg).

### Qt Creator + MinGW

To build the command-line tool, PCRE.dll is required. It can be downloaded from:
http://software-download.name/pcre-library-windows/

### GNU make

Simple unoptimized build (no dependencies):

```shell
make
```

Recommended release build:

```shell
make MATCHCOMPILER=yes FILESDIR=/usr/share/cppcheck HAVE_RULES=yes CXXOPTS="-O2 -DNDEBUG"
```

Flags:

1. `MATCHCOMPILER=yes`
Uses Python for cppcheck optimization. Token::Match patterns are converted to C++ code at compile time.

2. `FILESDIR=/usr/share/cppcheck`
Specifies the directory where cppcheck configuration files (addon, cfg, platform) are stored.

3. `HAVE_RULES=yes`
Enables rules support (rules support requires PCRE).

4. `CXXOPTS="-O2 -DNDEBUG"`
Enables optimization options for most compilers, disables internal cppcheck debug code, and enables basic compiler warnings.

### g++ (for experts)

If you want to build Cppcheck without dependencies, use:

```shell
g++ -o cppcheck -std=c++11 -Iexternals -Iexternals/simplecpp -Iexternals/tinyxml2 -Ilib cli/*.cpp lib/*.cpp externals/simplecpp/simplecpp.cpp externals/tinyxml2/*.cpp
```

If you use `--rule` or `--rule-file`, dependency libraries are required:

```shell
g++ -o cppcheck -std=c++11 -lpcre -DHAVE_RULES -Iexternals -Iexternals/simplecpp -Iexternals/tinyxml2 -Ilib cli/*.cpp lib/*.cpp externals/simplecpp/simplecpp.cpp externals/tinyxml2/*.cpp
```

### MinGW

```shell
mingw32-make
```

### Other compilers/IDE

1. Create an empty project file / makefile.
2. Add all cpp files in cppcheck cli and the lib directory to that project file or makefile.
3. Add all cpp files in the externals folder to the project file or makefile.
4. Build.

### Cross-compiling Win32 command-line version on Linux

```shell
sudo apt-get install mingw32
make CXX=i586-mingw32msvc-g++ LDFLAGS="-lshlwapi" RDYNAMIC=""
mv cppcheck cppcheck.exe
```

## Website

https://cppcheck.sourceforge.io/
