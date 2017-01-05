@echo off
::: 実行前の準備
set EXEC_DIR=%~dp0

::: python
rem PATH=C:\Python27;C:\Python27\Scripts;%PATH%

cd %EXEC_DIR%
PROMPT #$S

%ComSpec%